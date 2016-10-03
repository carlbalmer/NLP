import re

inputFile = open("input_ex4.txt", "r")
for line in inputFile:
    if re.search(r"^(?!b|B).*(?:\d){2,}", line) is not None:
        print(line)
