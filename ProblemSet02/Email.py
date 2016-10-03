import re

inputFile = open("input_ex5.txt", "r")
for line in inputFile:
    if re.search(r"^([A-Z]\D*)\.([A-Z]\D*)@(\S+)\.com\b", line) is not None:
        print(line)
