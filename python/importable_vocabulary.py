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
    embolden_kanji(rows)
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
            cleaned_data = clean_data(entry)
            cleaned_data.append(tags)
            rows.append(cleaned_data)


def generate_tags(raw):
    """
    Takes in the name of the table, which resembles the tags of the contained vocabulary.

    :param raw:  A string containing the tags. It has the form "tag.csv".
                 Multiple tags are concatenated with '+' ("tag1+tag2.csv").
    :return: A list of tags
    """
    tag_string = raw[:-4]
    return tag_string.split("+")


def embolden_kanji(rows):
    """
    Adds HTML tags to embolden the Kanji Characters.

    :param rows: A list of lists with the Kanji Character in the first spot. It will be updated.
    """
    for r in rows:
        if not r[0] == " ":
            r[0] = "<b>" + r[0] + "</b>"


def clean_data(data):
    """
    Takes in the current data row, cleans it and returns a list of all entries.

    :param data: Current noisy data
    :return: List of cell content in the row
    """
    result = data[:-1]
    result = result.split(';')
    return result


if __name__ == "__main__":
    main()
