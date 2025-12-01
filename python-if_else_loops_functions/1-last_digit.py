#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimo = abs(number) % 10
if number < 0:
    ultimo = -ultimo
if ultimo > 5:
    print(f'Last digit of {number} is {ultimo} and is greater than 5')
elif ultimo == 0:
    print(f'Last digit of {number} is {ultimo} and is 0')
else:
    print(f'Last digit of {number} is {ultimo} and is less than 6 and not 0')
