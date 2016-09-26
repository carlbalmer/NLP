import sys


# Validates that there are only two natural numbers in the args and sorts them in a list. Terminates otherwise.
def inputisvalid(argv):
    try:
        if len(argv) != 3:
            raise ValueError("Wrong number of arguments, please enter two Numbers")
        a = [int(argv[1]), int(argv[2])]
        a.sort()
        return a
    except ValueError:
        sys.exit("No valid input")


def sumupdifference(lower, upper):
    if lower == upper:
        return upper
    return upper + sumupdifference(lower, upper - 1)

numbers = inputisvalid(sys.argv)
print("The sum of all numbers from {0} to {1} is: {2}".format(str(numbers[0]), str(numbers[1]),
                                                              str(sumupdifference(numbers[0], numbers[1]))))
