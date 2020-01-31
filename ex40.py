#!/usr/bin/python3

"""
Modules, Classes, and Objects
Python is an Object Oriented Programming language. Means there is a construct
in Python called a class that lets you structure in a particular way.
Using classes, you can build consistency into your programs so that they can be
used in a cleaner way. Or so they say...
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])
bulls_on_parade = Song(["They rally around the family",
                        "With a pocket full of shells."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
