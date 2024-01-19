#***************************************************************
# Author: Vega Skelton
# Lab: Practice 2
# Date: 1/17/2024
# Description: This program prompts the user for two float
#   numbers: a car's MPG value and the price of gas, and will
#   output the gas cost for 20, 75, and 500 miles, rounded to
#   two decimal places.
# Input: car's fuel efficiency, cost of gas
# Output: cost of gas at 20/75/500 miles
# Sources: Practice 2 specifications; Fuel Cost Calculator at
#  Omni Calculator (helped me work out the math much faster than
#  if I'd been trying it on my own)
#   https://www.omnicalculator.com/everyday-life/fuel-cost
#***************************************************************
#                        *********
# Sample Run
# Hello! This program will calculate fuel costs given your car's
#   average MPG and the cost of fuel.
# Please enter the cost of fuel ($):
# 3.82
# And please enter your car's fuel efficiency, in MPG:
# 28
# For a 20 mile trip, you will pay $2.34
# For a 75 mile trip, you will pay $8.79
# For a 500 mile trip, you will pay $58.57
#***************************************************************

#the greeting and user input
print("Hello! This program will calculate fuel costs given your car's average"
      " MPG and the cost of fuel.")
fuel_cost = input("Please enter the cost of fuel: ")
fuel_cost = float(fuel_cost)
fuel_mpg = input("Please enter the vehicle's fuel efficiency in miles "
                 "per gallon): ")
fuel_mpg = float(fuel_mpg)

#Calculating trip costs:
#20 miles
distance = 20
trip_cost = (distance / fuel_mpg) * fuel_cost
print("A", distance, "mile trip would cost you ${:.2f}".format(trip_cost))

#75 miles
distance = 75
trip_cost = (distance / fuel_mpg) * fuel_cost
print("A", distance, "mile trip would cost you ${:.2f}".format(trip_cost))

#500 miles
distance = 500
trip_cost = (distance / fuel_mpg) * fuel_cost
print("A", distance, "mile trip would cost you ${:.2f}".format(trip_cost))


#***************************************************************
#                           Planning
# Despite being at the end this was written first, I just didn't want
# to have a bunch of comments at the top of the file
# Greeting message
# Prompt the user for input of the cost of fuel (fuel_cost)
# Convert that into a float
# Prompt the user for input on their car's MPG value (fuel_mpg)
# Convert that into a float too
# The trip_formula cost is as follows:
#   trip_cost = (distance / fuel_mpg) * fuel_cost
# distance = 20
# trip_cost = [trip_cost formula for 20 miles]
# Print "A 20 mile trip would cost you ${:.2f}".format(trip_cost)
#
# distance = 75
# trip_cost = [trip_cost formula for 75 miles]
# Print "A 75 mile trip would cost you ${:.2f}".format(trip_cost)
#
# distance = 500
# # trip_cost = [trip_cost formula for 500 miles]
# Print "A 250 mile trip would cost you ${:.2f}".format(trip_cost)
#***************************************************************