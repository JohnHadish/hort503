## Animal is an object
class Animal(object):
    pass
    def aminal():
        print("Animal, Animal")

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        def bork():
            print("Bork, bork")
## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        ##Person has a pet of some kind
        self.pet = None
## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

##??
class Fish(object):
    def fih():
        print("I am agetated from these past two practice things")

##??
class Salmon(Fish):
    pass

##??
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

##??
satan = Cat("Satan")

##??
mary = Person("Mary")

##??
mary.pet = satan

##??
frank = Employee("Frank", 120000)

##??
frank.pet = rover

##??
flipper = Fish()

##??
crouse = Salmon()

##??
harry = Halibut()

print(frank)
