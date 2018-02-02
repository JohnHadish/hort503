#This program asks a user for 10 float numbers, and averages them.

#Main function. This calls the other functions
def main():
    #Asks user how many variables they want to average
    how_many_numbers = int(input("How many numbers would you like to average? > "))
    print(f"Ok, this program will ask for you to input {how_many_numbers} numbers.")
    #Passes this to the function "request_numbers". Gets a vector back with the inputs
    #From the user
    List_of_Numbers = request_numbers(how_many_numbers)
    print(List_of_Numbers)
    #Sends List_of_Numbers that the user inputed to calculate_average
    Average = calculate_average(List_of_Numbers)
    print(Average)

#Request_numbers function. This requests numbers from the Request_numbers
def request_numbers(how_many):
    List_of_Numbers = []
    for i in range(how_many):
        List_of_Numbers.append(float(input(f"number {i + 1} > ")))
    return(List_of_Numbers)

#def request_numbers():
#    List_of_Numbers = []
#    Stop = False
#    while(Stop = False):
#        print("Insert numbers, press q when done")
#        x = input("Please insert number > ")
#        if
#Calculate_average. This calculates average of the numbers
def calculate_average(vector_to_average):
    total = 0
    for i in vector_to_average:
        total += i
    average = total / len(vector_to_average)
    return(average)
main()
