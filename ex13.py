#!/usr/bin/python3
from sys import argv
# read the WYSS section for how to run this
script, input_file, min_doh, target_doh, output = argv

print("Script is called:", script)
print("Input csv is:", input_file)
print("Minimum Days on Hand is:", min_doh)
print("Target Days on Hand is:", target_doh)
print("Output txt is:", output)
spc_msg = input("Special message? (Publix ad coming? Last call on orders \
for xyz event?) ")

print(spc_msg)
