import csv
import json
import os
from datetime import timedelta

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
    text_time = "00:15:26"
    print(str_h(text_time))
    print(str_min(text_time))
    print(str_sec(text_time))
    print(str_sec(text_time)+str_min(text_time))
    print(times)
    print(groups)
    print(translate_time(5, 115, 80))


def new_prediction(used_time, predicted_time, alpha=0.1):
    return alpha * used_time + (1 - alpha) * predicted_time


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


def translate_time(hours, minute, sec):
    formatted_sec = sec % 60
    formatted_min = minute + sec // 60
    formatted_hours = hours + formatted_min // 60
    formatted_min = formatted_min % 60
    return f"{formatted_hours}:{formatted_min}:{formatted_sec}"


def element_wise_add(first, second):
    result = []
    for (item1, item2) in zip(first, second):
        result.append(item1 + item2)
    return result


if __name__ == '__main__':
    main()
