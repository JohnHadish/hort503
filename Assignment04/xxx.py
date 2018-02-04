#Practice with dictionaries

List_of_Lab = {"Pipette" : "Sigma Aldrich",
                "Matt" : "Grad Student",
                "Conner" : "Undergrad",
                "John" : "Grad Student"}


#print(List_of_Lab)

#print("I am a bird")


for List_of_Lab, occupation in list(List_of_Lab.items()):
    print(f"{List_of_Lab} is a {occupation}")


x = len(List_of_Lab)
List_of_Lab['John'] = 'Tired'
print(List_of_Lab["John"])
#print(x)

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}
print(cities['CA'])
