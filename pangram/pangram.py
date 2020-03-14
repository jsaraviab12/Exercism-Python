def is_pangram(sentence):
    abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in abc:
        if letter not in sentence.upper():
            return False
    return True
