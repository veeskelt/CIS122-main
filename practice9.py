import valid as v
class Restaurant:
    __name__ = ""
    __type__ = ""
    __price_range__ = ""
    __rating__ = 0

    def __init__(self, n, t, pr, r):
        self.__name__ = n
        self.__type__ = t
        self.__price_range__ = pr
        self.__rating__ = r

    def get_name(self):
        return self.__name__

    def get_type(self):
        return self.__type__

    def get_price_range(self):
        return self.__price_range__

    def get_rating(self):
        return self.__rating__

    def set_name(self, n):
        self.__name__ = n

    def set_type(self, t):
        self.__type__ = t

    def set_price_range(self, pr):
        self.__price_range__ = pr

    def set_rating(self, r):
        self.__rating__ = r


def main():
    # Create 2 restaurant objects
    # Change at least one of the fields
    # print objects after each update
    restaurant_1 = Restaurant("", "", "", 0)
    restaurant_2 = Restaurant("", "", "", 0)
    cont = 'Y'
    while cont == 'Y':
        get_restaurant_name()
        print(restaurant_1.get_name(), restaurant_1.get_type(),
              restaurant_1.get_price_range(), restaurant_1.get_rating())
        get_restaurant_type()
        print(restaurant_1.get_name(), restaurant_1.get_type(),
              restaurant_1.get_price_range(), restaurant_1.get_rating())
        get_restaurant_price_range()
        print(restaurant_1.get_name(), restaurant_1.get_type(),
              restaurant_1.get_price_range(), restaurant_1.get_rating())
        get_restaurant_rating()
        print(restaurant_1.get_name(), restaurant_1.get_type(),
              restaurant_1.get_price_range(), restaurant_1.get_rating())

