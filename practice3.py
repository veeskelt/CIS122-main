# Author: Vega Skelton
# Sample Run:

# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!

# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10

# The jar will hold 477 gumballs!

# Goodbye!

import math
GUMBALL_VOLUME = 0.5236 # a gumball with a 1" diameter
PERCENT_SOLID = 0.65    # the percent of the container that's filled

def main():
    """
    Main function
    :return: nothing
    """
    welcome_message()
    dia = float(input_diameter())  # converting these to float for safety
    height = float(input_height())  # better safe than sorry
    gumballs = gumball_calc(dia, height)
    output_message(gumballs)


def gumball_calc(dia, height):
    """
    Calculates the number of gumballs that can fit in a given cylinder
    :param dia: the diameter of the container
    :param height: the height of the container
    :return: num_gumballs, the number of gumballs that'll fit in the container.
    """
    gumball_volume = 0.5236  # gumball with 1" diameter
    percent_solid = .65  # percentage of cylinder that will contain solids
    # to account for space between gumballs
    # PI = 3.14159265
    rad = dia / 2.0
    # Calculate the volume of cylinder = πr^2h
    # Multiply cylinder volume by 65% to account for empty space
    # between gumballs
    cylinder_volume = (math.pi * rad ** 2 * height) * PERCENT_SOLID
    # Calculate the number of gumballs and then truncate the decimal
    # portion - we want the whole number of gumballs
    num_gumballs = int(cylinder_volume / GUMBALL_VOLUME)
    return num_gumballs


def welcome_message():
    """
    Prints a simple welcome message to the user
    :return: nothing
    """
    print("Gumball Estimator!")
    print('Enter the dimensions of a cylinder jar and I will')
    print('tell you how many 1" gumballs it will take to fill!\n')


def input_diameter():
    """
    Gets user input for diameter
    :return: diameter
    """
    diameter = float(input("Enter cylinder diameter (in): "))
    return diameter


def input_height():
    """
    Gets user input for diameter
    :return: height
    """
    height = float(input("Enter cylinder height (in): "))
    return height


def output_message(ball_amt):
    """
    Prints the output message
    :param ball_amt:
    :return: none
    """
    print("\nThe jar will hold", ball_amt, "gumballs!")
    print("\nGoodbye!")


main()
