#This is my function called cheese_and_crackers
#it asks how much cheese and crackers and then tells you you have enough
#for a party!
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#This calls the function with variables 20 cheese_count and 50 boxes_of_crackers
print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#This calls the function using variables for each
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This plays with math to call the function
print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#This uses variables and math!
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def cheese_monster(cheese_count):
    print("Oh no! A cheese monster is attacking the party")
    print(f"Xe ate {cheese_count / 2} of your {cheese_count} cheeses!")
    print("I hope that is still enough for a party!\n")

cheese_monster(100)

cheese_monster(amount_of_cheese)

cheese_monster(66%5)

cheese_monster(100 + amount_of_cheese)

cheese_monster(amount_of_cheese * 8)

cheese_monster(amount_of_cheese - 99)

cheese_monster(0)

cheese_in = int(input("How much cheese is left at the party? > "))
cheese_monster(cheese_in)

cheese_count = 10
cheese_monster(cheese_count)

cheese_monster(100000000000)
