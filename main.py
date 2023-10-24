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


date_now = dt.date.today()
with open("progress_file.txt", "r") as fp:
    progress_dict = json.load(fp)

while True:
    print("plot\npu\nsq\ncr")
    user_input = input()

    day_difference = num_of_days(datetime.strptime(progress_dict["start_date"], "%Y-%m-%d").date(), dt.date.today())
    while len(progress_dict["push_ups"]) < day_difference + 1:
        progress_dict["push_ups"].append(0)
        progress_dict["squats"].append(0)
        progress_dict["crunches"].append(0)

    if user_input == "plot":

        x_axis = [i for i in range(1, day_difference+2)]

        plt.plot(x_axis, progress_dict["push_ups"], label="push ups")
        plt.plot(x_axis, progress_dict["squats"], label="squats")
        plt.plot(x_axis, progress_dict["crunches"], label="crunches")

        xint = range(min(x_axis), math.ceil(max(x_axis)) + 1)
        matplotlib.pyplot.xticks(xint)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()

        plt.show()
    if user_input == "pu":
        num_in = get_int_from_user()
        progress_dict["push_ups"][day_difference] += num_in
        with open("progress_file.txt", "w") as fp:
            json.dump(progress_dict, fp)
    if user_input == "sq":
        num_in = get_int_from_user()
        progress_dict["squats"][day_difference] += num_in
        with open("progress_file.txt", "w") as fp:
            json.dump(progress_dict, fp)
    if user_input == "cr":
        num_in = get_int_from_user()
        progress_dict["crunches"][day_difference] += num_in
        with open("progress_file.txt", "w") as fp:
            json.dump(progress_dict, fp)

