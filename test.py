import tabula
from datetime import date
import calendar
import json
import glob
from tabulate import tabulate


def pdf_extract(group):
    """Extracts the pdf file and keeps the
    data in a single dictionary"""
    pdf_file = glob.glob("./*.pdf")
    min_schedule = []
    df = tabula.read_pdf(pdf_file[0], pages="all")
    schedule = df.values.tolist()
    return schedule


def user_group(schedule, group):
    """Extracts the schedule of the group
    that the user inputs"""
    min_schedule = []
    for values in schedule:
        if group in values[6]:
            min_schedule.append(values)
    save_to_json(group, min_schedule)
    display(min_schedule)


def display(group_schedule):
    today_schedule = []
    header = [
        "Time",
        "Class Type",
        "Module Title",
        "Lecturer",
        "Group",
        "Block",
        "Room",
    ]
    for values in group_schedule:
        if date_today == values[0].title():
            today_schedule.append(values[1:3] + values[4:])

    print(tabulate(today_schedule, headers=header, tablefmt="orgtbl"))


def save_to_json(group, min_schedule):
    """Save the user group into a json file"""
    file_name = group + ".json"
    with open(file_name, "w") as file:
        json.dump(min_schedule, file)


def main(group):
    file_name = group + ".json"
    try:
        with open(file_name) as file:
            contents = json.load(file)
    except FileNotFoundError:
        schedule = pdf_extract(group)
        user_group(schedule, group)
    else:
        display(contents)


days = list(calendar.day_abbr)

while True:
    user_input = input("Input: ").split()
    group = user_input[0]
    if len(user_input) == 2:
        if user_input[1] in days:
            date_today = user_input[1]
            break
        else:
            print("Please enter the correct format for Days")
    else:
        date_today = date.today().strftime("%a")
        break
main(group)
