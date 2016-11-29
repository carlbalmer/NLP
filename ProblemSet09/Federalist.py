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

test_file = open("FederalistTest.txt", "r")
testWords = {}
docno = ""
in_text = False
for line in test_file:
    if "PUBLIUS" in line:
        in_text = False
    elif "<DOCNO>" in line:
        in_text = False
        docno = re.search(r">(.*?)<", line).group(0)[1:-1]
        print(docno)
    elif "</SOURCE>" in line:
        in_text = True
    elif in_text:
        if docno not in testWords:
            testWords[docno] = []
        testWords[docno].extend(sstemmer(re.findall(r"\b(\w+)\b", line.lower())))

for key in testWords.keys():
    testWords[key] = Counter(testWords[key])
    word_sum = sum(testWords[key].values())
    for k in testWords[key].keys():
        testWords[key][k] = testWords[key][k] / word_sum

for testDoc in testWords.keys():
    i = 1
    out = "Document " + testDoc + ": "
    distances = {}
    for author in words.keys():
        distances[author] = 0
        for key in words[author].keys():
            distances[author] = distances[author] + abs(words[author][key] - testWords[testDoc][key])
    for w in sorted(distances, key=distances.get, reverse=False):
        out += str(i) + ". " + w + " " + str(distances[w]) + " "
        i += 1
    print(out)
