import pandas as pd

input_filename = "index"
output_filename = "output"

colum_dicts = {"担当教員": "teacher", "科目": "name", "時間割コード": "class_code"}

weekdays_ja = {"月","火","水","木","金"}
weekdays_en = {"mon", "tue", "wed", "thu", "fri"}
weekdays_dict = dict(zip(weekdays_ja, weekdays_en))


def html_to_json(input_filename: str, output_filename: str):
    
    df = pd.read_html(f"{input_filename}.html")

    df = df[6]
    df = df.dropna(axis='index', thresh=7)
    df = df.drop(columns="No.")

    # ja to english
    df = df.rename(columns=colum_dicts)

    # extracts each date and class 
    # TODO: support cases like "月3，月4"
    df["day_of_week"] = df["曜日・時限"].str[0]
    df["period"] = df["曜日・時限"].str[1]

    for ja, en in weekdays_dict.items():
        df["day_of_week"] = df['day_of_week'].str.replace(ja, en, regex=False)

    df = df.drop(columns=["学期", "開講"])


    with open(f"{output_filename}.json", "w", encoding="utf-8") as f:
        df.to_json(f, orient="records", force_ascii=False,
                double_precision=0)


if __name__== "__main__":
    html_to_json(input_filename, output_filename)
