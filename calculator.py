number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number:"))
operate = input("choose which operate do you want to use( + | - | % | * | ** |  / |):")
if operate == "+":
    result = number_1 + number_2
elif operate == "-":
    result = number_1 - number_2
elif operate == "*":
    result = number_1 * number_2
elif operate == "/":
    result = number_1 / number_2
elif operate == "**":
    result = number_1 ** number_2
elif operate == "%":
    result = number_1 % number_2
print(result)

quit(input())
