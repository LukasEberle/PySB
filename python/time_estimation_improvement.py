import csv
import json
import sys
from datetime import timedelta

time_file = '../data/times_test.csv'
goal_file = '../data/working_set.json'
times = {}
with open(goal_file, 'r', encoding='utf-8') as data:
    times = json.load(data)

#arguments = sys.argv[1:]
#if len(arguments) < 1:
#    print("Please enter a filename")
#else:
#    filename = arguments[0]


def main():
    csv.Dialect.delimiter = ','
    load_times()
    text_time = "00:15:26"
    print(str_h(text_time))
    print(str_min(text_time))
    print(str_sec(text_time))
    print(str_sec(text_time)+str_min(text_time))


def new_prediction(used_time, predicted_time, alpha=0.1):
    return alpha * used_time + (1 - alpha) * predicted_time


def load_times():
    with open(time_file, 'r', encoding='utf-8') as data:
        time_reader = csv.reader(data, delimiter=',')
        next(time_reader)
        current_line = (next(time_reader))
        project = current_line[3]
        duration = current_line[11]
        print(f"You worked {duration} hours on {project}!")


def str_h(time_text):
    return int(time_text[0:2])


def str_min(time_text):
    return int(time_text[3:5])


def str_sec(time_text):
    return int(time_text[6:])


if __name__ == '__main__':
    main()
