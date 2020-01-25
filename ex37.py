#!/usr/bin/python3

import sys

class Teashop:
    def __init__(self, x, y):
        self.tea = x
        self.price = y

    def pricing(self):
        print(f"The {self.tea} tea is ${self.price}!")

class Dogtionary:

    def __init__(self, a, b, c):
        self.name = a
        self.breed = b
        self.age = c

    def dog_dicter(self):
        dog_dict[self.name] = self.breed, self.age

#Learning about with-as statements
def with_as(input):
    with open(input, 'r') as file:
        for line in file:
            print(line.strip())

x = sys.argv[1]
y = input("Should you do it? ")
z = input("Are you tired? ")

assert y == "yes"

if y and z == "yes":
    with_as(x)

iterations = 5

with open(x, 'r') as lang:
    for line in lang:
        if iterations == 0:
            break
        else:
            print(line.strip(), "- this is a language!")
            iterations -= 1

print("\n")

tea1 = Teashop("green", 2.50)
tea2 = Teashop("oolong", 3.50)

tea1.pricing()
tea2.pricing()

del tea1.price
tea1.price = 6.66
tea1.pricing()
print("\n")

dog1 = Dogtionary("Ollie", 3.5, "Pit Bull")
dog2 = Dogtionary("Isla", 3.5, "Monster")
dog3 = Dogtionary("Pepper", 10, "Sweet Pea Murder Dog")

dog_dict = {}

dog1.dog_dicter()
dog2.dog_dicter()
dog3.dog_dicter()

for i in dog_dict.keys():
    print(f"{i}, good dog. Here are the details: {dog_dict[i]}")
