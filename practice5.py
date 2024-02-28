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


def main():
    """The main function of the program
    returns: nothing"""
    cont = 'y'
    nums = 0
    sums = 0
    avg = 0.0
    high = 0
    low = 0
    count = 0
    greeting()
    while cont == 'y':
        nums = input_nums()
        sums, count = sum_calc(nums, sums, count)
        high = high_eval(nums, high, count)
        low = low_eval(nums, low, count)
        cont = proceed()
    # this has to go after the while loop, otherwise we'd continuously call
    # the function and divide sums by count, which does not result in
    # accurate results. learned this the hard way.
    avg = avg_calc(sums, count)
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
    returns: usrNum, an int"""
    nums = 0
    nums = int(input("Please enter a number: "))
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


def sum_calc(nums, sums, count):
    """Calculates the sum of every value the user inputs. This is a running
        total.
    param: nums, an int, the current user input
    param: sums, an int, the sum of every user input before this function
        is called
    param: count, an int, keeps track of how many values have been input
    returns: sums, an int, the sum of every user input"""
    sums = sums + nums
    count = count + 1  # increment our count variable by 1
    return sums, count


def avg_calc(sums, count):
    """Calculates the average of all user inputs
    param: nums, an int, the current user input
    param: count, an int, keeps track of how many values have been input
    returns: avg"""
    # we set avg to 0.0 here to ensure it's not influenced by anything else.
    avg = 0.0
    avg = sums / count
    return avg


def high_eval(nums, high, count):
    """Compares the current user input to the stored highest value
    param: nums, an int, the current user input
    param: high, an int, the current highest value (will be set to the user
        input if count is 1, otherwise performs the comparison
    param: count, an int, keeps track of how many values have been input
    returns: high, a float"""
    # we need to ensure high is set equal to nums if it's the first input from
    # the user, otherwise we perform the comparison.
    if count == 1:
        high = nums
    elif high < nums:
        high = nums
    return high


def low_eval(nums, low, count):
    """Compares the current user input to the stored lowest value
    param: nums, an int, the current user input
    param: low, an int, the current lowest input so far
    param: count, an int, keeps track of how many values have been input
    returns: low, an int, the lowest user input so far"""
    # we need to ensure low is set equal to nums if it's the first input from
    # the user, otherwise we perform the comparison.
    if count == 1:
        low = nums
    elif low > nums:
        low = nums
    return low


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