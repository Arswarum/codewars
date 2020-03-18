import string

def is_pangram(s):
    for letter in string.ascii_lowercase:
        if letter in s.lower():
            return True
    return True

pangram = "The quick, brown fox jumps over the lazy dog!"
test.assert_equals(is_pangram(pangram), True)
