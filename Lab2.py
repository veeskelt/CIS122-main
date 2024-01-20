#***************************************************************
# Author: Vega Skelton
# Lab: Lab 2
# Date: 1/16/2024
# Description: Example: This program prompts the user for the
#   playtime of a yet unspecified game before and after a session
#   after a session and output the session time in hours and
#   minutes (rounded).
# Input: old play time, new play time
# Output: simple session time, session time in hours,
#   session time in minutes
# Sources: Lab 2 specifications and any other substantial
# aids, like web pages
#***************************************************************
#                          Sample Run
# Hello! This program calculates a session length of a game after
#   asking the play times of the beginning and end of a gaming
#   session.
# Please enter the game run time at the start of the session: 20.6
# Please enter the run time at the end: 22.5
# This session lasted for 1.9 hours, or roughly 1 hours and 54 minutes.
#***************************************************************

# Greeting and user input
print("Hello! This program calculates a session length of a game after asking"
      "for the play times of the beginning and end of a gaming session.")
old_time = float(input("Please enter the total game run time at the start of "
               "the session: "))
#print(type(old_time))
new_time = float(input("Please enter the total game run time at the end of the"
               " session: "))
#print(type(new_time))

# The math part
session_time_simple = (new_time - old_time)
session_time_hrs = session_time_simple // 1         # truncate the decimal
session_time_mins = (session_time_simple % 1) * 60  # truncate to the decimal

# Output
print("This session's playtime is {:.1f} hours, or approximately {:.0f} "
      "hours and {:.0f} minutes.".format(session_time_simple,
                                         session_time_hrs, session_time_mins))
#the above is how pycharm wrapped this line, idk it reads fine to me

#***************************************************************
#                           Planning
# Greeting
# Prompt the user for starting session time (old_time)
# convert that into a float
# Prompt the user for ending session time (new_time)
# convert that into a float
#
# session_time_simple is just new_time - old time
# session_time_hrs is session_time_simple // 1, to truncate the decimal
# session_time_mins is (session_time_simple % 1) * 60, to isolate the playtime
#   minutes. keeping session_time_mins as a float allows us to keep track of it
#   for more precise math later, if needed. Also lets me use the format string
#   function.
# Output: This session's playtime is 1.9 hours, or approximately 1 hours and 54 minutes
# can't use if/then/else statements to check for values of 0 or 1, so "1 hours"
# gets to stay for now.
#***************************************************************