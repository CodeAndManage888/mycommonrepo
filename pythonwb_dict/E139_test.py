#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 10 Lines of Code)      *
# Title: Checking for a Winning Card                          *
# Status: Testing (In Progress / Testing / Working)           *
# A winning Bingo card contains a line of 5 numbers that have *
# all been called. Players normally mark the numbers that     *
# have been called by crossing them out or marking them with  *
# a Bingo dauber. In our implementation we will mark that a   *
# number has been called by replacing it with a 0 in the      *
# Bingo card dictionary. Write a function that takes a        *
# dictionary representing a Bingo card as its only parameter. *
# If the card contains a line of ﬁve zeros (vertical,         *
# horizontal or diagonal) then your function should return    *
# True , indicating that the card has won. Otherwise the      *
# function should return False . Create a main program that   *
# demonstrates your function by creating several Bingo cards, *
# displaying them, and indicating whether or not they contain *
# a winning line. You should demonstrate your function with   *
# at least one card with a horizontal line, at least one card *
# with a vertical line, at least one card with a diagonal     *
# line, and at least one card that has some numbers crossed   *
# out but does not contain a winning line. You will probably  *
# want to import your solution to Exercise 138 when           *
# completing this exercise. Hint: Because there are no        *
# negative numbers on a Bingo card, ﬁnding a line of 5 zeros  *
# is the same problem as ﬁnding a line of 5 entries that sum  *
# to zero. You may ﬁnd the summation problem easier to solve. *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def bingo_card_gen():
  import random
  bingo_card = {}
  bingo_card["B"] = random.sample(range(1,16),5)
  bingo_card["I"] = random.sample(range(16,31),5)
  bingo_card["N"] = random.sample(range(31,46),5)
  bingo_card["G"] = random.sample(range(46,61),5)
  bingo_card["O"] = random.sample(range(61,76),5)
  return bingo_card

def bingo_card_check(bingo_card):
  if bingo_card["B"][0] + bingo_card["I"][1] + bingo_card["N"][2] + bingo_card["G"][3] + bingo_card["O"][4] == 0:
    return True
  elif bingo_card["B"][4] + bingo_card["I"][3] + bingo_card["N"][2] + bingo_card["G"][1] + bingo_card["O"][0] == 0:
    return True
  elif bingo_card["B"][0] + bingo_card["B"][1] + bingo_card[ "B"][2] + bingo_card["B"][3] + bingo_card["B"][4] == 0:
    return True
  elif bingo_card["I"][0] + bingo_card["I"][1] + bingo_card["I"][2] + bingo_card["I"][3] + bingo_card["I"][4] == 0:
    return True
  elif bingo_card["N"][0] + bingo_card["N"][1] + bingo_card["N"][2] + bingo_card["N"][3] + bingo_card["N"][4] == 0:
    return True
  elif bingo_card["G"][0] + bingo_card["G"][1] + bingo_card["G"][2] + bingo_card["G"][3] + bingo_card["G"][4] == 0:
    return True
  elif bingo_card["O"][0] + bingo_card["O"][1] + bingo_card[ "O"][2] + bingo_card["O"][3] + bingo_card["O"][4] == 0:
    return True
  elif bingo_card["B"][0] + bingo_card["I"][0] + bingo_card["N"][0] + bingo_card["G"][0] + bingo_card["O"][0] == 0:
    return True
  elif bingo_card["B"][1] + bingo_card["I"][1] + bingo_card["N"][1] + bingo_card["G"][1] + bingo_card["O"][1] == 0:
   return True
  elif bingo_card["B"][2] + bingo_card["I"][2] + bingo_card["N"][2] + bingo_card["G"][2] + bingo_card["O"][2] == 0:
   return True
  elif bingo_card["B"][3] + bingo_card["I"][3] + bingo_card["N"][3] + bingo_card["G"][3] + bingo_card["O"][3] == 0:
   return True
  elif bingo_card["B"][4] + bingo_card["I"][4] + bingo_card["N"][4] + bingo_card["G"][4] + bingo_card["O"][4] == 0:
   return True
  else:
   return False
#--------------------------------------------------------------
if __name__ == "__main__":
  bingo_card = bingo_card_gen()
  print(bingo_card)
  print("B\tI\tN\tG\tO")
  for i in range(5):
    print(bingo_card["B"][i],"\t",bingo_card["I"][i],"\t",bingo_card["N"][i],"\t",bingo_card["G"][i],"\t",bingo_card["O"][i])
  #------------------------------------------------------------
  # Number Update:
  #------------------------------------------------------------
  user_input = input("Enter a list number: ")
  user_list = user_input.split()
  print(user_list)
  for n in user_list:
    print(n)
    if int(n) in bingo_card["B"]:
      bingo_card["B"][bingo_card["B"].index(int(n))] = 0
    elif int(n) in bingo_card["I"]:
      bingo_card["I"][bingo_card["I"].index(int(n))] = 0
    elif int(n) in bingo_card["N"]:
      bingo_card["N"][bingo_card["N"].index(int(n))] = 0
    elif int(n) in bingo_card["G"]:
      bingo_card["G"][bingo_card["G"].index(int(n))] = 0
    elif int(n) in bingo_card["O"]:
      bingo_card["O"][bingo_card["O"].index(int(n))] = 0
    else:
      print("Invalid number.")
  #------------------------------------------------------------
  # Print the updated Bingo card:
  #------------------------------------------------------------
  print("B\tI\tN\tG\tO")
  for i in range(5):
    print(bingo_card["B"][i],"\t",bingo_card["I"][i],"\t",bingo_card["N"][i],"\t",bingo_card["G"][i],"\t",bingo_card["O"][i])
  #------------------------------------------------------------
  # Check for a winning line:
  #------------------------------------------------------------
  if bingo_card_check(bingo_card) == False:
    print("No winning line.")
  else:
    print("Winning line!")
  print("Thank you for using this app.")
#**************************************************************