class Calculator:
    def __init__(self, input1, input2):
        self.n1 = input1
        self.n2 = input2

    def adder(self):
        return self.n1 + self.n2

    def subtractor(self):
        return self.n1 - self.n2

    def multiplier(self):
        return self.n1 * self.n2

    def divider(self):
        return self.n1 / self.n2

    def clear(self):
        self.n1 = 0
        self.n2 = 0

calculator = Calculator(int(input("First Number: ")), int(input("Second Number: ")))
print("Adder: ", calculator.adder())
print("Subtractor: ", calculator.subtractor())
print("Multiplier: ", calculator.multiplier())
print("Divider: ", calculator.divider())
calculator.clear()