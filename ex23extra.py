#!/usr/bin/python3

import sys
script, input_encoding, error, output = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

    byte_out.write(str(raw_bytes)+"\n")

languages = open("languages.txt", encoding="utf-8")

byte_out = open(output, 'w')

main(languages, input_encoding, error)
