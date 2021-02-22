import re
import csv
from os import listdir
from os.path import isfile, join


results_dir = join('C:\\', 'Users', 'Agando', 'Desktop', 'Uni', 'Thesis', 'results')
experiments = []
for x in listdir(results_dir):
    if not isfile(join(results_dir, x)):
        experiments.append(x)
data_points = ['', 'Training Time', 'Binning/Reading Time', 'User Time', 'System Time', 'CPU Percentage']


def main():
    result_table = [data_points]
    for entry in experiments:
        result_table.append(generate_entry(entry))
    with open(join(results_dir, "results_overall_time.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(result_table)


def generate_entry(directory):
    experiment_values = [directory]
    directory = join(results_dir, directory)
    experiment_values.append(get_training_time(join(directory, 'evaluation_overall.csv')))
    directory = join(directory, 'log')
    log_file = get_logfile(directory)
    time_log = get_time_log(directory)
    # for i in get_bin_info(log_file):
    #     experiment_values.append(i)
    experiment_values.append(get_binning_time(log_file))
    for i in get_gnu_time(time_log):
        experiment_values.append(i)
    return experiment_values


def get_training_time(log_file):
    with open(log_file, "r", encoding="utf-8", errors="ignore") as evaluation:
        final_line = evaluation.readlines()[-1]
        time = float(final_line.split(',')[-1])
    return time


def get_bin_info(log_file):
    bin_info_format = re.compile(r'Number of Bins: (\d+) ;')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = bin_info_format.findall(log_lines)
        print(match_object)
        if match_object:
            min_bins = min(match_object)
            max_bins = max(match_object)
            total = 0
            number = 0
            sorted_list = []
            for i in match_object:
                total += int(i)
                sorted_list.append(int(i))
                number += 1
            avg_bins = total/number
            sorted_list.sort()
            median = sorted_list[int(total/2)]
            return [min_bins, median]
        else:
            return ['', '']



def get_binning_time(log_file):
    # Feature Binning took 2296135 microseconds
    bin_time_format = re.compile(r'Feature Binning took (\d+) microseconds')
    # Reading feature vector took 20385 microseconds.
    read_time_format = re.compile(r'Reading feature vector took (\d+) microseconds')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = bin_time_format.findall(log_lines)
        if match_object:
            time = float(match_object[-1]) / 10000000
        else:
            match_object = read_time_format.findall(log_lines)
            time = float(match_object[-1]) / 10000000
    return time


def get_gnu_time(log_file):
    # User time (seconds): 95.76
    user_time = re.compile(r'User time \(seconds\): (\d+\.\d+)')
    # System time (seconds): 1.69
    sys_time = re.compile(r'System time \(seconds\): (\d+\.\d+)')
    # Percent of CPU this job got: 689%
    cpu_percent = re.compile(r'Percent of CPU this job got: (\d\d\d)')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = user_time.findall(log_lines)
        t_user = float(match_object[0])
        match_object = sys_time.findall(log_lines)
        t_sys = float(match_object[0])
        match_object = cpu_percent.findall(log_lines)
        p_cpu = match_object[0]+'%'
    gnu_time = [t_user, t_sys, p_cpu]
    return gnu_time


def get_logfile(log_dir):
    log_files = []
    for x in listdir(log_dir):
        if isfile(join(log_dir, x)):
            log_files.append(x)
    log_file = join(log_dir, log_files[1])
    return log_file


def get_time_log(log_dir):
    log_files = []
    for x in listdir(log_dir):
        if isfile(join(log_dir, x)):
            log_files.append(x)
    log_file = join(log_dir, log_files[2])
    return log_file


if __name__ == "__main__":
    main()
