#!/usr/bin/python3

"""
Modules, Classes, and Objects
Python is an Object Oriented Programming language. Means there is a construct
in Python called a class that lets you structure in a particular way.
Using classes, you can build consistency into your programs so that they can be
used in a cleaner way. Or so they say...
"""

class Math(object):

    def __init__(self, inventory):
        self.inventory = inventory

    def inv_to_doh(self):
        derived = lambda data: (data[0], data[1], data[2]/data[1], data[3]/data[1])
        calcd = list(map(derived, self.inventory))
        for i in calcd:
            print(f"{i[0]}\nRate of Sale: {i[1]}")
            print("Days on Hand:")
            print(f"1/27/2020: {int(i[2])}, 2/14/2020: {int(i[3])}\n")

# Using a variable to pass the data to the class / function
gb_nums = [("Pernicious IPA", 30, 150, 90),
            ("Burst", 10, 20, 40)]

great_bay = Math(gb_nums)

# Passing the data to the class / function
pepin = Math([("Pernicious IPA", 25, 100, 250),
                ("Burst", 5, 15, 35)])
print("-Great Bay-")
great_bay.inv_to_doh()
print("-Pepin-")
pepin.inv_to_doh()
