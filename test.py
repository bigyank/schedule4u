import tabula
from datetime import date
import calendar
import json


def pdf_extract(user_input):
    """Extracts the pdf file and keeps the
    data in a single dictionary"""
    min_schedule = []
    df = tabula.read_pdf("1.pdf", pages="all")
    # print(test)
    schedule = df.values.tolist()
    return schedule


def user_group(schedule, user_input):
    """Displays the schedule of the group
    that the user inputs"""
    min_schedule = []
    for values in schedule:
        if user_input in values[6]:
            min_schedule.append(values)
            if date_today == values[0].title():
                print((" ".join(str(x) for x in values)))
    save_to_json(user_input, min_schedule)


def save_to_json(group, re_list):
    """Save the user group into a json file"""
    file_name = group + ".json"
    with open(file_name, "w") as file:
        json.dump(re_list, file)


def main(user_input):
    file_name = user_input + ".json"
    try:
        with open(file_name) as file:
            contents = json.load(file)
    except FileNotFoundError:
        schedule = pdf_extract(user_input)
        user_group(schedule, user_input)
    else:
        user_group(contents, user_input)


days = list(calendar.day_abbr)

while True:
    user_input = input("Input: ").split()
    if len(user_input) == 2:
        if user_input[1] in days:
            date_today = user_input[1]
            break
        else:
            print("Please enter the correct format for Days")
    else:
        date_today = date.today().strftime("%a")
        break
main(user_input[0])
