import re


def main():
    fn = '../data/text.txt'
    with open(fn, 'r', encoding='utf-8') as data:
        msg = data.read()
        print(get_american_numbers(msg))


def get_american_numbers(msg):
    american_format = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    match_object = american_format.findall(msg)
    if not match_object:
        return None
    return match_object


def get_german_numbers(msg):
    german_format = re.compile(r'')


if __name__ == "__main__":
    main()
