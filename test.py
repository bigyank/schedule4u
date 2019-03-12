"""TODO
1) Assign user day to a single variable instead of using idex everywhere
"""
import tabula
from datetime import date
import calendar
import json

days = list(calendar.day_abbr)

date_today = date.today().strftime("%a")


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
        if user_input[0] in values[6]:
            min_schedule.append(values)
            display(values, user_input)
    save_to_json(user_input[0], min_schedule)


def save_to_json(group, re_list):
    """Save the user group into a json file"""
    file_name = group + ".json"
    with open(file_name, "w") as file:
        json.dump(re_list, file)


def display(values, user_input):
    try:
        user_day = user_input[1]
    except IndexError:
        if date_today == values[0].title():
            print((" ".join(str(x) for x in values)))
    else:
        if user_day.title() == values[0].title():
            print((" ".join(str(x) for x in values)))


def main(user_input):
    file_name = user_input[0] + ".json"
    try:
        with open(file_name) as file:
            contents = json.load(file)
    except FileNotFoundError:
        schedule = pdf_extract(user_input)
        user_group(schedule, user_input)
    else:
        user_group(contents, user_input)


user_input = input("Input: ").split()
main(user_input)
