import argparse
from os import listdir, makedirs
from os.path import isfile, join, exists
from gtts import gTTS
import sys
import csv
import random

# Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument('--deck', help="The name of the vocabulary deck. It should be equal to the table directory.",
                    type=str)
parser.add_argument('--sound', help="This parameter determines, if the algorithm should generate a sound for each word",
                    type=bool, default=False)
args = parser.parse_args()

# Setting important paths
output_path = join('C:\\', 'Users', 'Agando', 'Documents', 'Anki')
vocabulary_file = args.deck + ".csv"
vocabulary_dir = join(output_path, args.deck)  # Build the complete directory
vocabulary_path = join(vocabulary_dir, vocabulary_file)
sound_dir = ""
if args.sound:
    sound_dir = join(vocabulary_dir, 'sound')
    if not exists(sound_dir):
        makedirs(sound_dir)


def main():
    rows = read_table()
    rows[0].append('Audio')
    rows[0].append('SentanceAudio')
    if args.sound:
        generate_pronunciations(rows)
    result_file = join(output_path, args.deck + ".txt")
    with open(result_file, "w", encoding="utf-8", errors="ignore") as data:
        for line in rows:
            cue_card = line[0] + "; " + line[1] + "; " + line[2] + "; " + line[3] + "; " + line[4] + "; " + line[5] + "\n"
            data.write(cue_card)


def read_table():
    r = []
    with open(vocabulary_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            r.append(row)
    return r


def generate_pronunciations(rows):
    print(f"Generating {len(rows)} pronunciations. This might take a while.")
    toolbar_width = 50  # Length of the progressbar
    # Setup progressbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    # Generating pronunciations
    for row in rows[1:]:
        # Generate Audio
        filename = pronounce(row[0])
        row.append("[sound:" + filename + "]")
        # Generate Sentence Audio
        if row[3] is not " ":
            filename = pronounce(row[3])
            row.append("[sound:" + filename + "]")
        else:
            row.append(" ")
        # Adding to the progressbar
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write("]\n")  # this ends the progress bar
    print("Successfully generated pronunciations.")


def pronounce(cue):
    tts = gTTS(cue, lang='ja')
    prefix = ""
    if len(cue) > 16:
        prefix = cue[:8] + get_random_string()
    else:
        prefix = cue
    filename = prefix + '.mp3'
    tts.save(join(sound_dir, filename))
    return filename


def get_random_string():
    random_string = ''

    for _ in range(8):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string


if __name__ == "__main__":
    main()
