# Author: Vega Skelton
# Version: 1
# Sample Run:
#
# Hello!
# I'm the Change Calculator-inator!
# Enter your change and I will calculate how much you'll get back in
# dollars, quarters, dimes, nickels, and pennies!
#
# Enter your change ($x.xx): $1.43
# You will get back:
# 1 Dollar
# 1 Quarter
# 1 Dime
# 1 Nickel
# 3 Pennies
#
# Goodbye!

def main():
    change = 0.0
    change_dollars = 0.0
    change_quarters = 0.0
    change_dimes = 0.0
    change_nickels = 0.0
    change_pennies = 0.0

    greeting()
    change = get_change()
    if change > 0:
        change_dollars, change = calc_change_dollars(change)
        change_quarters, change = calc_change_quarters(change)
        change_dimes, change = calc_change_dimes(change)
        change_nickels, change_pennies = calc_change_nickels(change)
        print_dollars(change_dollars)
        print_quarters(change_quarters)
        print_dimes(change_dimes)
        print_nickels(change_nickels)
        print_pennies(change_pennies)
    else:
        change_is_zero()
    goodbye()


def greeting():
    """Prints a greeting to the user
    return: nothing
    """
    print("Hello!")
    print("I'm the Change Calculator-inator!")
    print("Enter your change and I will calculate how much you'll get back in ")
    print("dollars, quarters, dimes, nickels, and pennies.")


def goodbye():
    """Prints a goodbye message to the user
    return: nothing
    """
    print("Goodbye!")


def change_is_zero():
    """If change is equal to zero, this is executed, otherwise this is unused
    """
    print("You get no change in return.")


def get_change():
    """Gets the change from the user
    return: func_change, the value input by the user rounded to two decimals
    and set to its absolute value
    """
    func_change = 0.0
    func_change = float(input("Enter your change ($x.xx): $"))
    func_change = round(func_change, 2)  # rounds input to two decimal places
    func_change = abs(func_change)
    # the third functional line in this function rounds the input to two
    # decimal places
    # the sets it to the absolute value of the variable, to account for
    # negative user inputs.
    return func_change


def calc_change_dollars(usr_change):
    """Calculates the user's change in dollars and returns the result and
    the remaining change
    param: usr_change, a float
    returns: usr_change_dollars, usr_change, the first is the user's change
    in dollars and the second is the remaining change after factoring out
    the dollar amount.
    """
    usr_change_dollars = 0.0
    usr_change_dollars = usr_change // 1
    usr_change_dollars = int(usr_change_dollars)
    usr_change = usr_change % 1
    usr_change = round(usr_change, 2)
    usr_change = int(usr_change * 100)
    # functional line 2 gets the dollar amount by int dividing usr_change by 1
    # functional line 3 reassigns usr_change to the same variable with the
    # leading 1 stripped
    # functional line 4 rounds usr_change to 2 because I kept loosing pennies
    # functional line 5 multiplies usr_change by 100 to convert it into a
    # whole number and makes it into an int
    # further functions will only contain functional lines 1 and 3
    return usr_change_dollars, usr_change


def calc_change_quarters(usr_change):
    """This function calculates the user's change in quarters and returns
    the result and the remaining change
    param: usr_change, a float
    returns: usr_change_quarters, usr_change, the first is the user's change
    in quarters and the second is the remaining change after factoring out the
    quarter amount.
    """
    usr_change_quarters = 0
    usr_change_quarters = usr_change // 25
    usr_change = usr_change % 25
    return usr_change_quarters, usr_change


def calc_change_dimes(usr_change):
    """This function calculates the user's change in dimes and returns
    the result and the remaining change
    param: usr_change_dimes, a float
    returns: usr_change_dimes, usr_change, the first is the user's change in
    dimes and the second is the remaining change after factoring out the dime
    amount.
    """
    usr_change_dimes = 0
    usr_change_dimes = usr_change // 10
    usr_change = usr_change % 10
    return usr_change_dimes, usr_change


def calc_change_nickels(usr_change):
    """This function calculates the user's change in nickels and returns
    the result and the remaining change
    param: usr_change, a float
    returns: usr_change_nickels, usr_change, the first is the user's change in
    nickels and the second is the remaining change after factoring out the
    nickel amount.
    """
    usr_change_nickels = 0
    usr_change_nickels = usr_change // 5
    usr_change = usr_change % 5
    return usr_change_nickels, usr_change


def print_dollars(usr_change_dollars):
    """This function prints the user's change in dollars.
    param: usr_change_dollars, an int
    returns: nothing
    """
    if usr_change_dollars > 0:
        if usr_change_dollars == 1:
            print("You have", usr_change_dollars, "dollar;")
        else:
            print("You have", usr_change_dollars, "dollars;")


def print_quarters(usr_change_quarters):
    """This function prints the user's change in quarters.
    param: usr_change_quarters, an int
    returns: nothing
    """
    if usr_change_quarters > 0:
        if usr_change_quarters == 1:
            print("You have", usr_change_quarters, "quarter;")
        else:
            print("You have", usr_change_quarters, "quarters;")


def print_dimes(usr_change_dimes):
    """This function prints the user's change in dimes.
    param: usr_change_dimes, an int
    returns: nothing
    """
    if usr_change_dimes > 0:
        if usr_change_dimes == 1:
            print("You have", usr_change_dimes, "dime;")
        else:
            print("You have", usr_change_dimes, "dimes;")


def print_nickels(usr_change_nickels):
    """This function prints the user's change in nickels.
    param: usr_change_nickels, an int
    returns: nothing
    """
    if usr_change_nickels > 0:
        if usr_change_nickels == 1:
            print("You have", usr_change_nickels, "nickel;")
        else:
            print("You have", usr_change_nickels, "nickels;")


def print_pennies(usr_change_pennies):
    """This function prints the user's change in pennies
    param: usr_change_pennies, an int
    returns: nothing
    """
    if usr_change_pennies > 0:
        if usr_change_pennies == 1:
            print("and", usr_change_pennies, "penny.")
        else:
            print("and", usr_change_pennies, "pennies.")


if __name__ == "__main__":
    main()

