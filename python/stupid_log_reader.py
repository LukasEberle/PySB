import re
import csv
from os import listdir
from os.path import isfile, join


results_dir = join('C:\\', 'Users', 'Agando', 'Desktop', 'Uni', 'Thesis', 'results')
experiments = []
for x in listdir(results_dir):
    if not isfile(join(results_dir, x)):
        experiments.append(x)
print(experiments)
data_points = ['', 'Training Time', 'Binning/Reading Time', 'Filter Any Time', 'Filter Any Calls',
               'Filter Current Time', 'Filter Current Calls', 'User Time', 'System Time', 'CPU Percentage']


def main():
    result_table = [data_points]
    for entry in experiments:
        result_table.append(generate_entry(entry))
    print(result_table)


def generate_entry(directory):
    experiment_values = [directory]
    directory = join(results_dir, directory)
    experiment_values.append(get_training_time(join(directory, 'evaluation_overall.csv')))
    directory = join(directory, 'log')
    get_binning_time(directory)
    return experiment_values


def get_training_time(log_file):
    time = -1.0
    with open(log_file, "r", encoding="utf-8", errors="ignore") as evaluation:
        final_line = evaluation.readlines()[-1]
        time = float(final_line.split(',')[-1])
    return time


def get_binning_time(log_dir):
    log_files = []
    for x in listdir(log_dir):
        if isfile(join(log_dir, x)):
            log_files.append(x)
    log_file = join(log_dir, log_files[1])
    print(log_file)


def get_filter_time(log_dir):
    pass


def get_gnu_time(log_dir):
    pass


if __name__ == "__main__":
    main()
