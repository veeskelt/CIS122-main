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
    greeting()
    old_time = get_old_time()
    new_time = get_new_time()
    session_time_full = abs(time_calc_full(old_time, new_time))
    session_time_hrs = abs(time_calc_hrs(session_time_full))
    session_time_mins = abs(time_calc_mins(session_time_full))
    output(session_time_full, session_time_hrs, session_time_mins)


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
    :return:
    """
    old = float(input("Please enter the total game run time at the start "
                      "of the session: "))
    return old


def get_new_time():
    """
    This function gets the new time from the user
    :return: new_time
    """
    new_time = float(input("Please enter the total game run time at the end of"
                           " the session: "))
    return new_time


def time_calc_full(old_time, new_time):
    """
    Calculates the true session time
    :param old_time:
    :param new_time:
    :return: sesh_full
    """
    sesh_full = (new_time - old_time)
    return sesh_full


def time_calc_hrs(session_time_full):
    """
    Calculates the session time in hours
    :param session_time_full:
    :return: sesh_hrs
    """
    sesh_hrs = session_time_full // 1  # truncate the decimal
    return sesh_hrs


def time_calc_mins(session_time_full):
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
