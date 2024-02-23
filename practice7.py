# Author: Vega Skelton
# Version: 1
# Sample Run:
# Hi! Enter a range of integers, and I'll calculate the average of all the
# numbers, print the highest and lowest of them, and tell you their sum and
# average!
# sum of the numbers!
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
    """The main function of the program
    returns: nothing"""
    cont = 'y'
    nums = []
    sums = 0
    avg = 0.0
    high = 0
    low = 0
    count = 0
    greeting()
#    print(type(nums))
    while cont == 'y':
        nums = input_nums(nums)
        cont = proceed()
    print(nums)
    sums = sum_calc(nums)
#    print(sums)
    high = high_eval(nums)
    low = low_eval(nums)
    avg = avg_calc(nums)
    output(count, sums, avg, high, low)


def greeting():
    """Outputs a greeting to the user, and an explanation of the program.
    returns: nothing"""
    print("Hi! Enter a range of numbers, and I'll calculate the average of all"
          "the \nnumbers, print the highest and lowest of them, and tell you "
          "their sum and \naverage!")


def input_nums(nums):
    """Gets user input of a series of numbers, one after the other; stores
    these in a float because the calculations are performed sequentially.
    returns: usrNum, an int"""
    nums.append(v.get_real())
    return nums


def proceed():
    """Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    returns: more, a char"""
    # cont = ""
    cont = input("Do you want to continue? (y/n) ")
    cont = cont.lower()
    # The following checks to make sure the input was a valid input
    if cont != 'y' and cont != 'n':
        print("This is not a valid input. Please try again.")
        cont = input("Do you want to continue? (y/n) ")
        cont = cont.lower()
    return cont


def sum_calc(a_list):
    """
    Calculates the sum of every value the user inputs.
    param: a_list, any list of ints or floats
    returns: total_sums, a float, the sum of every item in the list
    """
    total_sum = 0.0
    for index in range(len(a_list)):
        total_sum = total_sum + a_list[index]
    return total_sum


def avg_calc(a_list):
    """Calculates the average of all user inputs
    param: nums, an int, the current user input
    param: count, an int, keeps track of how many values have been input
    returns: avg"""
    average = 0.0
    avg_sum = sum_calc(a_list)
    average = avg_sum / len(a_list)
    return average


def high_eval(a_list):
    """
    Function to find the maximum value in a list
    :param a_list: a list of values
    :return: the maximum value in the list
    """
    list_max = a_list[0]
    for index in range(len(a_list)):
        if index > list_max:
            list_max = index
    return list_max


def low_eval(a_list):
    """
    Function to find the maximum value in a list
    :param a_list: a list of values
    :return: the minimum value in the list
    """
    list_min = a_list[0]
    for index in range(len(a_list)):
        if index < list_min:
            list_min = index
    return list_min


def output(count, sums, avg, high, low):
    """Prints the output of all the functions.
    param: count, an int, keeps track of how many times the loop was run
    param: sums, an int, the sum of the user inputs
    param: avg, an int, the average of the user inputs
    param: high, an int, the highest value of the user inputs
    param: low, an int, the lowest value of the user inputs
    returns: None"""
    print("You entered", count, "numbers.")
    print("The sum of these is", sums)
    print("The average of them is", avg)
    print("The lowest of these is", low)
    print("The highest of these is", high)
    print("Have a good day!")


if __name__ == "__main__":
    main()
