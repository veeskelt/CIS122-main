# Author: Vega Skelton
# Version: 1
# Sample Run:
#
# Election 2023
#
# Welcome to the Election calculator.
# Enter the candidates and their votes and this program will calculate the
# results of the election.
#
# Please enter the candidate: Green
# Please enter their votes: 100
# Are there more candidates? ('y' to continue, 'n' to exit): y
#
# Enter candidate name: Red
# Please enter their votes: 34
# Are there more candidates? ('y' to continue, 'n' to exit): y
#
# Enter candidate name: Green
# Please enter their votes: 99
# Are there more candidates? ('y' to continue, 'n' to exit): y
#
# Enter candidate name: Green
# Please enter their votes: 105
# Are there more candidates? ('y' to continue, 'n' to exit): n
#
# Results:
# Candidate           Votes     Vote %
# _____________________________________
# Green               100       29.59%
# Red                 34        10.06%
# Blue                99        29.29%
# Purple              105       31.07%
#
# And the winner is...
# Purple with 105 votes!

import valid as v
import list_mod as l


def main():
    """
    The main function of the program
    :return: none
    """
    cont = "y"
#    candidate_list = ["Green", "Red", "Blue", "Purple"]
#    cand_votes = [100, 34, 99, 105]  # These are debugging lines
    candidate_list = []
    cand_votes = []
    vote_percent = []
    greeting()
    while cont != "n":
        get_candidate(candidate_list)
        get_cand_votes(cand_votes)
        cont = v.get_y_or_n("Are there more candidates? ('y' to continue, 'n' "
                            "to exit): ")

    calc_vote_percent(cand_votes, vote_percent)
    winner_index = winner(cand_votes)
    print_results(candidate_list, cand_votes, vote_percent, winner_index)


def greeting():
    """
    The greeting function.
    :return: nothing
    """
    print("Welcome to the Election calculator.")
    print("Enter the candidates and their votes and this program will calculate"
          "the \nresults of the election.")


def get_candidate(candidate_list):
    """
    Function to get the list of candidates from the user.
    :param candidate_list: a list of the candidates.
    :return: nothing
    """
    candidate_list.append(v.get_string("Please enter the candidate: "))


def get_cand_votes(cand_votes_list):
    """
    Function to get the candidate's votes from the user.
    :param cand_votes_list: a list of the candidate's votes.
    :return:
    """
    votes = 0
    votes = v.get_integer("Please enter their votes: ")
    if votes < 0:
        print("Invalid input.")
        votes = v.get_integer("Please enter their votes: ")
    else:
        cand_votes_list.append(votes)


def calc_vote_percent(cand_votes, vote_percent):
    """
    Function to calculate the percentage of total votes each candidate received.
    :param cand_votes: the list of candidate's votes
    :param vote_percent: the percentage of total votes each candidate received
    :return: nothing
    """
    percent = 0.0
    vote_sum = 0
    vote_sum = l.calc_list_sum(cand_votes)
    for i in range(len(cand_votes)):
        percent = (cand_votes[i] / vote_sum) * 100
        percent = round(percent, 2)
        vote_percent.append(percent)

    return 0


def winner(cand_votes):
    """
    Function to find the index of the first occurrence of the maximum value
    :param cand_votes: a list of values
    :return winner_spot: the index of the candidate with the most votes. In
    actuality, it's the index of the highest vote count, but these are parallel
    lists.
    """
    max_votes = cand_votes[0]
    winner_spot = 0
    for i in range(len(cand_votes)):
        if cand_votes[i] > max_votes:
            max_votes = cand_votes[i]
            winner_spot = i

    return winner_spot


def print_results(candidate_list, cand_votes, vote_percent, winner_index):
    """
    Function to print the results of the election
    :param candidate_list: the list of candidates.
    :param cand_votes: the candidate votes
    :param vote_percent: the percentage of total votes each candidate received
    :param winner_index: the spot of the winner in the cand_votes list
    :return:
    """
    print("Results: ")
    print("{: <20}{: <10}{: <4}".format("Candidate", "Votes", "Vote %"))
    print("_____________________________________")
    for i in range(len(candidate_list)):
        print("{: <20}{: <10}".format(candidate_list[i], cand_votes[i]),
              vote_percent[i], "%", sep="")
    print("\nAnd the winner is...")
    print(candidate_list[winner_index], "with ", cand_votes[winner_index],
          "votes!")


main()
