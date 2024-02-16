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
# Sources: Lab 6 specifications, previous labs
# *****************************************************************************
#                          Sample Run
# Hello! This program calculates a session length of a program after
# asking the play times of the beginning and end of a working session.
#
# Please enter the game run time at the start of the session: 20.6

# Please enter the run time at the end: 22.5
# This session lasted for 1.9 hours, or roughly 1 hours and 54 minutes.
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
    old_time = 0.0
    new_time = 0.0
    session_time_full = 0.0
    session_time_hrs = 0
    session_time_mins = 0.0
    hr_plurality = ""
    mins_plurality = ""
    full_plurality = False
    cont = "y"
    while cont == CARRY_ON:
        # While cont is equal to CARRY_ON, the program loops. cont can only be
        # set to something else in the proceed function, which is at the end
        # of this loop.

        # Here we greet the user.
        greeting()

        # Gets old_time from the user
        old_time = get_old_time()
        old_time = validate_old_time(old_time)  # Make sure old_time !< 0
        new_time = get_new_time()
        new_time = validate_new_time(new_time, old_time)
        # ^^^ Checks new_time to ensure it's not <=0  or < old_time
        # We could check this to make sure new_time != old_time, but for
        # what I eventually want to expand this into, it is not needed.

        # Calculate our times
        session_time_full = time_calc_full(old_time, new_time)
        session_time_hrs = time_calc_hrs(session_time_full)
        session_time_mins = time_calc_mins(session_time_full)

        # Begin formatting the output
        hr_plurality, mins_plurality = plurality_calc(
            session_time_hrs, session_time_mins)
        # And now we output our output
        output(hr_plurality, mins_plurality, session_time_full,
               session_time_hrs, session_time_mins)

        # "Wanna do it again?"
        cont = proceed()
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
    cont = v.get_y_or_n("\nDo you want to continue? (y/n) ")
    return cont


def get_old_time():
    """
    This function gets the old time from the user
    :return: old, short for old time. Shortened so it doesn't get confused
    with main's old_time variable.
    """
    old = 0.0
    old = v.get_real("\nPlease enter the total game run time "
                     "at the start of the session \n(in decimal "
                     "form): ")
    return old


def get_new_time():
    """
    This function gets the new time from the user
    :return: new, short for new time. Shortened so it doesn't get confused
    with main's new_time variable.
    """
    new = 0.0
    new = v.get_real("Please enter the total game run time "
                     "at the end of the session \n(in decimal "
                     "form): ")
    return new


def validate_old_time(old_time):
    """
    This function checks to make sure old_time isn't negative.
    :param old_time: a float, the first value the user enters
    :return: old_time, a float, only after getting a valid input from the user
    """
    if old_time < 0:
        while old_time < 0:
            print("You cannot have a negative session time. Please try again.")
            old_time = get_old_time()
    return old_time


def validate_new_time(new_time, old_time):
    """
    This function checks the variable new_time to ensure it's not lower than
    old_time or 0, and loops until a valid time is entered.
    :param new_time: a float, the user's new run time.
    :param old_time: a float, the user's old run time
    :return: new time
    """
    while new_time < old_time or new_time <= 0:
        if new_time < 0:
            if new_time < 0:
                print("\nYou cannot have a negative run time. Please try again.")
                new_time = get_new_time()
        else:
            if new_time < old_time or new_time == 0:
                if new_time == 0:
                    print("\nYou cannot have a new session time that's 0. Please try again.")
                    new_time = get_new_time()
                elif new_time < old_time:
                    print("\nYou cannot have a new session time that's less than the old"
                          " session time. Please try again.")
                    new_time = get_new_time()
            else:
                return new_time
    else:
        return new_time


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
    sesh_full = (new_time - old_time)
    # The session time variables are being converted to absolute values in all
    # the time_calc functions to account for the user entering the times in
    # the wrong order.
    # Lab 6: chose to keep this as using the absolute value of the results as
    # it's cleaner than doing one order or another. However, performing one set
    # calculations if new_time is a smaller time than low_time isn't difficult.
    # it's just if new_time < old time: sesh_full = old_time - new_time.
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
    sesh_mins = abs(sesh_mins)  # doesn't appear to properly round.
    return sesh_mins


def plurality_calc(session_time_hrs, session_time_mins):
    """
    This function determines the plurality of the variables and assigns strings
    based on the results.
    :param session_time_hrs: the session time's hours
    :param session_time_mins: the session time's minutes
    :return hr_plural:, a bool storing the plurality of the session hours
    :return min_plural:, a bool storing the plurality of the session minutes
    """
    hr_plural = True
    mins_plural = True
    if session_time_mins <= 1:
        mins_plural = False
    if session_time_hrs <= 1:
        hr_plural = False
    # If either were above 1, we would be setting the variable to true, which
    # they're initialized to.
    return hr_plural, mins_plural


def output(hr_plurality, min_plurality, session_time_full, session_time_hrs,
           session_time_mins):
    """
    Outputs the results to the user
    :param hr_plurality: string, determines if "hours" or "hour" is used
    :param min_plurality: string, determines if "minutes" or "minute" is used
    :param session_time_full: The result of time_calc_full()
    :param session_time_hrs: The result of time_calc_hrs()
    :param session_time_mins: The result of time_calc_mins()
    :return: nothing
    """
    if hr_plurality is False and session_time_mins == 0:
        # If the runtime is exactly one hour, we don't need any other output
        print("This session's run time is", int(session_time_hrs), "hour.")
    else:
        if hr_plurality is True and session_time_mins == 0:
            # If the runtime is more than one hour and 0 minutes
            print("This session's run time is", session_time_hrs, "hours")

        elif hr_plurality is False and session_time_hrs == 0 and min_plurality is True:
            # If the playtime is 0 hours and some-odd minutes
            print("This session's run time is", session_time_mins, "minutes.")

        elif hr_plurality is False and min_plurality is True:
            # If the runtime is 1 hour and some-odd minutes
            print("This session's time is ", session_time_hrs, "hour and",
                  session_time_mins, min_plurality, "minutes.")

        elif hr_plurality is True and min_plurality is True:
            # If the playtime is >1 hours and some-odd minutes
            print("This session's time is", round(session_time_full, 2),
                  " hours, or approximately", int(session_time_hrs),
                  "hours and", int(session_time_mins), "minutes.")


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
