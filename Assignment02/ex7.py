#This writes out first line of poem
print("Mary had a little lamb.")

#This writes out second line of code. snow is addeed to the string as a format
print("Its fleece was white as {}.".format("snow"))

#prints out third line of code
print("And everywhere that Mary went.")

#This makes a period 10 times
print("." * 10) #This makes the period repeat 10 times

#Makes variable end1 - end 12, each containing 1 letter of CheeseBurger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch the comma at the end and see what happens when you remove it.
#Prints out cheese and a space
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')

#Prints out burger immediatly after cheese. The weird end = ' ' makes them be on
#the same line, but I dont know why.
print(end7 + end8 + end9 + end10 + end11 + end12)
