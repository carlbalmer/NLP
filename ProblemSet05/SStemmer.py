import re

from ProblemSet05 import Utility


def sstemmer(string):
    if len(string) < 5:
        return None
    elif re.search(r"(?<!a|e)ies$", string) is not None:
        return re.sub("ies", "y", string)
    elif re.search(r"(?<!a|e|o)es$", string) is not None:
        return re.sub("es", "e", string)
    elif re.search(r"(?<!u|s)s$", string) is not None:
        return re.sub("s", "", string)
    else:
        return None


words = Utility.parse_words("input_ex3.txt")
pairs = []

for word in words:
    if sstemmer(word) is not None:
        pairs.append(word + " -> " + sstemmer(word))

pairs = sorted(list(set(pairs)))

Utility.print_list_to_file("stemmed.txt", pairs)
