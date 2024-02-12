# Author: Vega Skelton
# Version: 2
# Sample Run:

# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!

# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10

# The jar will hold 477 gumballs!

# Goodbye!

import math
GUMBALL_VOLUME = 0.5236  # a gumball with a 1" diameter
PERCENT_SOLID = 0.65  # the percent of the container that's filled
PI = math.pi  # the value of pi, gathered from the math library.


def main():
    """
    Main function
    :return: nothing
    """
    # initialize our variables
    dia = 0.0
    rad = 0.0
    height = 0.0
    volume = 0.0
    gumballs = 0

    welcome_message()

    dia = float(input_diameter())  # converting these to float for safety
    height = float(input_height())  # better safe than sorry
    # Calculate the radius, then volume of the cylinder
    rad = float(calc_radius(dia))
    volume = cylinder_volume(PI, rad, height)
    usable = calc_usable_volume(PERCENT_SOLID, volume)
    gumballs = gumball_calc(GUMBALL_VOLUME, usable)
    output_message(gumballs)


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
    diameter = 0.0
    diameter = float(input("Enter cylinder diameter (in): "))
    return diameter


def input_height():
    """
    Gets user input for diameter
    :return: height
    """
    height = 0.0
    height = float(input("Enter cylinder height (in): "))
    return height


def calc_radius(dia):
    """
    Calculates the radius given diameter.
    :param dia: a float, the diameter of the cylinder or circle
    :return: rad, a float, the radius of the cylinder or circle
    """
    rad = 0.0
    rad = dia / 2
    return rad


def cylinder_volume(PI, rad, height):
    """
    Calculates the volume of the cylinder given its diameter and height.
    :param PI: the value of PI as a constant float
    :param rad: a float, the radius of the container
    :param height: a float, the height of the container
    :return: cylinder_volume, a float the volume of the cylinder
    """
    cyl_volume = 0.0
    cyl_volume = (PI * rad ** 2 * height)
    return cyl_volume


def calc_usable_volume(PERCENT_SOLID, cyl_volume):
    """
    Calculates the usable volume of a cylinder, since most objects aren't solid
    and won't fill 100% of the space in a cylinder.
    :param PERCENT_SOLID: a constant float, the percentage of the cylinder in
    decimal form that you can expect to be occupied with something.
    :param cyl_volume: a float, the volume of the cylinder
    :return: usable_volume, a float, the usable volume of the cylinder
    """
    usable_volume = 0.0
    usable_volume = cyl_volume * PERCENT_SOLID
    return usable_volume


def gumball_calc(GUMBALL_VOLUME, usable_volume):
    """
    Calculates the number of gumballs that can fit in a given cylinder
    :param GUMBALL_VOLUME: a constant float, the volume of the object being used
    :param usable_volume: a float, the usable volume of the cylinder
    :return: num_gumballs, the number of gumballs that'll fit in the container
    """
    num_gumballs = 0
    # Calculate the number of gumballs and then truncate the decimal portion:
    # we want the whole number of gumballs, and the int function rounds down
    num_gumballs = int(usable_volume / GUMBALL_VOLUME)
    return num_gumballs


def output_message(ball_amt):
    """
    Prints the output message
    :param ball_amt:
    :return: none
    """
    print("\nThe jar will hold", ball_amt, "gumballs!")
    print("\nGoodbye!")


main()
