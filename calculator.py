class Calculator:
    def addition(x, y):
        return x + y
    def subtraction(x, y):
        return x/y
    def multiplicatoin(x, y):
        return x*y
    def division(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        else:
            return x/y