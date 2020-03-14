import re
def abbreviate(words):
    words = re.findall(r"['A-Z0-9]+", words.upper())
    return ''.join([word[0] for word in words])
