import re
import pyperclip


def main():
    text = pyperclip.paste()
    print(get_contact_information(text))


def get_american_numbers(msg):
    """
    We want to export American-Style phone numbers. Those could look like this:
    415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    :param msg: Message is the text which should be searched
    :return: A list of phone numbers
    """
    american_format = re.compile(r'(((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d((ext(\.)?\s|x)(\d{2,5}))?)')
    match_object = american_format.findall(msg)
    return match_object


def get_german_numbers(msg):
    """
    We want to export German-Style mobile phone numbers. Those could look like this:
    0123 123456, +49123 123456, 0049123 123456
    :param msg: Message is the text which should be searched
    :return: A list of phone numbers
    """
    german_format = re.compile(r'((\d\d\d\d|(\+|00)49\d\d\d)( \d+))')
    match_object = german_format.findall(msg)
    return match_object


def get_email(msg):
    email_format = re.compile(r'[a-zA-Z0-9.\-_]+@\w+\.\w+')
    match_object = email_format.findall(msg)
    return match_object


def get_main_group(numbers):
    result = []
    for i in range(0, len(numbers)):
        result.append(numbers[i][0])
    return result


def get_contact_information(msg):
    result = get_main_group(get_american_numbers(msg)) + get_main_group(get_german_numbers(msg)) + get_email(msg)
    if not result:
        return "There are no numbers or emails that could be extracted!"
    return result


if __name__ == "__main__":
    main()
