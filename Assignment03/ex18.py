#This one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#Takes two arguements and prints them out
def print_two_again(a1, arg2):
    print(f"arg1: {a1}, arg2: {arg2}")

#Takes 1 arguement and prints it out
def print_one(arg1):
    print(f"arg1: {arg1}")

#Takes no arguements!
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
