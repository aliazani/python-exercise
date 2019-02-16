def sqrt(number):
    guess = number / 2

    while abs(number - guess ** 2) > 0.0000000000001:
        # print('my guess ---->',guess)
        division = number / guess
        guess = (division + guess) / 2
    return guess


number = float(input('enter number:'))

print(sqrt(number))
