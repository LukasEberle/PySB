import csv
from datetime import timedelta

times = {}


def main():
    pass


def new_prediction(used_time, predicted_time, alpha=0.1):
    return alpha * used_time + (1 - alpha) * predicted_time


def load_times():
    with open(filename, 'r', encoding='utf-8') as data:
        pass


if __name__ == '__main__':
    main()
