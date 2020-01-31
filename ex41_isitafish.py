#!/usr/bin/python3

class Fish(object):

    def __init__(self, input):
        self.fish = input

    def is_fish(self):
        list_of_fish = [
        "salmon",
        "pike",
        "marlin",
        "bass",
        "bream",
        "carp",
        "trout",
        "tuna"
        ]
        if self.fish.lower() in list_of_fish:
            print(f"{self.fish} is indeed a fish!")
        else:
            print(f"I've never heard of a {self.fish}. Nope, never.")

fish_input = input("Name a fish!> ")

fish_input = Fish(fish_input)

fish_input.is_fish()
