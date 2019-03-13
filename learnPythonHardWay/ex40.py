class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy bday to you",
                    "blah",
                    "blah blah blah"])

dg = Song(["Ip dip doo",
            "doggy did a..."])

happy_bday.sing_me_a_song()
dg.sing_me_a_song()
