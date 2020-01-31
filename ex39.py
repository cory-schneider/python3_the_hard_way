#!/usr/bin/python3

# create a mapping of a state to abbreviation

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : ('Jacksonville', 'St. Pete')
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)

print("Michigan has: ", cities[states['Michigan']])

for state, abbrev in list(states.items()):
    print(f"{state} has {abbrev}")

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has cities {cities[abbrev]}")

state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

print(', '.join(sorted(cities)))

"""

Dictionaries are another form of Data Structure. Commonly used.
Used to *map* or *associate* things you want to store to keys you need to get
them.


"""
