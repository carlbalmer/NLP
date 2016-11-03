from ProblemSet05 import Utility


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def soundex(word):
    string_as_list = list(word)
    code = []
    code.append(string_as_list.pop(0))
    for i in range(0, len(string_as_list)):
        if codes[string_as_list[i]] is not 0 and code[-1] is not codes[string_as_list[i]]:
            code.append(str(codes[string_as_list[i]]))
    return "".join(code[:4]).upper()


codes = dict.fromkeys(["a", "e", "i", "o", "u", "h", "w", "y"], 0)
codes.update(dict.fromkeys(["b", "f", "p", "v"], 1))
codes.update(dict.fromkeys(["c", "g", "j", "k", "q", "s", "x", "z"], 2))
codes.update(dict.fromkeys(["d", "t"], 3))
codes.update(dict.fromkeys(["l"], 4))
codes.update(dict.fromkeys(["m", "n"], 5))
codes.update(dict.fromkeys(["r"], 6))

words = []
input_file = open("spelling.txt", "r")
for line in input_file:
    words.append(line.lower().split(" ")[2])
input_file.close()

soundex_dic = {}

for word in words:
    if not hasNumbers(word):
        soundex_dic[word] = soundex(word)

check_soundex = ["L1", "C535", "Z464"]

for key in soundex_dic.keys():
    Utility.append_string_to_file("soundex.txt", key + " -> " + soundex_dic[key])
    if soundex_dic[key] in check_soundex:
        Utility.append_string_to_file("soundex_filtered.txt", key + " -> " + soundex_dic[key])
