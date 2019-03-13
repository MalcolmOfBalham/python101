ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("But there aren't 10 things in that list..")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
    "Corn", "Banana", "Girl", "Boy"]

while(len(stuff) != 10):
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"THere are {len(stuff)} items now")

print("There we go: ", stuff)

print("now doing some more things...")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

#ex39 dictionaries!

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is ", states['Florida'])

#now use the states and then the cities dictionary
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print(states)
print(states.items())

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has the abbreviation {abbrev}")

#print every city
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{city} has the abbreviation {abbrev}")

#now both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has the abbreviation {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print("-" * 10)
#safely get an abbreviation for a state that might not be there

state = states.get('Texas')

print(state)

if not state:
    print("Sorry, no texas")

state = states.get("Texas", "oops state doesn't exist")

#get a city with a default value
city = cities.get("TX", "No cities for specified state")
print(f"the city for state 'TX' is {city}")

#extra stuff
#sort the states
print(states)
#items returns both k,v. Sorted returns just the sorted v
print(states.items())
print(sorted(states))

for i, v in enumerate(states):
    print(i, v)
    
    