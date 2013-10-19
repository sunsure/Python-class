#! /usr/bin/python
# code for mini-project 1
# author: cc
# class: CS-PY-Rice
# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error"
    # else is optional and for this MP unnecessary
    # still it is good coding practice to include
    # a last "catch-all" statement
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return 10

def rpsls(player_name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(player_name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5

    # use if/elif/else to determine winner
    if (result == 1) or (result == 2):
        is_winner = "Player"
    elif (result == 3) or (result == 4):
        is_winner = "Computer"
    else:
        is_winner = "tie"
        
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # print results
    print "Player chooses", player_name
    print "Computer chooses", comp_name
    # uncomment the three lines below to show additional debug info
    #print "_test_ Player chooses", player_name, "(", player_number, ")"
    #print "_test_ Computer chooses", comp_name, "(", comp_number, ")"
    #print "_test_ Result =", result
    # end of debug info
    if (is_winner == "Player") or (is_winner == "Computer"):
        print is_winner, "wins!"
    else:
        print "Player and computer " + is_winner + "!"
    print
    
# uncomment to test code
#print "0 =", number_to_name(0)
#print "1 =", number_to_name(1)
#print "2 =", number_to_name(2)
#print "3 =", number_to_name(3)
#print "4 =", number_to_name(4)
#print "-1 =", number_to_name(-1)
#print "5 =", number_to_name(5)
#print "==="
#print "rock =", name_to_number("rock")
#print "Spock =", name_to_number("Spock")
#print "paper =", name_to_number("paper")
#print "lizard =", name_to_number("lizard")
#print "scissors =", name_to_number("scissors")
#print "Joe =", name_to_number("Joe")
#print "==="
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
