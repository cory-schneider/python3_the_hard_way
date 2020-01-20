#!/usr/bin/python3



tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

output = open("out.txt", "a+")

fat_cat = """
I'll do a list:
\t* Cat fo\vod
\t* Fish\bies
\t* Catnip\n\t* Grass
"""

total = (tabby_cat + "\n" + persian_cat + "\n" + backslash_cat + "\n" + fat_cat)

output.write(total)
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

def func()
    Yes I did just do that.
