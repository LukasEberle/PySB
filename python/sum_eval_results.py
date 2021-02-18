import csv
from os import listdir
from os.path import isfile, join

results_dir = join('C:\\', 'Users', 'Agando', 'Desktop', 'Uni', 'Thesis', 'results')
experiments = []
for x in listdir(results_dir):
    if not isfile(join(results_dir, x)):
        experiments.append(x)


def main():
    summary = []
    initial_table = join(results_dir, experiments[0], "evaluation_overall.csv")
    with open(initial_table, "r", encoding="utf-8", errors="ignore") as evaluation:
        first_line = evaluation.readlines()[0].split(',')
        first_line[len(first_line)-1] = first_line[len(first_line)-1][:-1]
        for i in range(0, len(first_line)):
            first_line[i] = first_line[i].replace(".", "")
        summary.append(first_line)
    for directory in experiments:
        table = join(results_dir, directory, "evaluation_overall.csv")
        with open(table, "r", encoding="utf-8", errors="ignore") as evaluation:
            final_line = evaluation.readlines()[-1].split(',')
            final_line[len(first_line)-1] = final_line[len(first_line)-1][:-1]
            final_line[0] = directory
            summary.append(final_line)
    with open(join(results_dir, "evaluation_summary.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(summary)


if __name__ == '__main__':
    main()
