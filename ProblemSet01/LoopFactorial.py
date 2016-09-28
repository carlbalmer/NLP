def validateuserinput():
    while True:
        try:
            userinput = int(input("Please enter a number\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return userinput


def calculatefactorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

hello = "Hello!\n" \
        "I calculate" \
        " factorials\n"
print(hello)
inputNumber = validateuserinput()
print("The factorial of {0} is: {1}".format((str(inputNumber)), (str(calculatefactorial(inputNumber)))))
