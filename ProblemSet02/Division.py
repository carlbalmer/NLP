def validateuserinput():
    while True:
        try:
            a = [int(input("Please enter the first number\n")), int(input("Please enter the second number\n"))]
            a.sort()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return a


def calculatereciprocal(n):
    a = 1.0 / n
    return a


hello = "Hello!\n" \
        "I calculate" \
        " reciprocals\n"
print(hello)
inputNumbers = validateuserinput()
print("The reciprocals are:\n")
for i in range(inputNumbers[0] + 1, inputNumbers[1]):
    try:
        print(str(calculatereciprocal(i)) + "\n")
    except ZeroDivisionError:
        print("The number " + str(i) + " has no factorial")
