class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def _validate(self):
        if not isinstance(self.num1,(int,float)) or not isinstance(self.num2,(int,float)):
            raise ValueError("Provide numeric values")

    def add(self):
        self._validate()
        return self.num1+self.num2

    def sub(self):
        self._validate()
        return self.num1-self.num2

    def mul(self):
        self._validate()
        return self.num1*self.num2

    def divide(self):
        self._validate()
        if self.num2==0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.num1/self.num2