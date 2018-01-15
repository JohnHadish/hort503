#Setting up carpool variables
#How many cars avalible for the carpool (all are 2002 ford taurus)
cars = 100

#Space in each of the ford taurii
space_in_a_car = 4

#Number of taurus drivers
drivers = 30

#Number of taurus passemgers
passengers = 90

#Calculate information about todays carpool from above inputs
#Cars not used today due to lack of drivers
cars_not_driven = cars - drivers

#We can only use as many cars as there are drivers
cars_driven = drivers

#How many passendgers we can take in the carpool
carpool_capacity = cars_driven * space_in_a_car

#How many passengers will need to be in each car
average_passengers_per_car = passengers / cars_driven


# This reports the information we generate above
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
