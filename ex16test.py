#!/usr/bin/python3

from sys import argv

script, filename = argv

file = open(filename)
count_it = open(filename)

for_printing = file.read()
for_counting = len(count_it.readlines())

print(for_printing)
print(f"{filename} is a hefty {for_counting} lines long!")

file.close()
