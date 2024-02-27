def find_maximum(a_list):
    """
    Function to find the maximum value in a list
    :param a_list: a list of values
    :return: the maximum value in the list
    """
    list_max = a_list[0]
    for index in range(len(a_list)):
        if type(a_list[index]) is int or type(a_list[index]) is float:
            if index > list_max:
                list_max = index
    return list_max


def find_max_index(a_list):
    """
    Function to find the index of the first occurrence of the maximum value
    :param a_list: a list of values
    :return: the index of the first occurrence of the maximum value
    """
    maximum = a_list[0]
    max_index = 0
    for index in range(len(a_list)):
        if type(a_list[index]) is int or type(a_list[index]) is float:
            if a_list[index] > maximum:
                max_index = index

    return max_index


def find_minimum(a_list):
    """
    Function to find the maximum value in a list
    :param a_list: a list of values
    :return: the minimum value in the list
    """
    list_min = a_list[0]
    for index in range(len(a_list)):
        if type(a_list[index]) is int or type(a_list[index]) is float:
            if index < list_min:
                list_min = index
    return list_min


def find_min_index(a_list):
    """
    Function to find the index of the first occurrence of the minimum value
    :param a_list: a list of values
    :return: the index of the first occurrence of the minimum value
    """
    list_min = a_list[0]
    min_index = 0
    for index in range(len(a_list)):
        if type(a_list[index]) is int or type(a_list[index]) is float:
            if a_list[index] < list_min:
                list_min = a_list[index]
                min_index = index

    return min_index


def value_count(a_list, value):
    """
    Finds and returns the number of occurrences of value in the list
    :param a_list: a list of values
    :param value: a value to search for in the list
    :return: integer, the number of occurrences of value found in the list
    """
    count = 0
    for item in a_list:
        if item == value:
            count = count + 1

    return count


def is_in_list(a_list, search_item):
    """
    Verifies the existence of a value in a list.
    :param a_list: a list of values
    :param search_item: the value to be checked for
    :return: a bool, the existence of the item in the list
    """
    in_list = False
    for index in range(len(a_list)):
        if a_list[index] == search_item:
            in_list = True
    return in_list


def print_list(a_list):
    """
    Prints the entire list in a user-readable format
    :param a_list: a list of values
    :return: nothing, decorative
    """
    for index in range(len(a_list)):
        print("Value at position", index, ":", a_list[index])


def calc_list_sum(a_list):
    """
    Sums the values in a list
    :param a_list: a list of values
    :return: sum of the values
    """
    total_sum = 0.0
    for index in range(len(a_list)):
        # we need to check if the items in the list are ints or floats
        if type(a_list[index]) is int or type(a_list[index]) is float:
            total_sum = total_sum + a_list[index]
    return total_sum


def calc_list_average(a_list):
    """
    Calculates the average of the items in a list
    :param a_list: a list of values
    :return: the average of the list items
    """
    average = 0.0
    avg_sum = calc_list_sum(a_list)
    average = avg_sum / len(a_list)
    return average


def main():
    a_list = [1, 2, 3, 4, 5, 6]

    # print_list(a_list)

    maximum_value = 0.0
    minimum_value = 0.0
    max_index = 0
    min_index = 0
    maximum_value = find_maximum(a_list)
    max_index = find_max_index(a_list)
    minimum_value = find_minimum(a_list)
    min_index = find_min_index(a_list)
    print("maximum of ", maximum_value, " at index", max_index)
    print("minimum of ", minimum_value, " at index", min_index)

    value = 0
    search_item = 4
    in_list = False
    value = value_count(a_list, search_item)
    in_list = is_in_list(a_list, search_item)
    in_list = is_in_list(a_list, search_item)
    if in_list is True:
        print(search_item, "is in list")
        print(search_item, "appears", value, "times")
    else:
        print(search_item, "is not in list")
    list_sum = 0
    list_average = 0
    list_sum = calc_list_sum(a_list)
    print("the sum of the list is", list_sum)
    list_average = calc_list_average(a_list)
    print("the average of the list is", list_average)


if __name__ == "__main__":
    main()
    exit(0)
