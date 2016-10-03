import re

inputFile = open("input_ex3.txt", "r")
for line in inputFile:
    if re.search(r"[aA]{3,}", line) is not None:
        print(line)
