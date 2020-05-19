#Problem Statement: Find multiple instances of a character in a python string
#https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]