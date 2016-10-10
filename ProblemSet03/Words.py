import re
from collections import Counter

inputFile = open("input_ex3.txt", "r")
matches = []
for line in inputFile:
    matches.extend(re.findall(r"\b[a-z]{5,}", line))
inputFile.close()
word_counts = Counter(matches)

print("In total there are ", len(matches), " long words in the text and ", len(word_counts), " different long words\n")

print("The word \"people\" appears ", word_counts["people"], " times and \"health\" ", word_counts["health"],
      ".\nSo their relative frequency is ", word_counts["people"] / word_counts["health"], ".\n")

print("These word appear exactly 13 times:")
for k, v in iter(word_counts.items()):
    if v == 13:
        print(k, end=", ", flush=True)

print("Saving the five most common words to a file")
filename = str(input("Please enter the filename:\n"))
outputFile = open(filename, 'w')
for k, v in word_counts.most_common(5):
    outputFile.writelines(k + "\n")
