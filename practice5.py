# Author: Vega Skelton
# Version: 1
# Sample Run:
# Hi! Enter a range of numbers, and I'll calculate the average of all the
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


def main():
    """The main function of the program
    returns: nothing"""
    cont = 'y'
    nums = 0.0
    sums = 0.0
    avg = 0.0
    high = 0.0
    low = 0
    count = 0
    greeting()
    while cont == 'y':
        nums = input_nums()
        sums, count = sum_calc(nums, sums, count)
        high = high_eval(nums, high, count)
        low = low_eval(nums, low, count)
        cont = proceed()
    avg = avg_calc(avg, sums, count)
    output(count, sums, avg, high, low)


def greeting():
    """Outputs a greeting to the user, and an explanation of the program.
    returns: nothing"""
    print("Hi! Enter a range of numbers, and I'll calculate the average of all"
          "the \nnumbers, print the highest and lowest of them, and tell you "
          "their sum and \naverage!")


def input_nums():
    """Gets user input of a series of numbers, one after the other; stores
    these in a float because the calculations are performed sequentially.
    returns: usrNum, a float"""
    nums = 0.0
    nums = float(input("Please enter a number: "))
    return nums


def proceed():
    """Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    returns: more, a char"""
    # cont = ""
    cont = input("Do you want to continue? (y/n) ")
    cont = cont.lower()
    if cont != 'y' and cont != 'n':
        print("This is not a valid input. Please try again.")
        cont = input("Do you want to continue? (y/n) ")
        cont = cont.lower()
    return cont


def sum_calc(nums, sums, count):
    """Calculates the sum of every value the user inputs.
    param: nums, a float
    returns: inpSum, a float, short for 'input sum'"""
    sums = sums + nums
    count = count + 1
    return sums, count


def avg_calc(avg, sums, count):
    """Calculates the average of all user inputs
    param: nums, a float
    param: count, an int
    returns: avg"""
    print("avg before: ", avg)
    avg = sums / count
    print("avg after: ", avg)
    return avg


def high_eval(nums, high, count):
    """Compares the current user input to the stored highest value
    param: nums, a float
    param: high, a float
    param: count, an int
    returns: high, a float"""
    if count == 1:
        high = nums
    elif high < nums:
        high = nums
    return high


def low_eval(nums, low, count):
    """Compares the current user input to the stored lowest value
    param: nums, a float
    returns: low, a float"""
    if count == 1:
        low = nums
    elif low > nums:
        low = nums
    return low


def output(count, sums, avg, high, low):
    """Prints the output of all the functions.
    param: count, an int
    param: sums, a float
    param: avg, a float
    param: high, a float
    param: low, a float
    returns: None"""
    print("You entered", count, "numbers.")
    print("The sum of these is", sums)
    print("The average of them is", avg)
    print("The lowest of these is", low)
    print("The highest of these is", high)
    print("Have a good day!")


if __name__ == "__main__":
    main()
