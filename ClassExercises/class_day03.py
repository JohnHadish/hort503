#This script imports a file and writes it to a new file
#Using the argv method
from sys import argv

script, input_file, output_file = argv

indata = open(input_file).read()

print(f"The length of the input file is {len(indata)}.")
print(f"Copying {input_file} to {output_file}")

# Copies our data from input_file to output_file
open(output_file, "w").write(indata)
