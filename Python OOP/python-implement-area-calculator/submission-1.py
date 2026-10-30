import math


class AreaCalc:
    def calculate(self, length, width=None):
        return round(math.pi * (length * length), 2) if width is None else width * length


# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))
print(calc.calculate(4, 6))
