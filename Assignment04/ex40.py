class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        print(lyrics)


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def crazy_song(self):
        for line in self.lyrics:
            if line == "I don't want to get sued":
                print(line)
            else:
                print("Bob")

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

happy =             ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]
crazy = Song(happy)
crazy.sing_me_a_song()

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

crazy.crazy_song()
