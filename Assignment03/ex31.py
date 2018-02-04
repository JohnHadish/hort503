print(""" You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity =="2":
        print("Your body survives powdered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

        print("Now that you have no eyes, do you want to try to get back to door 1?")
        door1 = input("Y/N > ")

        if door1 == "Y":
            print("You stumble around and find what you think is door 1")
            print("You enter and hear a smacking noise")
            print("1. Start smacking your own lips")
            print("2. Decide you are hungy and call a lyft to bring you home")
            bear1 = input("> ")

            if bear1 == "1":
                print("You feel something soft brush your face!")
                print("Looks like you made a bear friend!")
            elif bear1 == "2":
                print("You decide to use lyft becasue you disagree with Uber's")
                print("corprate structure. You know deep down that lyft is probs")
                print("the same. You bleed out your eyeballs a little as the lyft driver")
                print("brings you back to your apartment.  You turn on the news and")
                print("hear that the government has shut down. What a life, what a life")
            else:
                print("You get eaten by a bear for not following instructions.")
        elif door1 == "N":
            print("That's smart, you should probably try to find your way to a hospital.")
        else:
            print("yeah, I don't know what that means, I guess you probably are still insane")
else:
    print("You stumble around and fall on a knife and die. Good job!")
