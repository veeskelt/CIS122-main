# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 9
# Date: 2/15/2024 (adjusted 3/13/2024)
# Description: Example: This program prompts the user for the
#   playtime of any program before and after a session
#   and output the session time in hours and minutes (rounded).
# Input: session time in hours, session time in minutes, continue option
# Output: session end times, session run times
# Sources: Lab 9 specifications, previous labs
#
# *****************************************************************************
# pseudocode
# Intro message
# Note on the expected input format
# Get the first run time from the user
#   Need to check of the list of class objects is empty
#       does if(len(session_times)) == 0) work? -Yes
#   if so, session_time 1 is equal to end_time_full (end_time_hr + (end_time_mins/60))
#   If not, it's end_time_full - session_time[i] or something
# Loop the above until the user is done entering times - standard 3 option menu
# Once done, sum session times, average them, print

import valid as v


class Session:
    __length = 0.0
    __note = ""

    def __init__(self, length, note):
        self.__length = length
        self.__note = note

    def get_length(self):
        return self.__length

    def get_note(self):
        return self.__note

    def set_length(self, length):
        self.__length = length

    def set_note(self, note):
        self.__note = note

    def __str__(self):
        printed_string = ""
        if len(self.__note) == 0:
            printed_string = "Length: {:.2f}, Note: {}".format(self.__length, "<no user notes>")
        else:
            printed_string = "Length: {:.2f}, Note: {}".format(self.__length, self.__note)
        return printed_string


CARRY_ON = 'y'


def main():
    run_time_hrs = 0
    run_time_mins = 0
    run_time_full = 0
    times_list = []
    sesh_list = []
    note = ""
    session_time = 0.0
    session_sum = 0.0
    session_average = 0.0
    cont = "y"
    greeting()
    print_input_note()
    while cont == 'y':
        run_time_hrs = get_runtime_hrs()
        #        print(run_time_hrs)
        run_time_mins = get_runtime_mins()
        #        print(run_time_mins)
        run_time_full = time_calc_full(run_time_hrs, run_time_mins)
        #        print(run_time_full)
        times_list.append(run_time_full)
        #        print(times_list)
        #        note = get_note()
        session_time = session_calc(run_time_full, sesh_list, times_list)
        #        print(session_time)
        added_note = get_note()
        sesh_list.append(Session(session_time, added_note))
        for i in range(len(sesh_list)):
            print(sesh_list[i])
        cont = proceed()
    session_average = calc_sesh_average(sesh_list)
    output(times_list, sesh_list, session_average)


def get_runtime_hrs():
    """
    This function gets the session end times from the user
    :return run_hrs: the input time's hours from the user
    """
    run_hrs = 0
    prompt = "\nPlease enter the total run time of the program in hours: "
    run_hrs = v.get_integer(prompt)
    while run_hrs < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer(prompt)

    return run_hrs


def get_runtime_mins():
    """
    This function gets the run time in minutes from the user.
    :return run_mins: the input time's minutes from the user, divided by 60 to
    make a decimal value
    """
    run_mins = 0
    prompt = "\nNow please enter the minutes portion of the run time: "
    run_mins = v.get_integer(prompt)
    while run_mins < 0:
        print("The run time cannot be negative.")
        run_hrs = v.get_integer(prompt)
    run_mins = run_mins / 60
    # This gives us the minute format in decimal form
    return run_mins


def time_calc_full(time_hrs, time_mins):
    """
    Calculates the true run times
    :param time_hrs: a list of the run times' hours
    :param time_mins: a list of the run times' minutes
    :return: nothing
    """
    full_time = 0
    full_time = time_hrs + time_mins
    # Convert the result into an absolute value to accounting for
    # backwards session times entered
    return full_time


def session_calc(time_full, sesh_list, times_list):
    """
    Calculates the session time in hours
    :param times_list: a list of the compound times the user has entered
    :param time_full: the last time the user entered
    :param sesh_list: a list of the session times
    :return: nothing
    """
    session_length = 0.0
    somthing_or_other = 0.0
    if len(sesh_list) == 0:
        session_length = time_full
    elif len(sesh_list) != 0:
        session_length = times_list[-1] - times_list[-2]
    #        print(session_length)
    return session_length


def get_note():
    """
    This gets a string from the user and returns it.
    :return: note, the user-input string.
    """
    note = ""
    note = input("If you have any notes for this entry, please enter them, "
                 "otherwise press enter: ")
    return note


def calc_sesh_sum(sesh_list):
    """
    Calculates the sum of all session times. Mainly used for calculating the
    average.
    :param sesh_list: a list of the session times
    :return:
    """
    sesh_sum = 0.0
    for i in range(len(sesh_list)):
        sesh = sesh_list[i].get_length()
        sesh_sum = sesh_sum + sesh
    return sesh_sum


def calc_sesh_average(sesh_list):
    """
    Calculates the average time of all the sessions
    :param sesh_list: the list of sessions
    :return:
    """
    average = 0.0
    average = calc_sesh_sum(sesh_list) / len(sesh_list)
    return average


def output(times, sesh_list, average):
    """
    Prints the result of all calculations
    :param times:
    :param sesh_list:
    :param average:
    :return:
    """
    full_times = ""
    sesh_times = ""
    print("Cumulative results:")
    print("{:<15} {:<13} {}".format("Total Time", "Session Time", "Notes"))
    for i in range(len(sesh_list)):
        full_times = (str(round(times[i], 2)) + " hours")
        sesh_times = (str(round(sesh_list[i].get_length(), 2)) + " hours")
        print("{:<3}{:>10} {:>17} {}".format(i + 1, full_times, sesh_times,
                                             sesh_list[i].get_note()))

    print("Average Session Length: {:.2f} hours".format(average))


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("\nHello! This program calculates a session lengths of a program"
          "after asking for \nthe run times of program at the beginning"
          " of each session.")


def print_input_note():
    """
    This function prints a note regarding how the input is expected to be
    formatted.
    :return: nothing
    """
    print("\nNote: when the program asks for the run time in hours, it is "
          "referring to the \nhours portion of the run time; if a program "
          "was run for 3 hours and 28 minutes, \nyou would enter 3. "
          "Likewise, when it asks for the minutes portion, you would "
          "\nenter 28. Any decimal places entered will be ignored.")


def proceed():
    """
    Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    :return: cont, a char, represents user's choice
    """
    cont = ""
    cont = v.get_y_or_n("\nDo you have another run time to enter? (y/n): ")
    return cont


if __name__ == "__main__":
    main()

# Future plans
#   Read session times from a file
#   Running average of session times
#   Highlight outliers, 0 values
#       Possibly add notes to these outliers and 0 values
#   Version that hooks into steam API for game runtimes???
#   Does blender have something similar I can hook into?
