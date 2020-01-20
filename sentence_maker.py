#!/usr/bin/python3

y = 0


def sentence_maker():

    y = input("How many words to string together? ")

    try:
        g = []
        x = 1
        y = int(y)
        for i in range(y):
            g.append(input("Word {} of {}> ".format(x,y)))
            x += 1
        return g
    except:
        print("Word Count must be an integer!")
        new_sentence = sentence_maker()

new_sentence = sentence_maker()

print(' '.join(new_sentence))
