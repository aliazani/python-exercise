class NumberString:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)


five = NumberString(5)
print(five)
print(int(five))
print(float(five))

