# Enter song title: Sp Harlm
# Enter song artist: Aretha
# Enter Song Duration: 3.33
#
# Title                Artist           Duration (mm.ss)
# _____                ______           ________________
# Sp Harlm             Aretha           3.33
#
# Enter a new song title: Spanish Harlem
#
# Title                Artist           Duration (mm.ss)
# _____                ______           ________________
# Spanish Harlem       Aretha           3.33
#
# Enter a new song artist: Aretha Franklin
#
# Title                Artist           Duration (mm.ss)
# _____                ______           ________________
# Spanish Harlem       Aretha Franklin  3.33
#
# Goodbye!

import valid as v


class Song:
    __title__ = ""
    __artist__ = ""
    __duration = 0.0

    def __init__(self, t, a, d):
        self.__title__ = t
        self.__artist__ = a
        self.__duration__ = d

    def get_title(self):
        return self.__title__

    def get_artist(self):
        return self.__artist__

    def get_duration(self):
        return self.__duration__

    def set_title(self, t):
        self.__title__ = t

    def set_artist(self, a):
        self.__artist__ = a

    def set_duration(self, d):
        self.__duration__ = d


def main():
    title = ""
    artist = ""
    duration = 0.0

    title = v.get_string("Enter song title: ")
    artist = v.get_string("Enter song artist: ")
    duration = get_duration()

    song = Song(title, artist, duration)
    print_song(song)

    title = v.get_string("\nEnter a new song title: ")
    song.set_title(title)
    print_song(song)

    artist = v.get_string("\nEnter a new song artist: ")
    song.set_artist(artist)
    print_song(song)

    duration = get_duration()
    song.set_duration(duration)
    print_song(song)


def get_duration():
    dur = 0.0
    dur = v.get_real("\nEnter song duration: ")
    while dur < 0:
        print("Must be positive.")
        dur = v.get_real("Enter song duration: ")
    return dur


def print_song(song):
    print("\n{: <20}{: <20}{: <20}".format("Title",
                                           "Artist",
                                           "Duration (mm.ss)"))

    print("{: <20}{: <20}{: <20}".format("_____",
                                         "______",
                                         "________________"))

    print("{: <20}{: <20}{: <20.2f}".format(song.get_title(),
                                            song.get_artist(),
                                            song.get_duration()))


main()
