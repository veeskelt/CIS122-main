# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 5
# Date: 2/9/2024
# Description: Example: This program prompts the user for the
#   playtime of a yet unspecified game before and after a session
#   after a session and output the session time in hours and
#   minutes (rounded).
# Input: old play time, new play time
# Output: simple session time, session time in hours,
#   session time in minutes
# Sources: Lab 5 specifications, got help from a friend debugging why my average
# function was breaking
# *****************************************************************************
#                          Sample Run
# Hello! This program calculates a session length of a game after
#   asking the play times of the beginning and end of a gaming
#   session.
# Please enter the game run time at the start of the session: 20.6
# Please enter the run time at the end: 22.5
# This session lasted for 1.9 hours, or roughly 1 hours and 54 minutes.
# *****************************************************************************


def main():
    """
    This program calculates the session length of a given thing given the
    total run time before the session and the run time after the session,
    and outputs the session time in decimal hours, integer hours, and integer
    minutes.
    :return: nothing
    """
    old_time = 0.0
    new_time = 0.0
    session_time_full = 0.0
    session_time_hrs = 0
    session_time_mins = 0.0
    cont = "y"
    while cont == "y":
        greeting()
        old_time = get_old_time()
        new_time = get_new_time()
        session_time_full = time_calc_full(old_time, new_time)
        session_time_hrs = time_calc_hrs(session_time_full)
        session_time_mins = time_calc_mins(session_time_full)
        output(session_time_full, session_time_hrs, session_time_mins)
        cont = proceed()
    exit_message()


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("Hello! This program calculates a session length of a program after"
          " asking for \n the run times of program at the the beginning and "
          "end of a session.")


def proceed():
    """Prompts the user for a request to continue until a valid input is
    entered ('y' or 'n').
    :return: cont, a char, represents
    """

    # cont = ""
    cont = input("\nDo you want to continue? (y/n) ")
    cont = cont.lower()
    # The following checks to make sure the input was a valid input
    if cont != 'y' and cont != 'n':
        print("This is not a valid input. Please try again.")
        cont = input("Do you want to continue? (y/n) ")
        cont = cont.lower()  # Set it to lowercase to match cases elsewhere
    return cont


def get_old_time():
    """
    This function gets the old time from the user
    :return: old, short for old time. Shortened so it doesn't get confused
    with main's old_time variable.
    """
    old = 0.0
    old = float(input("Please enter the total game run time "
                      "at the start of the session \n(in decimal "
                      "form): "))
    return old


def get_new_time():
    """
    This function gets the new time from the user
    :return: new, short for new time. Shortened so it doesn't get confused
    with main's new_time variable.
    """
    new = 0.0
    new = float(input("Please enter the total game run time "
                      "at the end of the session \n(in decimal "
                      "form): "))
    return new


def time_calc_full(old_time, new_time):
    """
    Calculates the true session time
    :param old_time: One of two times the program works with. should be, but
    doesn't have to be, the lower of the two times. This value should be
    obtained from the user or a file.
    :param new_time: One of two times the program works with. should be, but
    doesn't have to be, the higher of the two times. This value should be
    obtained from the user or a file.
    :return: sesh_full, short for the full session time.
    """
    sesh_full = 0.0
    sesh_full = abs((new_time - old_time))
    # The session time variables are being converted to absolute values in all
    # the time_calc functions to account for the user entering the times in
    # the wrong order.
    return sesh_full


def time_calc_hrs(session_time_full):
    """
    Calculates the session time in hours
    :param session_time_full: the variable that was assigned to the result of
    time_calc_full(). Should be a float.
    :return: sesh_hrs, short for the session time in hours
    """
    sesh_hrs = 0
    sesh_hrs = int(abs(session_time_full // 1))  # Truncates the decimal
    # We convert this to int because we only need to be an int
    return sesh_hrs


def time_calc_mins(session_time_full):
    """
    Calculates the session time in minutes
    :param session_time_full: The variable that was assigned to the result of
    time_calc_full(). Should be a float.
    :return: sesh_mins, short for the session time in minutes minus hours.
    """
    sesh_mins = 0.0
    sesh_mins = (session_time_full % 1) * 60  # Truncates to decimal
    sesh_mins = round(sesh_mins, 2)  # Round it up or down, as the abs function
    sesh_mins = abs(sesh_mins)       # doesn't appear to properly round.
    return sesh_mins


def output(session_time_full, session_time_hrs, session_time_mins):
    """
    Outputs the results to the user
    :param session_time_full: The result of time_calc_full()
    :param session_time_hrs: The result of time_calc_hrs()
    :param session_time_mins: The result of time_calc_mins()
    :return: nothing
    """
    hr_plurality = ""
    min_plurality = ""
    if session_time_full == 1:
        # If the runtime is exactly one hour
        print("This session's time is", int(session_time_hrs), "hour.")
    else:
        if session_time_hrs == 1:
            hr_plurality = "hour"
        else:
            hr_plurality = "hours"
        if session_time_mins == 1:
            min_plurality = "minute."
        else:
            min_plurality = "minutes."

        if hr_plurality == "hours" and session_time_mins == 0:
            # If the runtime is more than one hour and 0 minutes
            print("This session's time is", session_time_hrs, "hours.")
        elif hr_plurality == "hours" and session_time_hrs == 0 and session_time_mins > 1:
            # If the playtime is 0 hours and some-odd minutes
            print("This session's playtime is", session_time_mins, "minutes.")
        else:
            # If the playtime is >1 hours and some-odd minutes
            print("This session's time is", round(session_time_full, 2),
                  " hours, or approximately", int(session_time_hrs),
                  hr_plurality, "and", int(session_time_mins), min_plurality)


def exit_message():
    """This function prints an exit message.
    :return: nothing"""
    print("\nThank you for using this program.")
    print("Have a nice day!")


if __name__ == "__main__":
    main()
