import re

# Reads file line by line and saves the matches into a list
inputFile = open("input_ex1.txt", "r")
matches = []
for line in inputFile:
    matches.extend(re.findall(r"\{(.*?)\}", line.lower()))
inputFile.close()

# Iterates throught the matches splits them and saves them into a list of all words and a list of pairs.
# A pair is a set of words that were in the same brackes together.
words = []
pairs = []
for text in matches:
    pairs.append(set(text.split("|")))  # set removes the duplicates
    words += text.split("|")

words = set(words)  # set removes the duplicates
synonyms = {}

# Iterates through all words and pairs creating a set of all pairs that contain a word.
# Then saving this set into a dictionary with the word as key.
for word in words:
    syn = set()
    for pair in pairs:
        if word in pair:
            syn = syn.union(pair)
    syn.remove(word)
    synonyms.update({word: syn})

print("The synonyms for \"amazing\" are : ", synonyms["amazing"])
print("The synonyms for \"hello\" are : ", synonyms["hello"])
