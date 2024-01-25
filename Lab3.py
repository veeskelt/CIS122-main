# *****************************************************************************
# Author: Vega Skelton
# Lab: Lab 2
# Date: 1/24/2024
# Description: Example: This program prompts the user for the
#   playtime of a yet unspecified game before and after a session
#   after a session and output the session time in hours and
#   minutes (rounded).
# Input: old play time, new play time
# Output: simple session time, session time in hours,
#   session time in minutes
# Sources: Lab 2 specifications and any other substantial
# aids, like web pages
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
    greeting()
    old_time = get_old_time()
    new_time = get_new_time()
    session_time_full = abs(time_calc_full(old_time, new_time))
    session_time_hrs = abs(time_calc_hrs(session_time_full))
    session_time_mins = abs(time_calc_mins(session_time_full))
    output(session_time_full, session_time_hrs, session_time_mins)
    # the variables being assigned the output of the calc functions are
    # converted to the absolute values of the outputs to account for
    # the user entering the numbers in the wrong order, as I have
    # done many times while testing already.


def greeting():
    """
    This function displays a greeting
    :return: nothing
    """
    print("Hello! This program calculates a session length of a game after "
          "asking for the play times of the beginning and end of a gaming "
          "session.")


def get_old_time():
    """
    This function gets the old time from the user
    :return: old, short for old time. shortened so it doesn't get confused
    with main's old_time variable.
    """
    old = float(input("Please enter the total game run time at the start "
                      "of the session: "))
    return old


def get_new_time():
    """
    This function gets the new time from the user
    :return: new, short for new time. shortened so it doesn't get confused
    with main's new_time variable.
    """
    new = float(input("Please enter the total game run time at the end of"
                      " the session: "))
    return new


def time_calc_full(old_time, new_time):
    """
    Calculates the true session time
    :param old_time: one of two times the program works with. should be, but
    doesn't have to be, the lower of the two times. This value should be
    obtained from the user or a file.
    :param new_time: one of two times the program works with. should be, but
    doesn't have to be, the higher of the two times. This value should be
    obtained from the user or a file.
    :return: sesh_full, short for session_full.
    """
    sesh_full = (new_time - old_time)
    return sesh_full


def time_calc_hrs(session_time_full):
    """
    Calculates the session time in hours
    :param session_time_full: the variable that was assigned to the result of
    time_calc_full(). Should be a float.
    :return: sesh_hrs, short for session_hours
    """
    sesh_hrs = session_time_full // 1  # truncate the decimal
    return sesh_hrs


def time_calc_mins(session_time_full):
    """
    Calculates the session time in minutes
    :param session_time_full: the variable that was assigned to the result of
    time_calc_full(). Should be a float.
    :return: sesh_mins, short for session_minutes.
    """
    sesh_mins = (session_time_full % 1) * 60  # truncate to decimal
    return sesh_mins


def output(session_time_full, session_time_hrs, session_time_mins):
    """
    Outputs the results to the user
    :param session_time_full:
    :param session_time_hrs:
    :param session_time_mins:
    :return: nothing
    """
    print("This session's playtime is {:.1f} hours, or approximately {:.0f} "
          "hours and {:.0f} minutes.".format(session_time_full,
                                             session_time_hrs,
                                             session_time_mins))


main()
