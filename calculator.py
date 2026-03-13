class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        if not isinstance(self.num1, int) and not isinstance(self.num2, int):
            return "Please... Provide a Number"
        else:
            return self.num1 + self.num2

    def sub(self):
        if not isinstance(self.num1, int) and not isinstance(self.num2, int):
            return "Please... Provide a Number"
        else:
            return self.num1 - self.num2

    def mul(self):
        if not isinstance(self.num1, int) and not isinstance(self.num2, int):
            return "Please... Provide a Number"
        else:
            return self.num1 * self.num2
    
    def sqrt(self):
        if not isinstance(self.num1, int) and not isinstance(self.num2, int):
            return "Please... Provide a Number"
        else:
            return self.num1 ** self.num2

    def divide(self):
        if not isinstance(self.num1, int) and not isinstance(self.num2, int):
            return "Please... Provide a Number"
        else:
            return self.num1 / self.num2
