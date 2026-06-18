class Calculator:
    def __init__(self):
        pass
    @staticmethod
    def addition(x, y):
        return x + y
    @staticmethod
    def subtraction(x, y):
        return x-y
    @staticmethod
    def multiplication(x, y):
        return x*y
    @staticmethod
    def division(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        else:
            return x/y
