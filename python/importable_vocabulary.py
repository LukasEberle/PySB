import sys
import argparse
from os import listdir, makedirs
from os.path import isfile, join, exists
from gtts import gTTS

# Setting important parameters
parser = argparse.ArgumentParser()
parser.add_argument('--deck', help="The name of the vocabulary deck. It should be equal to the table directory.",
                    type=str)
parser.add_argument('--sound', help="This parameter determines, if the algorithm should generate a sound for each word",
                    type=bool, default=False)
args = parser.parse_args()
vocabulary_dir = join('C:\\', 'Users', 'Agando', 'Documents', 'Anki', args.deck)  # Build the complete directory
vocabulary_by_tags = [f for f in listdir(vocabulary_dir) if isfile(join(vocabulary_dir, f))]  # List all tables
sound_dir = ""
if args.sound:
    sound_dir = join(vocabulary_dir, 'sound')
    if not exists(sound_dir):
        makedirs(sound_dir)
        print(sound_dir)


def main():
    # Checking the result TODO: Remove later
    print(vocabulary_by_tags)
    rows = []
    for table in vocabulary_by_tags:
        read_vocabulary(rows, table)
    embolden_kanji(rows)
    rows = get_cue_card_list(rows)
    result_file = join(vocabulary_dir, args.deck+".txt")
    with open(result_file, "w", encoding="utf-8", errors="ignore") as data:
        for line in rows:
            cue_card = line[0] + "; " + line[1] + "; " + line[2] + "\n"
            data.write(cue_card)
    # Checking the result TODO: Remove later
    print(result_file)
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


def get_cue_card_list(rows):
    """
    Restructures the list, to resemble the final format.

    :param rows: Current raw data
    :return: The new format
    """
    cue_card_list = []
    for row in rows:
        entry = []
        if not row[0] == " ":
            entry.append(row[0] + " - ")
        else:
            entry.append("")
        entry[0] += row[1]
        entry.append(row[3])
        tags = ""
        for tag in row[4]:
            tags += tag
            tags += " "
        entry.append(tags)
        cue_card_list.append(entry)
    return cue_card_list


if __name__ == "__main__":
    main()
