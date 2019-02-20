class NumberString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return f"{self.value}"

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):

        if '.' in self.value:
            return float(self) + other
        else:
            return int(self) + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        else:
            return int(self) * other

    def __rmul__(self, other):
        return self * other


five = NumberString(5)
print(five)
print(int(five))
print(float(five))
print(str(five))
print(five + 2)
print(2.2 + five)
print(five * 2)
print(10 * five)

