#Yeh, I got argv down by now. This imports and unpacks the txt file
from sys import argv

script,  input_file = argv

#This line makes the function print_all which just prints the input file
def print_all(f):
    print(f.read())

#This rewinds the script, It appears that the program is smart enough to know where it is
#This does it letter by letter
def rewind(f):
    f.seek(0)

#This prints out 1 line, of line. read.line reads the line we are on
def  print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

#current file is now open
current_file = open(input_file)

#These do what the functon says they do with current file as the file
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#current_line thing is for counting which line we are on. We needed to rewind to be at
#the proper spot
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
