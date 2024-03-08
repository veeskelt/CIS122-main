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
    cont = 'y'
    top_choice = 0
    mid_choice = 0
    top_choice = menu_top()
    if top_choice == 1:
        mid_choice = 0
        while mid_choice != 6:
            if mid_choice == 0:
                mid_choice = menu_mid(top_choice)
            if mid_choice == 1:
                print(mid_choice)
                # Restaurant Name
                restaurant_name = get_restaurant_name()
                restaurant_1.set_name(restaurant_name)
                print_restaurant(restaurant_1)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 2:
                # Restaurant Type
                restaurant_type = get_restaurant_type()
                restaurant_1.set_type(restaurant_type)
                print_restaurant(restaurant_1)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 3:
                # Restaurant Price
                restaurant_price = get_restaurant_price()
                restaurant_1.set_price_range(restaurant_price)
                print_restaurant(restaurant_1)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 4:
                # Restaurant Rating
                restaurant_rating = get_restaurant_rating()
                restaurant_1.set_rating(restaurant_rating)
                print_restaurant(restaurant_1)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 5:
                # Print Restaurant
                print_restaurant(restaurant_1)
                mid_choice = menu_mid(top_choice)
            elif mid_choice == 6:
                mid_choice = 0
                top_choice = menu_top()

    elif top_choice == 2:
        mid_choice = 0
        while mid_choice != 6:
            if mid_choice == 0:
                mid_choice = menu_mid(top_choice)
            if mid_choice == 1:
                print(mid_choice)
                # Restaurant Name
                restaurant_name = get_restaurant_name()
                restaurant_2.set_name(restaurant_name)
                print_restaurant(restaurant_2)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 2:
                # Restaurant Type
                restaurant_type = get_restaurant_type()
                restaurant_2.set_type(restaurant_type)
                print_restaurant(restaurant_2)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 3:
                # Restaurant Price
                restaurant_price = get_restaurant_price()
                restaurant_2.set_price_range(restaurant_price)
                print_restaurant(restaurant_2)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 4:
                # Restaurant Rating
                restaurant_rating = get_restaurant_rating()
                restaurant_2.set_rating(restaurant_rating)
                print_restaurant(restaurant_2)
                mid_choice = menu_mid(top_choice)

            elif mid_choice == 5:
                # Print Restaurant
                print_restaurant(restaurant_2)
                mid_choice = menu_mid(top_choice)
            elif mid_choice == 6:
                mid_choice = 0
                top_choice = menu_top()


def menu_top():
    choice_start = 0
    print("Welcome to the restaurant database (kinda)! \n Please make your selection:")
    print("1. Modify restaurant 1")
    print("2. Modify restaurant 2")
    print("3. Exit")
    choice_start = v.get_integer("\nEnter your choice (1, 2, or 3): ")
    while choice_start != 1 and choice_start != 2 and choice_start != 3:
        print("invalid choice.")
        choice = v.get_integer("\nEnter your choice (1, 2, or 3): ")
    if choice_start == 3:
        print("Thank you for using this program!")
        exit(0)
    else:
        return choice_start


def menu_mid(choice_top):
    choice_mid = 0
#    print("\n", choice_mid)
    print("What do you want to do with restaurant ", choice_top, "?", sep="")
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


def print_restaurant(restaurant):
    print("\n{: <20}{: <20}{: <10}{: <5}".
          format('Name', "Type", "Pricing", "Rating"))
    print("{: <20}{: <20}{: <10}{: <5}"
          .format(restaurant.get_name(), restaurant.get_type(),
                  restaurant.get_price_range(), restaurant.get_rating()))


def get_restaurant_name():
    restaurant_name = ""
    restaurant_name = v.get_string("\nEnter the name of the restaurant: ")
    return restaurant_name


def get_restaurant_type():
    restaurant_type = ""
    restaurant_type = v.get_string("\nEnter the type of restaurant: ")
    return restaurant_type


def get_restaurant_price():
    restaurant_price = ""
    restaurant_price = v.get_string("\nEnter the price of the restaurant: ")
    print(restaurant_price)
    while restaurant_price != "$" and restaurant_price != "$$" and restaurant_price != "$$$":
        print("Invalid input. Please try again.")
        restaurant_price = v.get_string("Enter the price of the restaurant: ")
    return restaurant_price


def get_restaurant_rating():
    restaurant_rating = 0
    restaurant_rating = v.get_integer("\nEnter the rating of the restaurant: ")
    while restaurant_rating > 5 or restaurant_rating < 0:
        print("Rating cannot be greater than 5 or less than 0.")
        restaurant_rating = v.get_string("Enter the rating of the restaurant: ")
    return restaurant_rating


main()
