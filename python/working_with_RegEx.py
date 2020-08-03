import re


def main():
    fn = '../data/text.txt'
    with open(fn, 'r', encoding='utf-8') as data:
        msg = data.read()
        print(get_contact_information(msg))


def get_american_numbers(msg):
    american_format = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    match_object = american_format.findall(msg)
    return match_object


def get_german_numbers(msg):
    german_format = re.compile(r'(\d\d\d\d|(\+|00)49\d\d\d)( \d\d\d\d\d\d)')
    match_object = german_format.findall(msg)
    return match_object


def get_email(msg):
    email_format = re.compile(r'[a-zA-Z0-9.\-_]+@\w+\.\w+')
    match_object = email_format.findall(msg)
    return match_object


def get_contact_information(msg):
    result = get_american_numbers(msg) + get_german_numbers(msg) + get_email(msg)
    return result


if __name__ == "__main__":
    main()
