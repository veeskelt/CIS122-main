# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 7
# Date: 2/15/2024 (adjusted 3/13/2024)
# Description: Example: This program prompts the user for the
#   playtime of any program before and after a session
#   and output the session time in hours and minutes (rounded).
# Input: old play time, new play time
# Output: simple session time, session time in hours,
#   session time in minutes
# Sources: Lab 7 specifications, previous labs
#
# *****************************************************************************
#                          Sample Run
# Hello! This program calculates a session lengths of a program after asking for
# the run times of program at the beginning of each session.
#
# Note: when the program asks for the run time in hours, it is referring to the
# hours portion of the run time; if a program was run for 3 hours and 28 minutes,
# you would enter 3. Likewise, when it asks for the minutes portion, you would
# enter 28.
#
# Please enter the total run time of the program in hours: 20
#
# Now please enter the minutes portion of the run time: 36
#
# Do you have another run time to enter? (y/n): y
#
# Note: when the program asks for the run time in hours, it is referring to the
# hours portion of the run time; if a program was run for 3 hours and 28 minutes,
# you would enter 3. Likewise, when it asks for the minutes portion, you would
# enter 28.
#
# Please enter the total run time of the program in hours: 22
#
# Now please enter the minutes portion of the run time: 30
#
# Do you have another run time to enter? (y/n): n
# Results:
# Run Time (hours)    Session Time (hours)
# _____________________________________
# 20.60               20.60
# 22.50               1.90
# The sum of all session lengths is 22.50
# The average of all session lengths is 11.25
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
    session_sum = 0.0
    session_average = 0.0
    cont = "y"

    # Here we greet the user.
    greeting()

    while cont == CARRY_ON:
        # While cont is equal to CARRY_ON, the program loops. cont can only be
        # set to something else in the proceed function, which is at the end
        # of this loop.

        # Gets old_time from the user
        print("\nNote: when the program asks for the run time in hours, it is "
              "referring to the \nhours portion of the run time; if a program "
              "was run for 3 hours and 28 minutes, \nyou would enter 3. "
              "Likewise, when it asks for the minutes portion, you would "
              "\nenter 28.")
        get_runtime_hrs(run_time_hrs)
        get_runtime_mins(run_time_mins)
        # "Wanna do it again?"
        cont = proceed()

    # Calculate our times:
    time_calc_full(run_time_hrs, run_time_mins, run_time_full)
    session_calc(run_time_full, sesh_list)
    session_sum = calc_sesh_sum(sesh_list)
    session_average = calc_sesh_average(sesh_list)

    # And now we output our output
    output(run_time_full, sesh_list, session_sum, session_average)
    exit_message()


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("\nHello! This program calculates a session lengths of a program"
          "after asking for \nthe run times of program at the beginning"
          " of each session.")


def proceed():
    """
    Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    :return: cont, a char, represents user's choice
    """
    cont = ""
    cont = v.get_y_or_n("\nDo you have another run time to enter? (y/n): ")
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
    prompt = "\nPlease enter the total run time of the program in hours: "
    run_hrs = v.get_integer(prompt)
    if run_hrs < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer(prompt)
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
    prompt = "\nNow please enter the minutes portion of the run time: "
    run_mins = v.get_integer(prompt)
    if run_mins < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer(prompt)
    else:
        run_mins = run_mins / 60
        # This gives us the minute format in decimal form
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
        total_time = abs(run_time_hrs[i] + run_time_mins[i])
        # Convert the result into an absolute value to accounting for
        # backwards session times entered
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


def calc_sesh_sum(a_list):
    """
    Sums the values in a list
    :param a_list: a list of values
    :return total_sum: the sum of the values
    """
    total_sum = 0.0
    for index in range(len(a_list)):
        # we need to check if the items in the list are ints and/or floats
        if type(a_list[index]) is int or type(a_list[index]) is float:
            total_sum = total_sum + a_list[index]
    return total_sum


def calc_sesh_average(a_list):
    """
    Calculates the average of the items in a list
    :param a_list: a list of values
    :return: the average of the list items
    """
    average = 0.0
    avg_sum = calc_sesh_sum(a_list)
    average = avg_sum / len(a_list)
    return average


def output(run_time_full, sesh_list, sesh_sum, sesh_average):
    """
    Outputs the results to the user
    :param run_time_full: a list of the run times
    :param sesh_list: a list of the session times
    :param sesh_sum: the sum of all the session times
    :param sesh_average: the average of the session times
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
    print("The sum of all session lengths is {:.2f}".format(sesh_sum))
    print("The average of all session lengths is "
          "{:.2f}".format(sesh_average))


def exit_message():
    """
    This function prints an exit message.
    :return: nothing
    """
    print("\nThank you for using this program.")
    print("Have a nice day!")


if __name__ == "__main__":
    main()


# Read session times from a file
# Running average of session times
# Highlight outliers, 0 values
#   Possibly add notes to these outliers and 0 values
# Version that hooks into steam API for game runtimes???
# Does blender have something similar I can hook into?
