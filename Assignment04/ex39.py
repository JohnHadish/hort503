#Create a mapping of state to abbreviation
states = {
        'Oregon' : 'OR',
        'Florida' : 'FL',
        'California' : 'CA',
        'New York' : 'NY',
        'Mitchigan' : 'MI'
}

# Create a basic set of states and some cities in them
cities = {
        'CA' : 'San Fransisco',
        'MI' : 'Detroit',
        'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Mitchigan's abbreviation is: ", states['Mitchigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then the cities dict
print('-' * 10)
print("Mitchigan has: ", cities[states['Mitchigan']])
print("Florida has: ", cities[states['Florida']])

#print out every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abb in list(states.items()):
    print(f"{state} state is abbreviated {abb}")
    print(f"and has city {cities[abb]}")

print('-' * 10)
#safley get an abbreviation by state that might not be There
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', "Does Not Exisit")
print(f"The city for the state 'TX' is: {city}")
