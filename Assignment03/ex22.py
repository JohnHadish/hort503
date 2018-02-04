print() #Prints out words
+ #adds
/ # divides
- # subtracts
* #multiplies
% #remainder of division
> < # greater than and less than, returns a boolina
<= >= # Less to or equal and more than or equal
= #assign a variable
f"{variable}" # f string, allows for variables to be called in a string
TRUE T # True, a boolian value
FALSE F # False, a boolian value
"{}".format("") # puts format thing in the {}
formatter = "{} {} {} {}" formatter.format(1, 2, 3, 4) # Puts into formatter
\  #exclude this from the string
\n #puts a return in a string
"""  """ #allows you to have multiple lines of code readout
\t #tab\
\\ # backslash
end = ' ' # used to end a printy section with a space instead of a return (default is return)
input() #Takes an input from the user, can put text in the input bit
from sys import argv #Imports function argv from sys
script, input, input2, .... = argv # How argv is used to assign variables
open(filename, "w") #opens a file, can be saved as a variable. "w" means write, by default opens as read
filename.read() #reads a filename, can be used with print to print FILE
filename.truncate() #erases a file with name "filename"
filename.write("text") #writes text to a file with name "filename"
filename.close() #closes a file with "filename" as name
from os import exists
exists(filename) #checks to see if file exists
def function_name(input1, input2):
    function_operation(input) #This is a function that takes inputs and uses them. Can call function usin anythiong pretty much
filename.seek(0) # seeks a point in the file (in byts)
filename.readline() #reads the next line
