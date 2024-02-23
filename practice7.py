# Author: Vega Skelton
# Version: 1
# Sample Run:
# Hi! Enter a range of integers, and I'll calculate the average of all the
# numbers, print the highest and lowest of them, and tell you their sum and
# average!
# list_sum of the numbers!
# Enter your number: 4
# Continue? y
# Enter your number: 8
# Continue? y
# Enter your number: 12
# Continue? n
# The sum of these numbers is 24
# The average of these numbers is 8
# The lowest of these numbers is 4
# The highest of these numbers is 12
# Goodbye!

import valid as v


def main():
    """
    The main function of the program
    :return: nothing
    """
    cont = 'y'
    nums = []
    list_sum = 0
    avg = 0.0
    high = 0
    low = 0
    prompt = "Do you want to continue? (y/n) "
    greeting()
    while cont == 'y':
        nums = user_input(nums)
        cont = v.get_y_or_n(prompt)
    list_sum = list_sum_calc(nums)
    high = high_eval(nums)
    low = low_eval(nums)
    avg = avg_calc(nums)
    output(nums, list_sum, avg, high, low)


def greeting():
    """
    Outputs a greeting to the user, and an explanation of the program.
    :return: nothing
    """
    print("Hi! Enter a range of numbers, and I'll calculate the average of all"
          "the \nnumbers, print the highest and lowest of them, and tell you "
          "their sum and \naverage!")


def user_input(nums):
    """
    Gets user input of a series of numbers, one after the other; stores
    these in a float because the calculations are performed sequentially.
    :param nums: a list of numbers
    :return: usrNum, an int
    """
    nums.append(v.get_real())
    return nums


def list_sum_calc(a_list):
    """
    Calculates the list_sum of every value the user inputs.
    :param: a_list, any list of ints or floats
    :return: total_list_sum, a float, the list_sum of every item in the list
    """
    total_list_sum = 0.0
    for index in range(len(a_list)):
        total_list_sum = total_list_sum + a_list[index]
    return total_list_sum


def avg_calc(a_list):
    """
    Calculates the average of all user inputs
    :param: a_list, any list of ints or floats
    :return: avg, the average of the terms in a_list
    """
    average = 0.0
    avg_list_sum = list_sum_calc(a_list)
    average = avg_list_sum / len(a_list)
    return average


def high_eval(a_list):
    """
    Function to find the maximum value in a list
    :param: a_list, any list of ints or floats
    :return: the maximum value in the list
    """
    list_max = a_list[0]
    for index in a_list:
        if index > list_max:
            list_max = index
    return list_max


def low_eval(a_list):
    """
    Function to find the maximum value in a list
    :param: a_list, any list of ints or floats
    :return: the minimum value in the list
    """
    list_min = a_list[0]
    for index in a_list:
        if index < list_min:
            list_min = index
    return list_min


def output(a_list, list_sum, avg, high, low):
    """
    Prints the output of all the functions.
    :param a_list: any list of ints or floats
    :param list_sum: an int, the sum of the user inputs
    :param avg:, a float, the average of the user inputs
    :param high:, a float, the highest value of the user inputs
    :param low: a float, the lowest value of the user inputs
    :returns None
    """
    print("You entered", len(a_list), "numbers")
    print("The sum of these is", list_sum)
    print("The average of them is", avg)
    print("The lowest of these is", low)
    print("The highest of these is", high)
    print("Have a good day!")


if __name__ == "__main__":
    main()
