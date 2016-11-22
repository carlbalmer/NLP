import re
from collections import Counter


def sstemmer(strings):
    out = []
    for string in strings:
        if len(string) < 5:
            out.append(string)
        elif re.search(r"(?<!a|e)ies$", string) is not None:
            out.append(re.sub("ies$", "y", string))
        elif re.search(r"(?<!a|e|o)es$", string) is not None:
            out.append(re.sub("es$", "e", string))
        elif re.search(r"(?<!u|s)s$", string) is not None:
            out.append(re.sub("s$", "", string))
        else:
            out.append(string)

    return out


input_file = open("FederalistTraining.txt", "r")
words = {
    "hamilton": [],
    "madison": [],
    "jay": []
}
author = ""
in_text = False
for line in input_file:

    if "<DOCNO>" in line or "PUBLIUS" in line:
        in_text = False
    elif "</SOURCE>" in line:
        in_text = True
    elif not in_text:
        if line == "<AUTHOR> Alexander Hamilton </AUTHOR>\n":
            author = "hamilton"
        elif line == "<AUTHOR> James Madison </AUTHOR>\n":
            author = "madison"
        elif line == "<AUTHOR> John Jay </AUTHOR>\n":
            author = "jay"
    elif in_text:
        words[author].extend(sstemmer(re.findall(r"\b(\w+)\b", line.lower())))

input_file.close()

for key in words.keys():
    words[key] = Counter(words[key])
    word_sum = sum(words[key].values())
    for k in words[key].keys():
        words[key][k] = words[key][k] / word_sum

print("Hamilton Madison Jay")

for i in range(25):
    string = ""
    for key in words:
        string += words[key].most_common(25)[i][0] + " " + str(words[key].most_common(25)[i][1]) + " "
    print(string)

output_file = open("Hamilton", 'a')
for i in range(len(words["hamilton"].most_common())):
    output_file.write(str(i) + " " + str(words["hamilton"].most_common()[i][1]) + "\n")

output_file.close()
