import json
import datetime as dt
import math
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def num_of_days(date1, date2):
    return abs((date1 - date2).days)


def get_int_from_user() -> int:
    num_input = input()
    while not num_input.isdigit():
        print("not an integer")
        num_input = input()
    return int(num_input)


def get_name_from_user() -> str:
    while True:
        name_input = input()
        confirmation = input("ary you sure? if yes type in y")
        if confirmation == "y":
            return name_input


date_now = dt.date.today()
with open("progress_file.txt", "r") as fp:
    progress_dict = json.load(fp)

while True:
    print("plot\nadd\nlist")
    user_input = input()

    day_difference = num_of_days(datetime.strptime(progress_dict["start_date"], "%Y-%m-%d").date(), dt.date.today())
    days_since_update = (day_difference - len(progress_dict["push_ups"])) + 1
    for key in progress_dict:
        if key == "start_date":
            continue
        progress_dict[key] = progress_dict[key] + [0 for _ in range(1, days_since_update)]

    if user_input == "plot":

        x_axis = [i for i in range(1, day_difference+1)]

        for key in progress_dict:
            if key == "start_date":
                continue
            plt.plot(x_axis, progress_dict[key], label=key)

        xint = range(min(x_axis), math.ceil(max(x_axis)) + 1)
        matplotlib.pyplot.xticks(xint)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()

        plt.show()
    elif user_input == "add":
        name_in = get_name_from_user()
        progress_dict[name_in] = [0 for _ in range(0, len(progress_dict["push_ups"]) + 1)]
        with open("progress_file.txt", "w") as fp:
            json.dump(progress_dict, fp)
    elif user_input == "list":
        for key in progress_dict:
            if key == "start_date":
                continue
            print(key)
        print("------------------------")
    elif user_input != "start_date" and user_input in progress_dict:
        num_in = get_int_from_user()
        progress_dict[user_input][day_difference] += num_in
        with open("progress_file.txt", "w") as fp:
            json.dump(progress_dict, fp)
