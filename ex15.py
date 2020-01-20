#!/usr/bin/python3

# So here's the deal. I'm currently working on example 15 from Learn Python
# the Hard Way and this is the relevant code. Get in the game

# Tells the script to import arguments from the initial 'run' command
# in terminal
from sys import argv

# Sets the variable names for initial arguments
script, filename = argv

# Creates a variable called txt that opens the file from args
txt = open(filename)

# Writes a quick descriptive line
print(f"Here's your file {filename}:")

# Reads out the contexts of the file, opened earlier into variable txt
print(txt.read())

# Prompts the user to enter the filename manually to illustrate opening
# from inside the script itself
print("Type the filename again:")

# Creates a variable called file_again out of user input of the file
# name to pull it a second time
file_again = input("> ")

# Creates a variable called txt that opens the file from args
txt_again = open(file_again)

# Prints that contents of the file in its entirety
print(txt_again.read())

txt.close()
txt_again.close()
