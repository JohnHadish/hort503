mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])


import myStuff
myStuff.apple()

print(myStuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

#dict style
mystuff['apple']

#module style
myStuff.apple()
print(myStuff.tangerine)

#class style
thing = MyStuff
thing.apple('self')
print(thing.tangerine)
