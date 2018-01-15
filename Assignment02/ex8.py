#Establishes our format that will be used for the rest of this exercise
formatter = "{} {} {} {}"

#Uses the formatter in several different ways
#First, imputs number strings
print(formatter.format(1, 2, 3, 4))
#Second, imputs strings
print(formatter.format("one", "two", "three", "four"))
#Third, imputs boolians
print(formatter.format(True, False, False, True))
#Forth, imputs itself
print(formatter.format(formatter, formatter, formatter, formatter))
#Fifth, imputs the Neff Lab's hiku, plus one line
print(formatter.format(
    "This is DNA",
    "It looks like water to me",
    "OK, if you say so",
    "Steveeee"
))
