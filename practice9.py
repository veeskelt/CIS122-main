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
    """
    The main function of the program
    :return: none
    """
    # Create 2 restaurant objects
    # Change at least one of the fields
    # print objects after each update
    restaurant_1 = Restaurant("", "", "", 0)
    restaurant_2 = Restaurant("", "", "", 0)

    cont = 'y'
    top_choice = 0
    mid_choice = 0
    print("Welcome to the restaurant database (kinda)!")
    top_choice = menu_top()
    while top_choice != 4:
        if top_choice == 1:
            change_attributes(restaurant_1, top_choice)
            top_choice = menu_top()
        elif top_choice == 2:
            change_attributes(restaurant_2, top_choice)
            top_choice = menu_top()
        else:
            print_both_restaurants(restaurant_1, restaurant_2)
            top_choice = menu_top()
    print("Thanks for using this program!")


def menu_top():
    """
    This function prints a top-level menu that allows the user to choose which
    restaurant is being manipulated.
    :return choice_start: int, the top level menu selection from the user.
    """
    choice_start = 0
    print("\nPlease make your selection: "
          "\n1. Modify restaurant 1 \n2. Modify restaurant 2 "
          "\n3. Print both \n3. Exit ")
    choice_start = v.get_integer("\nEnter your choice (1, 2, 3, or 4): ")
    while choice_start < 0 or choice_start > 4:
        print("invalid choice.")
        choice = v.get_integer("\nEnter your choice (1, 2, 3 or 4): ")
    else:
        return choice_start


def menu_mid(choice_top):
    """
    This function prints a middle menu that allows the user to choose which
    attribute of the selected menu is being manipulated, or to print the entire
    restaurant, or exit the loop.
    :param choice_top: the  menu selection of the user from the top menu, only
    passed so the user knows which restaurant they're manipulating.
    :return choice_mid: int, the mid menu selection from the user.
    """
    choice_mid = 0
    #    print("\n", choice_mid)
    print("\nWhat do you want to do with restaurant ", choice_top, "?", sep="")
    print("1. Modify Name \n2. Modify Type \n3. Modify Price \n"
          "4. Modify Rating \n5. Print Restaurant \n6. Exit")
    choice_mid = v.get_integer("Enter your selection: ")
    #    print("\n", choice_mid)
    while choice_mid <= 0 or choice_mid > 6:
        print("Invalid choice.")
        print("What do you want to do with restaurant", choice_top, "?")
        print("1. Modify Name \n2. Modify Type \n3. Modify Price \n"
              "4. Modify Rating \n5. Print Restaurant \n6. Exit")
        choice_mid = v.get_integer("Enter your selection: ")
    #        print("\n", choice_mid)
    else:
        return choice_mid


def change_attributes(restaurant, top):
    """
    This function contains the code for manipulating the restaurant passed to
    it. It is self-contained for cleanliness purposes.
    :param restaurant: a restaurant object, matches the menu option from
    menu_top
    :param top: the selection from menu_top, so it can be passed it to
    mid_choice
    :return: none
    """
    # This function exists because I wanted to clean up main() while i was
    # debugging how the menu functions played with each other- it used to be
    # that going to modify another object after the first ended the program
    # because I wasn't clearing mid_choice, so it stored persisted, immediately
    # ended this loop, and because the loop of the top menu wasn't properly
    # written it "reached the end". I moved one half of the loop down here and
    # saw how to fix it instantly, then discovered that this was cleaner.
    # (The fix was not having the exit condition inside top_menu and instead in
    # main.)

    restaurant_name = ""
    restaurant_type = ""
    restaurant_price = ""
    restaurant_rating = 0
    mid_choice = 0
    mid_choice = menu_mid(top)
    while mid_choice != 6:
        if mid_choice == 0:
            mid_choice = menu_mid(top)

        elif mid_choice == 1:
            mid_choice = 0
            restaurant_name = get_restaurant_name()
            restaurant.set_name(restaurant_name)
            print_restaurant(restaurant)

        elif mid_choice == 2:
            mid_choice = 0
            restaurant_type = get_restaurant_type()
            restaurant.set_type(restaurant_type)
            print_restaurant(restaurant)

        elif mid_choice == 3:
            mid_choice = 0
            restaurant_price = get_restaurant_price()
            restaurant.set_price_range(restaurant_price)
            print_restaurant(restaurant)

        elif mid_choice == 4:
            mid_choice = 0
            restaurant_rating = get_restaurant_rating()
            restaurant.set_rating(restaurant_rating)
            print_restaurant(restaurant)

        elif mid_choice == 5:
            mid_choice = 0
            print_restaurant(restaurant)


def print_restaurant(restaurant):
    """
    This function restaurants prints the passed restaurant object in a
    user-friendly way
    :param restaurant: The passed restaurant object
    :return: none
    """
    print("\n{: <20}{: <20}{: <10}{: <5}".
          format('Name', "Type", "Pricing", "Rating"))
    print("{: <20}{: <20}{: <10}{: <5}"
          .format(restaurant.get_name(), restaurant.get_type(),
                  restaurant.get_price_range(), restaurant.get_rating()))


def print_both_restaurants(restaurant_1, restaurant_2):
    """
    This function prints both restaurant objects.
    :param restaurant_1: The first restaurant object
    :param restaurant_2: The first restaurant object
    :return: none
    """
    print("\n{: <20}{: <20}{: <10}{: <5}".
          format('Name', "Type", "Pricing", "Rating"))
    print("{: <20}{: <20}{: <10}{: <5}"
          .format(restaurant_1.get_name(), restaurant_1.get_type(),
                  restaurant_1.get_price_range(), restaurant_1.get_rating()))
    print("{: <20}{: <20}{: <10}{: <5}"
          .format(restaurant_2.get_name(), restaurant_2.get_type(),
                  restaurant_2.get_price_range(), restaurant_2.get_rating()))


def get_restaurant_name():
    """
    This function gets the name of the restaurant to be assigned to the object
    :return: none
    """
    restaurant_name = ""
    restaurant_name = v.get_string("\nEnter the name of the restaurant: ")
    return restaurant_name


def get_restaurant_type():
    """
    This function gets the type of the restaurant to be assigned to the object
    :return: none
    """
    restaurant_type = ""
    restaurant_type = v.get_string("\nEnter the type of restaurant: ")
    return restaurant_type


def get_restaurant_price():
    """
    This function gets the price of the restaurant to be assigned to the object
    :return: none
    """
    restaurant_price = ""
    restaurant_price = v.get_string("\nEnter the price of the restaurant: ")
    print(restaurant_price)
    while restaurant_price != "$" and restaurant_price != "$$" and restaurant_price != "$$$":
        print("Invalid input. Please try again.")
        restaurant_price = v.get_string("Enter the price of the restaurant: ")
    return restaurant_price


def get_restaurant_rating():
    """
    This function gets the rating of the restaurant to be assigned to the
    object
    :return: none
    """
    restaurant_rating = 0
    restaurant_rating = v.get_integer("\nEnter the rating of the restaurant: ")
    while restaurant_rating > 5 or restaurant_rating < 0:
        print("Rating cannot be greater than 5 or less than 0.")
        restaurant_rating = v.get_string("Enter the rating of the restaurant: ")
    return restaurant_rating


if __name__ == "__main__":
    main()
