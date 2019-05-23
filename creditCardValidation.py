import re

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def is_valid_card_number(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-".
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    """

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

    for group in match.groups:
        if group[0] * 4 == group:
            return False
    return True

is_valid_card_number('245689655889696')
is_valid_card_number('123456789123456')
is_valid_card_number('5241250010365896')



def findCardNumber(string):
    # pattern = r"(^|\s+)(\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4})(?:\s+|$)"
    # pattern = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    pattern = r"([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$"
    match = re.search(pattern, string)

    if match:
        print(match.group(0))

findCardNumber("My Credict card number is 1234 1234 1832 1234")

findCardNumber("My Credict card number is 5241 2500 1036 5896")

findCardNumber("My Credict card number is 5241250010365896")
