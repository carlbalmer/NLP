import re

list_ = []
inputFile = open("input_ex2.txt", "r")
for line in inputFile:
    if re.search(r"(\.ch\b|ch/)", line) is not None:
        list_.append(line)
print(list_)
