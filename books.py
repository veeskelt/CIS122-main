class Book:
    __title__ = ""
    __author__ = ""
    __publisher__ = ""
    __copies_sold__ = 0

    def __init__(self, t, a, p, c):
        self.__title__ = t
        self.__author__ = a
        self.__publisher__ = p
        self.__copies_sold__ = c

    def get_title(self):
        return self.__title__

    def get_author(self):
        return self.__author__

    def get_publisher(self):
        return self.__publisher__

    def get_copies_sold(self):
        return self.__copies_sold__

    def set_title(self, t):
        self.__title__ = t

    def set_author(self, a):
        self.__author__ = a

    def set_publisher(self, p):
        self.__publisher__ = p

    def set_copies_sold(self, c):
        self.__copies_sold__ = c


# End Module
def main():
    my_book = Book("ABC", "Dr. Suess", "Harper", 10000)

    print(my_book.get_author(), my_book.get_author(), my_book.get_publisher(),
          my_book.get_copies_sold())


main()
