import datetime
from lib.html_to_files import html_to_files


input_filename = "index" # input the fiename for the html file

output_filename = f"{datetime.date.today()}-all"

if __name__ == "__main__":
    html_to_files(input_filename, output_filename)
