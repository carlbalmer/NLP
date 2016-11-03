import re


def parse_words(filename):
    words = []
    input_file = open(filename, "r")
    for line in input_file:
        words.extend(re.findall(r"\b(\w+)\b", line.lower()))
    input_file.close()
    return words


def print_list_to_file(filename, _list):
    output_file = open(filename, 'w')
    for item in _list:
        output_file.write(item + "\n")
    output_file.close()


def append_string_to_file(filename, string):
    output_file = open(filename, 'a')
    output_file.write(string + "\n")
    output_file.close()
