import re
import csv
from os import listdir
from os.path import isfile, join

results_dir = join('C:\\', 'Users', 'Agando', 'Desktop', 'Uni', 'Thesis', 'results')
experiments = []
for x in listdir(results_dir):
    if not isfile(join(results_dir, x)):
        experiments.append(x)
data_points = ['', 'Training Time', 'Binning/Reading Time', 'Candidate Calls', 'Filter Any Time',
               'Filter Any Calls', 'Filter Current Time', 'Filter Current Calls', 'Max. Bins', 'Min. Bins', 'Avg. Bins',
               'Median Bins', 'User Time', 'System Time', 'CPU Percentage']


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
    experiment_values.append(get_binning_time(log_file))
    experiment_values.append(get_candidate_calls(log_file))
    for i in get_filter_time(log_file):
        experiment_values.append(i)
    for i in get_num_bin_stats(log_file):
        experiment_values.append(i)
    for i in get_gnu_time(time_log):
        experiment_values.append(i)
    return experiment_values


def get_training_time(log_file):
    with open(log_file, "r", encoding="utf-8", errors="ignore") as evaluation:
        final_line = evaluation.readlines()[-1]
        time = float(final_line.split(',')[-1])
    return time


def get_binning_time(log_file):
    # Feature Binning took 2296135 microseconds
    bin_time_format = re.compile(r'<Feature Binning Time:(\d+)>')
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


def get_candidate_calls(log_file):
    candidate_format = re.compile(r'<Candidate Calls: (\d+)>')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = candidate_format.findall(log_lines)
        candidate_calls = float(match_object[-1])/10
    return candidate_calls


def get_filter_time(log_file):
    # Filter Any Vector took 21386.7 seconds
    fav_format = re.compile(r'<Filter Any Time:(\d+\.\d+)>')
    # Filter Current Vector took 983.864 seconds
    fcv_format = re.compile(r'<Filter Current Time:(\d+\.\d+)>')
    # seconds and was called 130284 times
    fa_calls = re.compile(r'<Filter Any Calls:(\d+)>')
    fc_calls = re.compile(r'<Filter Current Calls:(\d+)>')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = fav_format.findall(log_lines)
        fa_time = float(match_object[-1]) / 10
        match_object = fcv_format.findall(log_lines)
        fc_time = float(match_object[-1]) / 10
        match_object = fa_calls.findall(log_lines)
        fa_calls = float(match_object[-1]) / 10
        match_object = fc_calls.findall(log_lines)
        fc_calls = float(match_object[-1]) / 10
    time_and_calls = [fa_time, fa_calls, fc_time, fc_calls]
    return time_and_calls


def get_num_bin_stats(log_file):
    num_bin_format = re.compile(r'<Number of Bins:(\d+)>')
    with open(log_file, "r", encoding="utf-8", errors="ignore") as log_text:
        log_lines = log_text.read()
        match_object = num_bin_format.findall(log_lines)
        data = []
        for i in match_object:
            data.append(int(i))
    return [max(data), min(data), sum(data)/len(data), data[int(len(data)/2)]]


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
        p_cpu = match_object[0] + '%'
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
