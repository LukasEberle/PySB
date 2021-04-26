import csv
import sys
from os import listdir
from os.path import isfile, join

# Setting important parameters
deck_name = sys.argv[0]  # Pass Directory with Vocabulary Tables, it should be the same as the resulting decks name
vocabulary_dir = join('C:\\', 'Users', 'Agando', 'Documents', 'Anki', 'GenkiI6')  # Build the complete directory
vocabulary_by_tags = [f for f in listdir(vocabulary_dir) if isfile(join(vocabulary_dir, f))]  # List all tables


def main():
    # Checking the result TODO: Remove later
    print(vocabulary_by_tags)
    rows = []
    for table in vocabulary_by_tags:
        read_vocabulary(rows, table)
    # Checking the result TODO: Remove later
    print(rows)


def read_vocabulary(rows, table):
    """
    This function writes the rows of the table as a list and adds the appropriate tags.

    :param rows: A list which should be appended to
    :param table: A table which provides the necessary data
    """
    tags = generate_tags(table)
    with open(join(vocabulary_dir, table), "r", encoding="utf-8", errors="ignore") as data:
        for entry in data.readlines():
            cleaned_data = entry[:-1]
            cleaned_data = cleaned_data.split(';')
            cleaned_data.append(tags)
            rows.append(cleaned_data)


def generate_tags(raw):
    """
    Takes in the name of the table, which resembles the tags of the contained vocabulary.

    :param raw:  A string containing the tags. It has the form "tag.csv".
                 Multiple tags are concatenated with '+' ("tag1+tag2.csv").
    """
    tag_string = raw[:-4]
    return tag_string.split("+")


if __name__ == "__main__":
    main()
