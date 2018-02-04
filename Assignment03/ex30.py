#makes the variables "people" "cars" and "trucks"
people = 2
cars = 40
trucks = 15

#Determines if there are more cars than people
if cars > people:
#if there are more cars than people, prints following
    print("We should take the cars.")
    #if there are less cars than people, prints the folowing
elif cars < people:
    print("We should not take the cars.")
    #if there are the same amount, we can not decide
else:
    print("We can't decide.")
#Determines if we have too many trucks
if trucks > cars:
    #If there are more trucks than cars, that is too many
    print("That's too many trucks.")
    #If there are less trucks than cars, then maybe we can take them
elif trucks < cars:
    print("Maybe we could take the trucks.")
#If there are the same amount then we can not decide what to take
else:
    print("We still can't decide.")

#if people are more plentiful than trucks, then we should obviously take the trucks
if people > trucks:
    print("Alright, let's take the trucks.")
    #if the opposite is true, the trucks, cars and peole stay where they are 
else:
    print("Fine, let's stay home then.")
