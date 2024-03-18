# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 9
# Date: 2/15/2024 (adjusted 3/13/2024)
# Description: Example: This program prompts the user for the
#   playtime of any program before and after a session
#   and output the session time in hours and minutes (rounded).
# Input: session time in hours, session time in minutes, continue option
# Output: session end times, session run times
# Sources: Lab 9 specifications, previous labs, this thread on accessing the
# last item in a list:
# https://stackoverflow.com/questions/930397/how-do-i-get-the-last-element-of-a-list
#
# *****************************************************************************
# Hello! This program calculates the session lengths of a program after asking
# for the run times of program at the beginning of each session.
#
# Note: when the program asks for the run time in hours, it is referring to the
# hours portion of the run time; if a program was run for 3 hours and 28
# minutes, you would enter 3. Likewise, when it asks for the minutes portion,
# you would enter 28. Any decimal places entered will be ignored.
#
# Please enter the total run time of the program in hours: 1
#
# Now please enter the minutes portion of the run time: 18
# If you have any notes for this entry, enter them now, otherwise press enter:
# Length: 1.30, Note: <no user notes>
#
# Do you have another run time to enter? (y/n): y
#
# Please enter the total run time of the program in hours: 1
#
# Now please enter the minutes portion of the run time: 36
# If you have any notes for this entry, enter them now, otherwise press enter:
# job crashed
# Length: 1.30, Note: <no user notes>
# Length: 0.30, Note: job crashed
#
# Do you have another run time to enter? (y/n): y
#
# Please enter the total run time of the program in hours: 2
#
# Now please enter the minutes portion of the run time: 48
# If you have any notes for this entry, enter them now, otherwise press enter:
# successful run
# Length: 1.30, Note: <no user notes>
# Length: 0.30, Note: job crashed
# Length: 1.20, Note: successful run
#
# Do you have another run time to enter? (y/n): y
#
# Please enter the total run time of the program in hours: 3
#
# Now please enter the minutes portion of the run time: 54
# If you have any notes for this entry, enter them now, otherwise press enter:
# bad output, reconfigure settings
# Length: 1.30, Note: <no user notes>
# Length: 0.30, Note: job crashed
# Length: 1.20, Note: successful run
# Length: 1.10, Note: bad output, reconfigure settings
#
# Do you have another run time to enter? (y/n): n
# Cumulative results:
# Index  Total Time      Session Time    Notes
# 1.     1.3 hours          1.3 hours
# 2.     1.6 hours          0.3 hours    job crashed
# 3.     2.8 hours          1.2 hours    successful run
# 4.     3.9 hours          1.1 hours    bad output, reconfigure settings
# Average Session Length: 0.97 hours


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
            printed_string = "Length: {:.2f}, Note: {}".format(self.__length,
                                                               "<no user notes>")
        else:
            printed_string = "Length: {:.2f}, Note: {}".format(self.__length,
                                                               self.__note)
        return printed_string


CARRY_ON = 'y'


def main():
    run_time_hrs = 0
    run_time_mins = 0
    run_time_full = 0
    times_list = []
    sesh_list = []
    added_note = ""
    session_time = 0.0
    session_sum = 0.0
    session_average = 0.0
    choice = 0
    target = 0
    greeting()
    print_input_note()
    show_menu()
    choice = get_choice()
    while choice != 5:
        if choice == 1:
            # Get times and calculate full time
            run_time_hrs = get_runtime_hrs()
            run_time_mins = get_runtime_mins()
            run_time_full = time_calc_full(run_time_hrs, run_time_mins)
            # Add this to the list of runtimes
            times_list.append(run_time_full)
            # Calculate the session time, get the user note, and create a Session
            # object from the data
            session_time = session_calc(run_time_full, sesh_list, times_list)
            added_note = user_note()
            sesh_list.append(Session(session_time, added_note))
            for i in range(len(sesh_list)):
                print(i + 1, ". ", sesh_list[i], sep="")
            show_menu()
            choice = get_choice()

        elif choice == 2:
            # Change a note
            if len(sesh_list) == 0:
                print("\nThere are no entries to modify.")
            else:
                target = change_which_note(sesh_list)
                new_note = user_note()
                sesh_list[target].set_note(new_note)
            show_menu()
            choice = get_choice()

        elif choice == 3:
            # Output the list
            if len(sesh_list) == 0:
                print("\n There is no data to display.")
            else:
                session_average = calc_sesh_average(sesh_list)
                output(times_list, sesh_list, session_average)
            show_menu()
            choice = get_choice()

        elif choice == 4:
            sesh_list = []  # This clears the list
            show_menu()
            choice = get_choice()


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
    if run_mins < 0 or run_mins > 59:
        print("The run time cannot be negative or above 59.")
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


def user_note():
    """
    This gets a string from the user and returns it.
    :return: note, the user-input string.
    """
    note = ""
    note = input("If you have any notes for this entry, please enter them, "
                 "otherwise press enter: \n")
    return note


def calc_sesh_sum(sesh_list):
    """
    Calculates the sum of all session times. Mainly used for calculating the
    average.
    :param sesh_list: a list of the session times
    :return sesh_sum: the sum of the session times
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
    :return average: the average of all sessions
    """
    average = 0.0
    average = calc_sesh_sum(sesh_list) / len(sesh_list)
    return average


def output(times, sesh_list, average):
    """
    Prints the result of all calculations
    :param times: a list of runtimes
    :param sesh_list: a list of "Session" objects
    :param average: the average of all session times
    :return: nothing
    """
    full_times = ""
    sesh_times = ""
    index = ""
    print("Cumulative results:")
    print("{:<7}{:>10} {:>17} {}".format("Index", "Total Time", "Session Time",
                                         "   Notes"))
    for i in range(len(sesh_list)):
        full_times = (str(round(times[i], 2)) + " hours")
        sesh_times = (str(round(sesh_list[i].get_length(), 2)) + " hours")
        index = (str(i + 1) + ".")
        note = ("   " + sesh_list[i].get_note())
        print("{:<6} {:>9} {:>18} {}".format(index, full_times, sesh_times,
                                             note))

    print("Average Session Length: {:.2f} hours".format(average))


def show_menu():
    """
    This function prints a menu to give the user the choice of clearing the
    times list, adding a new entry, or modifying an entry's note.
    :return: none, decorative function
    """
    print("\n1. Add a new entry")
    print("2. Modify an existing entry's note")
    print("3. Show all entries in the list")
    print("4. Clear all entries")
    print("5. Exit")


def get_choice():
    """
    This function gets the menu choice from the user.
    :return choice: the
    """
    choice = 0
    choice = v.get_integer("\n Enter your selection (1-5): ")
    while choice < 0 or choice > 5:
        print("Invalid selection.")
        choice = v.get_integer("\n Enter your selection (1-5): ")
    return choice


def change_which_note(sesh_list):
    """
    This function gets the list of notes for the user and returns it.
    :param sesh_list: list of sessions, used for showing the range of valid
     inputs
    :return changed_note: chosen entry to modify
    """
    changed_note = ""
    prompt = ("Which of the", str(len(sesh_list)), " notes would you like to "
                                                   "change: \n")
    changed_note = v.get_integer(prompt)
    while changed_note < 0 or changed_note > len(sesh_list):
        print("Invalid choice.")
        changed_note = v.get_integer(prompt)
    changed_note = changed_note - 1  # Because this'll be an index position,
    # gotta subtract one from it b/c list entries start at position 0 and not 1
    return changed_note


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("\nHello! This program calculates the session lengths of a program"
          " after asking \nfor the run times of program at the beginning"
          " of each session.")


def print_input_note():
    """
    This function prints a note regarding how the input is expected to be
    formatted.
    :return: nothing
    """
    print("\nNote: when the program asks for the run time in hours, it is "
          "referring to the \nhours portion of the run time; if a program "
          "was run for 3 hours and 28 \nminutes, you would enter 3. "
          "Likewise, when it asks for the minutes portion, \nyou would "
          "enter 28. Any decimal places entered will be ignored.")


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
#   Highlight outliers, 0 values
#       This requires knowing how to sort
#   Version that hooks into steam API for game runtimes???
#   Does blender have something similar I can hook into?
#   Reconfigure the program to take session times and calculate total run times
#   ^^^ That's far more useful of a practical application, for say, rendering
#   video files or ripping bluray discs or rendering something in blender.
#       Can't do it now because I need to turn this in and I have a math final
#       to study for.
