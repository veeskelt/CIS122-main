import valid as v

# Welcome to PCC Credit Union

# 1. View balance
# 2. Make deposit
# 3. Withdraw funds
# 4. Quit

# Enter choice: 1
# Account balance: $ 0.00

# Enter your selection: 2
# Enter your deposit :$ 150.60
# Funds deposited: $ 150.60

# Enter your selection: 1
# Account balance: $ 150.60

# Enter your selection: 3
# Enter your withdrawal: $10.23
# Funds withdrawn: $10.23

# Enter your selection: 1
# Account balance: $ 140.37

# Enter your selection: 4

# Thank you for using PCC Credit Union!


QUIT = 4


def main():
    welcome_message()
    operation_loop()
    exit_message()


def operation_loop():
    """
    Contains the operational loop of the program.
    :returns: nothing
    """
    choice = 0
    balance = 0.0
    deposit = 0.0
    withdrawal = 0.0
    print_menu()
    choice = get_choice()
    while choice != QUIT:
        if choice == 1:
            view_balance(balance)
            choice = get_choice()
        elif choice == 2:
            deposit = get_deposit()
            balance = calc_deposit(balance, deposit)
            # print("Funds deposited: $", format(deposit, ".2f"))
            print_deposit(deposit)
            choice = get_choice()
        elif choice == 3:
            withdrawal = get_withdrawal()
            check_withdrawal(balance, withdrawal)
            balance = calc_withdrawal(balance, withdrawal)
            # print("Funds withdrawn: $", format(withdrawal, ".2f"))
            print_withdrawal(withdrawal)
            choice = get_choice()


def welcome_message():
    """
    Prints a welcome message.
    :returns: nothing
    """


def exit_message():
    """
    Prints an exit message.
    :return: nothing
    """
    print("\nThank you for using PCC Credit Union!")


def print_menu():
    """
    Function to print the menu to view balance, make deposit, or withdraw
     funds
    :return: none
    """
    print("\n1. View balance")
    print("2. Make deposit")
    print("3. Withdraw funds")
    print("4. Quit")


def get_choice():
    """Gets the choice from the user
    :return: choice, an int, represents the user's selection
    """
    choice = 0
    choice = v.get_integer("\nEnter your selection: ")
    while choice < 1 or choice > 4:
        print("Invalid selection. Please try again.")
        choice = v.get_integer("\nEnter your selection: ")
    else:
        return choice


def get_deposit():
    """
    Gets the deposit from the user, must be a Real number.
    :return: deposit, a float, the inputted amount form the user.
    """
    deposit = 0.0
    deposit = v.get_real("\nEnter your deposit: ")
    return deposit


def calc_deposit(balance, deposit):
    """
    Calculates the new balance from the deposit amount.
    :param balance: a float, must be a real number.
    :param deposit: a float, must be a real number.
    :return: balance, a float, after having deposit added to it.
    """
    balance = balance + deposit
    return balance


def print_deposit(deposit):
    """
    Prints the last deposit entered.
    :return: nothing
    """
    print("Funds deposited: $", deposit)


def get_withdrawal():
    """Gets the """
    withdrawal = 0.0
    withdrawal = v.get_real("\nEnter your withdrawal: $")
    return withdrawal


def check_withdrawal(balance, withdrawal):
    """
    Checks the withdrawal from the user and checks
    :param balance: a float, the user's balance.
    :param withdrawal: a float, the user's withdrawal
    :return withdrawal: a float, only returned if the withdrawal is valid.
    """
    while balance < withdrawal or withdrawal <= 0:
        print("Invalid withdrawal amount. (Cannot be more than your balance"
              "or 0.)")
        withdrawal = get_withdrawal()
    else:
        return withdrawal
    # return withdrawal


def calc_withdrawal(balance, withdrawal):
    """
    Calculates the balance from the withdrawal amount.
    :param balance: a float, the user's balance
    :param withdrawal: a float, the user's withdrawal
    :return: balance: a float, the user's balance after withdrawal is
    subtracted.
    """
    balance = balance - withdrawal
    return balance


def print_withdrawal(withdrawal):
    """
    Prints the last withdrawal entered.
    :return: nothing
    """
    print("Funds withdrawn: $", withdrawal)


def view_balance(balance):
    """
    Function to print current account balance.
    :param balance: float, current account balance
    :return: none
    """
    print("Account balance: $", format(balance, ".2f"))


main()
