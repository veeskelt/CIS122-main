import valid as v


# Add Song class definition below
class Song:
    __title = ""
    __artist = ""
    __duration = 0.0

    def __init__(self, title, artist, duration):
        self.__title__ = title
        self.__artist__ = artist
        self.__duration__ = duration
        print("Song created!")

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_duration(self):
        return self.__duration

    def set_title(self, t):
        self.__title = t

    def set_artist(self, a):
        self.__artist = a

    def set_duration(self, d):
        self.__duration = d

    def __str__(self):
        printed_string = f"Title: {self.__title}, Artist: {self.__artist}, Duration: {self.__duration}"
        return printed_string


QUIT = 3


def main():
    songs = []
    choice = 0

    print("Welcome to the Song library!")

    while choice != QUIT:
        print_menu()
        choice = get_choice()
        if choice == 1:
            add_song(songs)
        elif choice == 2:
            list_songs(songs)

    print("\nGoodbye!")


def print_menu():
    print("\n1. Add Song")
    print("2. List Songs")
    print("3. Quit\n")


def get_choice():
    choice = 0
    choice = v.get_integer("Please enter your choice: ")
    while choice < 1 or choice > 3:
        print("Invalid choice.")
        choice = v.get_integer("Please enter your choice: ")
    return choice


def add_song(songs):
    title = ""
    artist = ""
    duration = 0.0

    title = v.get_string("Enter title: ")
    artist = v.get_string("Enter artist: ")
    duration = v.get_real("Enter duration (mm.ss): ")
    songs.append(Song(title, artist, duration))


def list_songs(songs):
    print("\nList of songs:\n")
    print("{: <20} {: <20} {: <20}".format("Title",
                                           "Artist",
                                           "Duration (mm.ss)"))
    print("{: <20} {: <20} {: <20}".format("-----",
                                           "------",
                                           "----------------"))
    for i in range(len(songs)):
        print("{: <20} {: <20} {: <20.2f}".format(songs[i].get_title(),
                                                  songs[i].get_artist(),
                                                  songs[i].get_duration()))


main()
