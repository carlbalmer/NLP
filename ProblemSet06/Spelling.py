from collections import Counter

from ProblemSet05 import Utility


def char_range(start, end, step=1):
    for char in range(ord(start), ord(end) + 1, step):
        yield chr(char)


def delete(string):
    for i in range(0, len(string)):
        string_as_list = list(string)
        del string_as_list[i]
        removed_sting = "".join(string_as_list)
        if removed_sting in freqN_words:
            return removed_sting
    return None


def interchange(string):
    for i in range(0, len(string) - 1):
        string_as_list = list(string)
        buffer = string_as_list[i + 1]
        string_as_list[i + 1] = string_as_list[i]
        string_as_list[i] = buffer
        removed_sting = "".join(string_as_list)
        if removed_sting in freqN_words:
            return removed_sting
    return None


def replace(string):
    for i in range(0, len(string)):
        for x in char_range("a", "z"):
            string_as_list = list(string)
            string_as_list[i] = x
            removed_sting = "".join(string_as_list)
            if removed_sting in freqN_words:
                return removed_sting
    return None


def add(string):
    for i in range(0, len(string) + 1):
        for x in char_range("a", "z"):
            string_as_list = list(string)
            string_as_list.insert(i, x)
            removed_sting = "".join(string_as_list)
            if removed_sting in freqN_words:
                return removed_sting
    return None


def sstemmer(string):
    if delete(string) is not None:
        return string + " -> " + delete(string) + " (delete)"
    elif interchange(string) is not None:
        return string + " -> " + interchange(string) + " (interchange)"
    elif replace(string) is not None:
        return string + " -> " + replace(string) + " (replace)"
    elif add(string) is not None:
        return string + " -> " + add(string) + " (add)"
    else:
        return None


words = Utility.parse_words("input_ex1.txt")
word_counts = Counter(words)
freq1_words = []
freqN_words = []

for key in word_counts.keys():
    if word_counts[key] == 1:
        freq1_words.append(key)
    else:
        freqN_words.append(key)

for word in freq1_words:
    if sstemmer(word) is not None:
        Utility.append_string_to_file("spelling.txt", sstemmer(word))
