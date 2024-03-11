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

import valid as v


def main():
    food_list = []
    calorie_list = []
    calorie_goal = 0
    more = 'y'
    total_calories = 0
    food_item = ""
    calories = 0

    welcome_message()

    calorie_goal = get_calorie("Enter your daily calorie goal: ")

    while more == 'y':
        food_item = v.get_string("\nEnter food item name: ")
        food_list.append(food_item)
        calories = get_calorie("Enter calories for " + food_item + ": ")
        calorie_list.append(calories)
        more = v.get_y_or_n("Do you have more items to enter (y/n): ")

    print_list(food_list, calorie_list)
    print_results(calorie_goal, calorie_list)
    print("\nGoodbye!")


def calc_total_calories(calorie_list):
    num_sum = 0
    for i in range(len(calorie_list)):
        num_sum = num_sum + calorie_list[i]
    return num_sum


def print_list(food_list, calorie_list):
    print("\n{: <15}{: <8}".format("Item name", "Calories"))
    print("{: <15}{: <8}".format("---------", "--------"))

    for i in range(len(food_list)):
        print("{: <15}{: <8}".format(food_list[i], calorie_list[i]))

    print()


def get_calorie(prompt):
    cal = 0
    while True:
        cal = v.get_integer(prompt)
        if cal >= 0:
            return cal
        else:
            print("Must be positive number.")


def print_results(calorie_goal, calorie_list):
    print_sum = calc_total_calories(calorie_list)

    print("You consumed", print_sum, "calories today.\n")

    if calorie_goal == print_sum:
        print("Congratulations! You met your goal!")
    elif calorie_goal > print_sum:
        print("You were under your goal, look at your list, where can you add calories tomorrow?")
    else:
        print("Keep trying! You were over your goal, look at your list, where can you cut back tomorrow?")


def welcome_message():
    print("Welcome to the Stay Healthy App!")
    print("Enter your calorie goal and then the items and" +
          " calorie amounts \nand I will calculate if you met" +
          " your goal!\n")


main()
