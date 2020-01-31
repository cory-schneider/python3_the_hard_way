#!/usr/bin/python3

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not ten things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

"""
Notes:

When to use lists:
1. need to maintain order - listed order, not sorted order, lists don't
sort for you
2. If you need to access contents randomly by a number. Cardinal numbers -
starting at 0
3. If you need to go through contents linearly (first to last).
This is what for-loops are for.

Object Oriented Programming -
    refers to a type of programming (software design) in which programmers
    define the data type of a data structure, and also the types of operations
    (functions) that can be applied to that data structure.

    The main aim of OOP is to bind together the data and the functions that
    operate on them so that no other part of the code can access this data
    except that function

1. Encapsulation - mechanism of hiding of data implementation by restricting
access to public methods. Instance variables are kept private and accessor
methods are made public to achieve this.
2. Abstraction - means a concept or an idea which is not associated with
any particular instance. One class should not know the details of another
in order to use it, just knowing the interfaces should be good enough.
3. Inheritance - exjpresses an "is-a" and/or "has-a" relationship between two
objects. Using inheritance, in derived classes we can reuse the code of
existing super classes.
4. Polymorphism - means one name, many forms.
    Static Polymorphism - is achieved using method overloading
    Dynamic Polymorphism - achieved using method overriding
5. Class
6. Object

Class -
Method - a function that belongs to a class
Inheritance - defined as a way in which a particular class (subclass) inherits
features from its base class (superclass).

"""
