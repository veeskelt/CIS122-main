class Pet:
    __name__ = ""
    __type__ = ""
    __age__ = 0

    def __init__(self, n, t, a):
        self.__name__ = n
        self.__type__ = t
        self.__age__ = a

    def get_name(self):
        return self.__name__

    def get_type(self):
        return self.__type__

    def get_age(self):
        return self.__age__

    def set_name(self, n):
        self.__name__ = n

    def set_type(self, t):
        self.__type__ = t

    def set_age(self, a):
        self.__age__ = a


def main():
    # Create two Pet objects, my_pet and your_pet
    my_pet = Pet("Sam", "dog", 10)
    your_pet = Pet("Clifford", "cat", 3)

    # Write a statement to print my_pet name field
    print(Pet.get_name(my_pet))

    # Write a statement to change my_pet name to "Sammy"
    my_pet.set_name("Sammy")

    # Write a statement to print my_pet name field
    print(Pet.get_name(my_pet))

    # Write a statement to print your_pet age field
    print(Pet.get_age(my_pet))

    # Write a statement to change your_pet age to 17
    my_pet.set_age(17)

    # Write a statement to print all the your_pet
    # fields on one line
    print("My", Pet.get_type(my_pet), "is named", Pet.get_name(my_pet),
          "and is", Pet.get_age(my_pet), "years old.")


main()
