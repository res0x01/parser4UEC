import datetime
from lib.html_to_json import html_to_json


input_filename = "index" # input the fiename for the html file

output_filename = f"{datetime.date.today()}_all"

if __name__ == "__main__":
    html_to_json(input_filename, output_filename)
