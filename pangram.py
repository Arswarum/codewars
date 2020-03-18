import string

def is_pangram(s):
    for letter in string.ascii_lowercase:
        if letter in s.lower():
            return True
    return True
