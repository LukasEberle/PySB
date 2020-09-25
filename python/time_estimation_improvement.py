import csv
import json
import os
from math import floor
from datetime import datetime


class Time:
    def __init__(self, hours, minutes, seconds):
        m = minutes + floor(seconds / 60)
        h = hours + floor(m / 60)
        self.hms = [h, (m % 60), (seconds % 60)]

    def __add__(self, other):
        sec = self.hms[2] + other.hms[2]
        m = self.hms[1] + other.hms[1]
        h = self.hms[0] + other.hms[0]
        return Time(h, m, sec)

    def __mul__(self, other):
        sec = self.hms[2] + ((self.hms[1]+(self.hms[0] * 60)) * 60)
        sec = round(sec * other)
        return Time(0, 0, sec)

    def get_time(self):
        return self.hms


time_file = '../data/times_test.csv'
goal_file = '../data/working_set.json'
project_groups_file = '../data/project_association.json'
times = {}
groups = {}
with open(goal_file, 'r', encoding='utf-8') as data:
    times = json.load(data)
for key in times:
    times[key]["done"] = [0, 0, 0]
if os.path.isfile(project_groups_file):
    with open(project_groups_file, 'r', encoding='utf-8') as data:
        groups = json.load(data)


def main():
    csv.Dialect.delimiter = ','
    load_times()
    update_times()
    generate_new_plan()


def new_prediction(predicted_time, used_time, alpha=0.1):
    return (used_time * alpha) + (predicted_time * (1 - alpha))


def load_times():
    with open(time_file, 'r', encoding='utf-8') as data:
        time_reader = csv.reader(data, delimiter=',')
        next(time_reader)
        for row in time_reader:
            project = row[0]
            duration = row[3]
            if project in times.keys():
                times[project]["done"] = element_wise_add(times[project]["done"], [str_h(duration), str_min(duration), str_sec(duration)])
            elif project in groups.keys():
                project_group = groups[project]
                times[project_group]["done"] = element_wise_add(times[project_group]["done"], [str_h(duration), str_min(duration), str_sec(duration)])


def str_h(time_text):
    return int(time_text[0:2])


def str_min(time_text):
    return int(time_text[3:5])


def str_sec(time_text):
    return int(time_text[6:])


def element_wise_add(first, second):
    result = []
    for (item1, item2) in zip(first, second):
        result.append(item1 + item2)
    return result


def update_times():
    for key in times:
        goal = times[key]["goal"]
        done = times[key]["done"]
        goal_sec = Time(goal[0], goal[1], goal[2])
        done_sec = Time(done[0], done[1], done[2])
        new_goal = new_prediction(goal_sec, done_sec)
        times[key]["goal"] = new_goal.get_time()
        times[key]["done"] = done_sec.get_time()


def make_string(time_list):
    result = ""
    for digit in time_list:
        if result != "":
            result += ":"
        result += str(digit)
    return result


def make_title(name, data_format):
    date = datetime.date(datetime.now())
    return f"{date}" + f"{name}" + "." + f"{data_format}"


def generate_new_plan():
    f = open(make_title("plan", "txt"), "a")
    for project in times:
        f.write(project + ": " + make_string(times[project]["goal"]) + "\n")
    with open(make_title("working_set", "json"), 'w', encoding='utf-8') as new_plan:
        json.dump(times, new_plan)


if __name__ == '__main__':
    main()
