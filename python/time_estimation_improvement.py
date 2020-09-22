import csv
import json
import os
from math import floor


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
        sec = round(self.hms[2] * other)
        m = round(self.hms[1] * other)
        h = round(self.hms[0] * other)
        return Time(h, m, sec)

    def get_time(self):
        return self.hms


time_file = '../data/times_test.csv'
goal_file = '../data/working_set.json'
project_groups_file = '../data/project_association.json'
times = {}
groups = {}
with open(goal_file, 'r', encoding='utf-8') as data:
    times = json.load(data)
if os.path.isfile(project_groups_file):
    with open(project_groups_file, 'r', encoding='utf-8') as data:
        groups = json.load(data)


def main():
    csv.Dialect.delimiter = ','
    load_times()
    update_times()
    print(times)


def new_prediction(predicted_time, used_time, alpha=0.1):
    return (used_time * alpha) + (predicted_time * (1 - alpha))


def load_times():
    with open(time_file, 'r', encoding='utf-8') as data:
        time_reader = csv.reader(data, delimiter=',')
        next(time_reader)
        for row in time_reader:
            project = row[3]
            duration = row[11]
            if project in times.keys():
                times[project]["done"] = element_wise_add(times[project]["done"], [str_h(duration), str_min(duration), str_sec(duration)])


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
        times[key]["done"] = [0, 0, 0]


if __name__ == '__main__':
    main()
