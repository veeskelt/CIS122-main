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

#prelim testing to make sure i understand integer division and modulus, remove later
num1 = 1.92
print(num1)
num2 = num1 // 1
num2 = int(num2)
print(num2)
num3 = (num1 % 1) * 60
print("approximately {:.0f} minutes".format(num3))


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