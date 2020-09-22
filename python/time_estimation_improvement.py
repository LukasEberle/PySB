import csv
import json
import os


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hms = [hours, minutes, seconds]


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
    result = make_valid_time_str(formatted_hours)+":"
    result += make_valid_time_str(formatted_min)+":"+make_valid_time_str(formatted_sec)
    return result


def make_valid_time_str(time):
    round(time)
    if time/10 < 1:
        return f"0{time}"
    else:
        return f"{time}"


def translate_in_sec(hours, minutes, sec):
    whole_minutes = minutes + (hours * 60)
    return sec + (whole_minutes * 60)


def element_wise_add(first, second):
    result = []
    for (item1, item2) in zip(first, second):
        result.append(item1 + item2)
    return result


def to_list(time_str):
    return [str_h(time_str), str_min(time_str), str_sec(time_str)]


def update_times():
    for key in times:
        goal = times[key]["goal"]
        done = times[key]["done"]
        goal_sec = translate_in_sec(goal[0], goal[1], goal[2])
        done_sec = translate_in_sec(done[0], done[1], done[2])
        new_goal = new_prediction(goal_sec, done_sec)
        new_goal = translate_time(0, 0, new_goal)
        times[key]["goal"] = to_list(new_goal)
        times[key]["done"] = [0, 0, 0]


if __name__ == '__main__':
    main()
