import pandas as pd

input_filename = "index"
output_filename = "output"

colum_dicts = {"担当教員": "teacher", "科目": "name", "時間割コード": "class_code"}
colum_type = {"class_code": int, "lect_length": int}

weekdays_ja = ["月","火","水","木","金"]
weekdays_en = ["mon", "tue", "wed", "thu", "fri"]
weekdays_dict = dict(zip(weekdays_ja, weekdays_en))

parameters = ["type", "google_classroom", "webclass", "link", "link2", "zoom", "zoom_id", "zoom_password", "id", "password"]

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
    df["曜日・時限"] = df['曜日・時限'].str.replace("(,.他.)|(,)", '', regex=True)
    df["period"] = df["曜日・時限"].str[1]
    df["lect_length"] = (df["曜日・時限"].str.len()/2)

    # generates columns 
    df[parameters] = ""

    # cast float to int
    df = df.astype(colum_type)
    # change language
    for ja, en in weekdays_dict.items():
        df["day_of_week"] = df['day_of_week'].str.replace(ja, en, regex=False)
    
    # drops unsed columns
    df = df.drop(columns=["学期", "開講", "曜日・時限"])
    
    print("dataframe ready")


    # drops unsed columns
    df = df.drop(columns=["学期", "開講", "曜日・時限"])
    
    print("dataframe ready")

    def save_to_csv():
        print("saving to csv...")
        with open(f"{output_filename}.csv", "w", encoding="utf-8") as f:
            df.to_csv(f)
    
    def save_to_json():
        print("saving to json...")

        with open(f"{output_filename}.json", "w", encoding="utf-8") as f:
            df.to_json(f, orient="records", force_ascii=False, double_precision=0)
    

    save_to_csv()
    save_to_json()

if __name__== "__main__":
    html_to_json(input_filename, output_filename)
