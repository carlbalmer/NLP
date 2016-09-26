class ComplexNumber:
    def __init__(self, a=None, b=None):
        if a is not None and b is not None:
            self.a = a
            self.b = b
        else:
            self.a = 0
            self.b = 0

    def __str__(self):
        if self.b >= 0:
            return str(self.a) + "+" + str(self.b) + "i"
        else:
            return str(self.a) + str(self.b) + "i"

    def add(self, complex_number):
        return ComplexNumber(self.a + complex_number.a, self.b + complex_number.b)

    def sub(self, complex_number):
        return ComplexNumber(self.a - complex_number.a, self.b - complex_number.b)

one = ComplexNumber(12, 3)
two = ComplexNumber(2, 5)

print("The addition of {0} and {1} is:\n {2}\n and their substraction:\n {3}".format(str(one), str(two),
                                                                                     str(one.add(two)),
                                                                                     str(one.sub(two))))
