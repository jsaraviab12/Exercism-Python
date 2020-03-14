import re
from collections import Counter


aux = "(?:[0-9]+|[a-z]+(?:'[a-z])?)"


def count_words(sentence):
    return Counter(re.findall(aux, sentence.lower()))