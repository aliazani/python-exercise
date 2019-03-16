from random import randint

answer = 209
guess = randint(1, 2000)
print(guess)
mini = 1
maxi = 2000
count = 0
while guess != answer:

    guess = randint(mini, maxi)

    if guess > answer:

        maxi = guess

    elif guess < answer:

        mini = guess
    count += 1
    print(guess)

print(count)
