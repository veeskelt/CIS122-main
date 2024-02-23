import valid as v


DAYS = 7


def main():
    # rocks = 0
    rocks_list = []
    total_rocks = 0

    get_rocks(rocks_list)
    total_rocks = calc_total_rocks(rocks_list)

    print("\nYou collected", format(total_rocks, ".0f"), "rocks this week!")


def get_rocks(rock_list):
    """
    This function gets the number of rocks collected each day from the user.
    :param rock_list: a list of integers
    :return: nothing, since lists are updated globally
    """
    for i in range(DAYS):
        rocks = v.get_real("Enter number of rocks collected on day " + str(i+1)
                           + ": ")
        if rocks < 0:
            print("Invalid input. Please enter a positive integer.")
            rocks = v.get_real("Enter number of rocks collected on day " + str(i + 1)
                               + ": ")
        rock_list.append(rocks)


def calc_total_rocks(rock_list):
    """
    This function calculates the total rocks collected each day from the user
    :param rock_list: a list of integers
    :return: total, an int, the sum of the rocks collected
    """
    total = 0
    for i in range(DAYS):
        total = total + rock_list[i]
        # print(total_rocks)
    return total


main()
