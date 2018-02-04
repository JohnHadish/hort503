from sys import exit
from random import randint
from textwrap import dedent



class Scene():

    def enter(self):
        pass

            #if user_input

#my engine is going to be where everything is given to. It will receive info from the fifferent classes, and will send
#info to Map
class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.openingScene()

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.nextScene(next_scene_name)

#These are all "scenes"
class Death(Scene):
    quips = ["Death is but an illusion, but a very convincing one for you",
             "Your papi cries and your mother wails at your death",
             "At least you were not the best commander or something. You are dead now",
             "Whats that? you wanted to live? Shouldn't have done that then!",
             "YOU ARE DEAD"
             ]

    def enter(self):
        print(Death.quips[randint(0, len(Death.quips)-1)])
        exit(1)

class Central_Corridor(Scene):


    def enter(self):
        print(dedent("""
              You stand aboard the Starship Enterprise as a namesless Red Shirt
              This looks like it might be a rough day:

              Music: Daa, Da Daaa, Da Da Da Da Daaaaa

              Uhura : "Incoming video message sir"
              Kirk : "Put it on the screen"

              Gothon : "BNlarg NArG Snarg Nard!"

              Spock : "He is saying that they are going to board us. Logically
              this makes no sense"
              """))
        input("> ")
        print(dedent("""
              You hear a loud crash

              After everyone is done fake falling against a control panel, Captain
              Kirk points at you.

              Kirk: "You there, go see what that was.""

              You obey, and walk into the central corredor

              There you find a medium size Gothon gnahing on the dismembered remains
              of one of your comrads. What do you do?
              """))
        action = input("> ")


        if action == "Random":
            randlist = ["Phaser stun", 'walk North', 'Pray']
            action = randlist[randint(0, len(randlist)-1)]
            print(action)
        else:
            pass

        if action == "Phaser stun":
            print(dedent("No offrnse, but you should know stun never really works"))
            return('death')

        elif action == "walk North":
            print("There is no North in space. You get eaten alive")
            return('death')
        elif action == 'Pray':
            print("To what God?")
            God = input("> ")
            if God == 'Satan':
                print("Kind of messed up, but I guess we should have expected red shirts to be a little messed up")
                return('death')
            else:
                print("There is no God")
                return('death')
        elif action == 'Kill':
            print("Aight, you do some dope karate")
            return("laser_weapon_armory")
        else:
            print("You can type 'Random' if you don't know what to do")
            return('central_corridor')

class Laser_Weapon_Armory(Scene):

    def enter(self):
        print(dedent("""
                    You realize you are really underapreciated on this ship. You decide to blow it up
                    To blow it up you will need a bomb. Guess the code for the armory to get a bomb. The pass
                    code is only 2 numbers long because they never anticipated someone snapping like you just did.
                    It will lock permanintly if you do not get it in 10 guesses.
                    """))

        pass_code = (f"{randint(0,9)}{randint(0,9)}")
        how_many_times = 0
        while how_many_times < 9:
            x = input("[codebox] > ")
            if x == pass_code:
                print("Computer : 'Wow, you actually gussed it!'")
                print("K, you have a weapon now. It goes boom")
            else:
                print("Computer : 'Nope!'")
                times = 10 - how_many_times
                print(f"Computer : 'You only have {9 - how_many_times} left to guess the code'")
                how_many_times += 1
        print(f"\nComputer : '...The passcode is {pass_code} if you need to know'")
        x = input("[codebox] > ")
        if x == pass_code:
            print("Computer : Click")
            print("K, you have a weapon now. It goes boom")
            return('the_bridge')
        else:
            print("Computer : 'You are an idiot'")
            return('death')

class The_Bridge(Scene):

    def enter(self):
        input("> ")
        print(dedent("""
                     You stumble in a haze into the hallway holding the bomb.
                     You can't believe you are finally doing it.
                     You are going to destroy this terrible irrational ship.
                     You are going to purge this menace that has destroyed so many
                     lives under the thin guise of "Going where no man has gone before!"

                     You find your self trip over the threshold of the bridge.

                     You should probably set the bomb in here to blow up the Enterprise

                     Everyone is looking at you and can see that you are holding a bomb.

                     What do you say to evade their suspission?
                     """))

        action = input("> ")
        if action == "I am death":
            print("Kirk : 'Carry on Yeoman'")
            print("You are not actually a yeoman, but you are not going to tell Kirk that")
            return 'escape_pod'
        else:
            print("Kirk : 'No you are not, to the brig with you!'")
            return 'death'


class Escape_Pod(Scene):

    def enter(self):
        print(dedent("""
                     You set the bomb and get out of dodge. You have set it for 2 minutes.
                     The pain is almost over now.

                     You come to the Escape pods. Do you leave the Enterprise or stay for the
                     fireworks?
                     """))
        action = input("> ")
        if action == "Leave":
            print("You watch the Enterprise blink out of existance as you fly into space")
            exit(1)
        elif action == "Stay":
            print("You cry tears of joy as your prison goes up in flames around you")
            print("Good job")
            exit(1)
        else:
            return 'death'

#This is where I will record which directions a player can go
class Map():
    scenes = {'death' : Death(),
              'central_corridor' : Central_Corridor(),
              'laser_weapon_armory' : Laser_Weapon_Armory(),
              'the_bridge' : The_Bridge(),
              'escape_pod' : Escape_Pod(),
              }

    def __init__(self, start_scene):
        self.start_scene =  start_scene

    #I want this to pull out the proper scene from the library scene and "play" that scene.
    def nextScene(self, next_scene):
        play_me = Map.scenes[next_scene]
        return(play_me)

    def openingScene(self):
        play_me = Map.scenes[self.start_scene]
        return(play_me)

a_map = Map('central_corridor')
#a_map = Map('death')
a_game = Engine(a_map)
a_game.play()
