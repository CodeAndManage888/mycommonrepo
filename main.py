#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 88 Lines of Code)      *
# Title: Play Bingo                                           *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise you will write a program that simulates a  *
# game of Bingo for a single card. Begin by generating a list *
# of all of the valid Bingo calls (B1 through O75). Once the  *
# list has been created you can randomize the order of its    *
# elements by calling the shuffle function in the random      *
# module. Then your program should consume calls out of the   *
# list, crossing out numbers on the card, until the card      *
# contains a crossed out line (horizontal, vertical or        *
# diagonal). Simulate 1,000 games and report the minimum,     *
# maximum and average number of calls that must be made       *
# before the card wins. Import your solutions to Exercises    *
# 138 and 139 when completing this exercise allow us to work  *
# with data, without needing to enter it each time our program*
# runs. Files also allow us to store results from our program *
# in a more permanent manner. These features are often used   *
# when creating larger programs. When completing the exercises*
# in this chapter, you should expect to: Open a ﬁle for      *
# reading and/or writing Read data from a ﬁle Write data to *
# a new ﬁle Use values provided to the program as command    *
# line parameters Detect and recover from errors such as      *
# attempting to open a ﬁle that doesn’t exist Detect and     *
# recover from other errors that are not speciﬁcally related  *
# to ﬁles Some of the exercises in this chapter involve       *
# reading from existing ﬁles such as a list of words, names or*
# chemical elements. You can download these ﬁles from the     *
# author’s website:                                           *
# http://www.cpsc.ucalgary.ca/~bdstephe/PythonWorkbook .      *
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
