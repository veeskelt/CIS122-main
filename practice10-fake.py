# Problem: Create a program to prompt a user for their daily calorie intake
# goal and a list of food items and calories eaten in a day. The program will
# then print the list of items and calories, sum the total calories consumed,
# and print a message if they met or were over or under their goal.
#
# Algorithm steps:
#     Define variables to store daily calorie goal and a list for food item
#       names and another list for calories for each item.
#     Prompt for and input the daily calorie goal.
#     Loop and ask the user to enter the item eaten and the calorie amount.
#       Continue to ask until the user is done.
#     Print out the lists of items and calories.
#     Calculate the sum of calories.
#     If the sum is equal to the goal, print a message. "You met your goal".
#       If the sum is less than the goal, print the message "Great job! You
#       were under your goal.", if the sum is over the goal, print the message
#       "Uh oh! You ate more than your goal, look at the list and see where you
#       can do better tomorrow!"

# https://online.pcc.edu/d2l/le/content/508474/viewContent/11050239/View

# Welcome to the Stay Healthy App!
# Enter your calorie goal and then the items and calorie amounts
# and I will calculate if you met your goal!
#
# Enter your daily calorie goal: 2000
#
# 1. Add Food
# 2. List Foods
# 3. Done adding foods
#
# Please enter your choice: 1
#
# Please enter the food name: Cereal
# Please enter the calories in Cereal: 150
#
# List of Foods:
#
# Food           Calories
# Cereal         150
#
# 1. Add Food
# 2. List Foods
# 3. Done adding foods
#
# Please enter your choice: 1
#
# Please enter the food name: Apple (3)
# Please enter the calories in Apple (3): 60
#
# List of Foods:
#
# Food           Calories
# Cereal         150
# Apple (3)      60
#
# 1. Add Food
# 2. List Foods
# 3. Done adding foods
#
# Please enter your choice: 1
#
# Please enter the food name: Sandwhich (2)
# Please enter the calories in Sandwhich (2): 270
#
# List of Foods:
#
# Food           Calories
# Cereal         150
# Apple (3)      60
# Sandwhich (2)  270
#
# 1. Add Food
# 2. List Foods
# 3. Done adding foods
#
# Please enter your choice: 1
#
# Please enter the food name: Donut (3)
# Please enter the calories in Donut (3): 750
#
# List of Foods:
#
# Food           Calories
# Cereal         150
# Apple (3)      60
# Sandwhich (2)  270
# Donut (3)      750
#
# 1. Add Food
# 2. List Foods
# 3. Done adding foods
#
# Please enter your choice: 3
#
# List of Foods:
#
# Food           Calories
# Cereal         150
# Apple (3)      60
# Sandwhich (2)  270
# Donut (3)      750
#
# Total calories: 1230 calories
# Calorie goal: 2000 calories
#
# You did not meet your calorie goal. Maybe eat more tomorrow?
# Goodbye!

import valid as v


class Food:
    __name: ""  # Double underscores indicate that this is a private variable
    __calories: 0

    def __init__(self, name, calories):
        # A dunder method that creates a new object with the supplied fields
        # when a new object of this type is created
        # Likewise, self is an instanced variable that says "hey we're doing things to this"
        self.__name = name
        self.__calories = calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

    def set_name(self, name):
        self.__name = name

    def set_calories(self, calories):
        self.__calories = calories

    def __str__(self):  # A dunder method that, when print(object_instance) is called, runs this function instead
        printed_string = ""
        printed_string = "Food Name: " + self.__name + "" + "Calories: " + str(self.__calories)
        return printed_string


QUIT = 3


def main():
    # empty
    choice = 0
    foods = []
    calorie_goal = 0
    more = "y"
    total_calories = 0

    greeting()
    calorie_goal = get_calorie("Enter your daily calorie goal: ")
    while choice != QUIT:
        print_menu()
        choice = get_choice()
        if choice == 1:
            add_food(foods)
        elif choice == 2:
            list_food(foods)

        list_food(foods)
    total_calories = sum_calories(foods)
    compare_calories(total_calories, calorie_goal)
    print("Goodbye!")


def add_food(foods):
    food_name = ""
    food_calories = 0
    food_name = v.get_string("\nPlease enter the food name: ")
    prompt = ("Please enter the calories in " + food_name + ": ")
    food_calories = v.get_integer(prompt)
    if food_calories < 0:
        print("Invalid input, calories must be greater than or equal to 0.")
        food_calories = v.get_integer(prompt)
    foods.append(Food(food_name, food_calories))


def print_menu():
    print("\n1. Add Food")
    print("2. List Foods")
    print("3. Done adding foods\n")


def get_choice():
    choice = 0
    choice = v.get_integer("Please enter your choice: ")
    while choice < 1 or choice > 3:
        print("Invalid choice.")
        choice = v.get_integer("Please enter your choice: ")
    return choice


def list_food(foods):
    print("\nList of Foods:\n")
    print("{: <15}{: <5}".format("Food", "Calories"))
    for i in range(len(foods)):
        print("{: <15}{: <5}".format(foods[i].get_name(),
                                     foods[i].get_calories()))


def get_calorie(prompt):
    cal = 0
    while True:
        cal = v.get_integer(prompt)
        if cal >= 0:
            return cal
        else:
            print("Must be positive number.")


def sum_calories(foods):
    total_sum = 0
    for i in range(len(foods)):
        total_sum = total_sum + foods[i].get_calories()
    return total_sum


def compare_calories(total, goal):
    print("\nTotal calories:", total, "calories")
    print("Calorie goal:", goal, "calories")
    if total > goal:
        print("\nYou passed your calorie goal. Is there something you can "
              "go without tomorrow?")
    elif total < goal:
        print("\nYou did not meet your calorie goal. Maybe eat more tomorrow?")
    elif total == goal:
        print("\nCongratulations, you hit your calorie goal!")


def greeting():
    print("Welcome to the Stay Healthy App!")
    print("Enter your calorie goal and then the items and" +
          " calorie amounts \nand I will calculate if you met" +
          " your goal!\n")


if __name__ == "__main__":
    main()
