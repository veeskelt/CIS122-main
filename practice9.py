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
    restaurant_name = ""
    restaurant_type = ""
    restaurant_price = ""
    restaurant_rating = 0
    cont = 'Y'
    #while cont == 'Y':
    restaurant_name = get_restaurant_name()
    restaurant_1.set_name(restaurant_name)
    print(restaurant_1.get_name(), restaurant_1.get_type(),
          restaurant_1.get_price_range(), restaurant_1.get_rating())
    restaurant_type = get_restaurant_type()

    restaurant_1.set_type(restaurant_type)
    print(restaurant_1.get_name(), restaurant_1.get_type(),
          restaurant_1.get_price_range(), restaurant_1.get_rating())

    restaurant_price = get_restaurant_price()
    print(restaurant_1.get_name(), restaurant_1.get_type(),
          restaurant_1.get_price_range(), restaurant_1.get_rating())
    restaurant_rating = get_restaurant_rating()

    restaurant_1.set_rating(restaurant_rating)
    print(restaurant_1.get_name(), restaurant_1.get_type(),
          restaurant_1.get_price_range(), restaurant_1.get_rating())


def get_restaurant_name():
    restaurant_name = ""
    restaurant_name = v.get_string("Enter the name of the restaurant: ")
    return restaurant_name


def get_restaurant_type():
    restaurant_type = ""
    restaurant_type = v.get_string("Enter the type of restaurant: ")
    return restaurant_type


def get_restaurant_price():
    restaurant_price = ""
    restaurant_price = v.get_string("Enter the price of the restaurant: ")
    print(restaurant_price)
    while restaurant_price != "$" and restaurant_price != "$$" and restaurant_price != "$$$":
        print("Invalid input. Please try again.")
        restaurant_price = v.get_string("Enter the price of the restaurant: ")
    return restaurant_price


def get_restaurant_rating():
    restaurant_rating = 0
    restaurant_rating = v.get_integer("Enter the rating of the restaurant: ")
    while restaurant_rating > 5 or restaurant_rating < 0:
        print("Rating cannot be greater than 5 or less than 0.")
        restaurant_rating = v.get_string("Enter the rating of the restaurant: ")
    return restaurant_rating


main()
