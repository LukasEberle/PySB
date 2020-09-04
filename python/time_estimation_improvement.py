import csv
import sys
from datetime import timedelta


times = {}
filename = '../data/times_test.csv'
#arguments = sys.argv[1:]
#if len(arguments) < 1:
#    print("Please enter a filename")
#else:
#    filename = arguments[0]


def main():
    csv.Dialect.delimiter = ','
    load_times()


def new_prediction(used_time, predicted_time, alpha=0.1):
    return alpha * used_time + (1 - alpha) * predicted_time


def load_times():
    with open(filename, 'r', encoding='utf-8') as data:
        time_reader = csv.reader(data, delimiter=',')
        next(time_reader)
        current_line = (next(time_reader))
        project = current_line[3]
        duration = current_line[11]
        print(f"You worked {duration} hours on {project}!")


if __name__ == '__main__':
    main()
