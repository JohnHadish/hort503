#How many types of people in binary
types_of_people = 10

#establishes string x, the joke
x = f"There are {types_of_people} types of people."

#establishes supposidly funny parts of the joke punchline in variables
binary = "binary"
do_not = "don't"

#The punchline, as a f-string with previous two variables
y = f"Those who know {binary} and those who {do_not}."

#Prints Joke
print(x)

#Prints punchline
print(y)

#Prints joke in an f variable that emphasizes who said it
print(f"I said: {x}")

#prints punchline string within another string to verify who said it
print(f"I also said: '{y}'")

#variable hilarious is established as False
hilarious = False

#asks question of if joke is funny and leaves room for a response
joke_evaluation = "Isn't that joke so funny?! {}"

#prints out joke evaluation with variable "hilarious" as response
print(joke_evaluation.format(hilarious))

#Establishes a left and right side of a string as two seperate variables
w = "This is the left side of..."
e = "a string with a right side."

#Puts together two string variables 
print(w + e)
