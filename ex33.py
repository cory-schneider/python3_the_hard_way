#!/usr/bin/python3

"""
def list_gen(length, increment):
    i = 0
    numbers =[]
    while i < length:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment
        if i >= length:
            print("Maxed out, the numbers are: ")
            print(numbers)
            break
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

answers = list_gen(11, 2)
"""

shoop = range(0,11,2)
numbers = []
print(len(shoop))
for i in shoop:
    print(f"At the top i is {i}")
    numbers.append(i)
    if i >= max(shoop):
        print("Maxed out, the numbers are: ")
        print(numbers)
        break
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i+1}")
