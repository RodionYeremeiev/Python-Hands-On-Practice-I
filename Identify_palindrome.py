import re


def is_palindrome(check_word: str):
    forward = ''.join(re.findall('[a-z]+', check_word.lower()))
    backward = forward[::-1]
    return forward == backward
