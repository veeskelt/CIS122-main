# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 6
# Date: 2/15/2024
# Description: Example: This program prompts the user for the
#   playtime of any program before and after a session
#   and output the session time in hours and minutes (rounded).
# Input: old play time, new play time
# Output: simple session time, session time in hours,
#   session time in minutes
# Sources: Lab 7 specifications, previous labs
# *****************************************************************************
#                          Sample Run
# Hello! This program calculates a session length of a program after
# asking the play times of the beginning and end of a working session.
#
# Please enter the total program run time in hours:
# (whole numbers only): 20
#
# Please enter the total program run time in minutes
# (whole numbers only): 36
#
# Do you want to enter another session? (y/n): y
#
# Please enter the total program run time in hours:
# (whole numbers only): 22
#
# Please enter the total program run time in minutes
# (whole numbers only): 30
#
# Do you want to enter another session? (y/n): n
# Results:
# Run Time (hours)    Session Time (hours)
# _____________________________________
# 20.6                20.6
# 22.5                1.8999999999999986
#
# Thank you for using this program.
# Have a nice day!
# *****************************************************************************


import valid as v

CARRY_ON = 'y'


def main():
    """
    This program calculates the session length of a given thing given the
    total run time before the session and the run time after the session,
    and outputs the session time in decimal hours, integer hours, and integer
    minutes.
    :return: nothing
    """
    run_time_hrs = []
    run_time_mins = []
    run_time_full = []
    sesh_list = []

    cont = "y"

    # Here we greet the user.
    greeting()

    while cont == CARRY_ON:
        # While cont is equal to CARRY_ON, the program loops. cont can only be
        # set to something else in the proceed function, which is at the end
        # of this loop.

        # Gets old_time from the user
        get_runtime_hrs(run_time_hrs)
        get_runtime_mins(run_time_mins)
        # "Wanna do it again?"
        cont = proceed()

    # Calculate our times:
    time_calc_full(run_time_hrs, run_time_mins, run_time_full)
#    print(run_time_full)
    session_calc(run_time_full, sesh_list)
#    print(sesh_list)

    # And now we output our output
    output(run_time_full, sesh_list)
    exit_message()


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("\nHello! This program calculates a session length of a program"
          "after asking for \n the run times of program at the the beginning"
          " and end of a session.")


def proceed():
    """
    Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    :return: cont, a char, represents user's choice
    """
    cont = ""
    cont = v.get_y_or_n("\nDo you want to enter another session? (y/n): ")
    return cont


def get_runtime_hrs(run_time_hrs):
    """
    This function gets the run time in hours from the user.
    :param run_time_hrs: the list of run times' hours
    :returns: nothing
    """
    run_hrs = 0
    # We don't want to append anything to the list until we've validated the
    # input, hence this variable.
    run_hrs = v.get_integer("\nPlease enter the total program run time in hours"
                            ": \n(whole numbers only): ")
    if run_hrs < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer("\nPlease enter the total program run in hours"
                                "\n(whole numbers only): ")
    else:
        run_time_hrs.append(run_hrs)
    return 0


def get_runtime_mins(run_time_mins):
    """
    This function gets the run time in minutes from the user.
    :param run_time_mins: the list of run times' minutes
    :returns: nothing
    """
    run_mins = 0
    run_mins = v.get_integer("\nPlease enter the total program run time in "
                             "minutes \n(whole numbers only): ")
    if run_mins < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer("\nPlease enter the total program run in "
                                "minutes \n(whole numbers only): ")
    else:
        run_mins = run_mins / 60
        run_mins = round(run_mins, 2)
        # This gives us the minute format in decimal form, then rounds it down
        # to two decimals
        # Second step may be unnecessary if I can get the output formatting right
        run_time_mins.append(run_mins)
    return 0


def time_calc_full(run_time_hrs, run_time_mins, run_time_full):
    """
    Calculates the true run times
    :param run_time_hrs: a list of the run times' hours
    :param run_time_mins: a list of the run times' minutes
    :param run_time_full: a list of the full run times
    :return: nothing
    """
    for i in range(len(run_time_hrs)):
        total_time = run_time_hrs[i] + run_time_mins[i]
        run_time_full.append(total_time)

    return 0


def session_calc(run_time_full, sesh_list):
    """
    Calculates the session time in hours
    :param run_time_full:
    :param sesh_list: a list of the session times
    :return: nothing
    """
    sesh_time = 0
    for i in range(len(run_time_full)):
        if i == 0:
            sesh_time = run_time_full[i]
            sesh_list.append(sesh_time)
        else:
            sesh_time = run_time_full[i] - run_time_full[i - 1]
            sesh_list.append(sesh_time)


def output(run_time_full, sesh_list):
    """
    Outputs the results to the user
    :param run_time_full: a list of the run times
    :param sesh_list: a list of the session times
    :return: nothing
    """
    # I learned how the format string function works with practice 8, so
    # I'm gunna use it.
    print("Results: ")
    print("{: <20}{: <10}".format("Run Time (hours)", "Session Time (hours)"))
    print("_____________________________________")
    for i in range(len(run_time_full)):
        print("{: <20}{: <10}".format("{:.2f}".format(run_time_full[i]),
                                      "{:.2f}".format(sesh_list[i])))


def exit_message():
    """
    This function prints an exit message.
    :return: nothing
    """
    print("\nThank you for using this program.")
    print("Have a nice day!")


if __name__ == "__main__":
    main()

# Future planning (distant future for some of these)
# Allow entering multiple session times
#   Knowledge required: lists? Can lists be of an indefinite size?
#
# Fancy output only gets displayed if the user asks for it
#   Have the knowledge for this, but no need for it atm.
#   Could do it anyway.
# Read session times from a file
# Running average of session times
# Highlight outliers, 0 values
#   Possibly add notes to these outliers and 0 values
# Version that hooks into steam API for game runtimes???
# Does blender have something similar I can hook into?
