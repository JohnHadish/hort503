#Imports module/library argv from sys
from sys import argv

#Import parameters of argv
script, filename = argv

#opens the file you request with argv
txt = open(filename)

#prints the text file from the argv import
print(f"Here's your file {filename}:")
#the print function
print(txt.read())

txt.close()

#prints the text file from in put instead of from argv
print("Type the filename again:")
#File prompt
file_again = input("> ")

#opens requested file
txt_again = open(file_again)

#prints from requested file
print(txt_again.read())

txt_again.close()
