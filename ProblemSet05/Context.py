from ProblemSet05 import Utility

words = Utility.parse_words("input_ex3.txt")
can_context = []
general_context = []

for position, word in enumerate(words):
    if "can" == word:
        can_context.append(words[position - 1] + " can " + words[position + 1])

for position, word in enumerate(words):
    if "general" == word:
        general_context.append(words[position - 1] + " general " + words[position + 1])

can_context = sorted(can_context)
general_context = sorted(general_context)

Utility.print_list_to_file("can.txt", can_context)
Utility.print_list_to_file("general.txt", general_context)
