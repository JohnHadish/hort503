numbers = []

def loop(i, less_than, by_adding):
    while i < less_than:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + by_adding
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

loop(0, 10, 2)

print("The numbers: ")

for num in numbers:
    print(num)

#This is number two, question
i = 0
the_count = []

for number in range(0,7):
    print(f"At the top i is {number}")
    the_count.append(number)

    print("Number now: ", the_count)
    print(f"At the bottom i is {number}")
