#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 10 Lines of Code)      *
# Title: Checking for a Winning Card                          *
# Status: In Progress (In Progress / Testing / Working)       *
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
def chck_bingo_card(user_in):
  if user_in[0][0] == 0 and user_in[1][0] == 0 and user_in[2][0] == 0 and user_in[3][0] == 0 and user_in[4][0] == 0:
    return True
  elif user_in[0][1] == 0 and user_in[1][1] == 0 and user_in[2][1] == 0 and user_in[3][1] == 0 and user_in[4][1] == 0:
    return True
  elif user_in[0][2] == 0 and user_in[1][2] == 0 and user_in[2][2] == 0 and user_in[3][2] == 0 and user_in[4][2] == 0:
    return True
  elif user_in[0][3] == 0 and user_in[1][3] == 0 and user_in[2][3] == 0 and user_in[3][3] == 0 and user_in[4][3] == 0:
    return True
  elif user_in[0][4] == 0 and user_in[1][4] == 0 and user_in[2][4] == 0 and user_in[3][4] == 0 and user_in[4][4] == 0:
    return True
  elif user_in[0][0] == 0 and user_in[1][1] == 0 and user_in[2][2] == 0 and user_in[3][3] == 0 and user_in[4][4] == 0:
    return True
  elif user_in[0][4] == 0 and user_in[1][3] == 0 and user_in[2][2] == 0 and user_in[3][1] == 0 and user_in[4][0] == 0:
    return True
  else:
    return False
#--------------------------------------------------------------
if __name__ == "__main__":
  chck_bingo_card([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
  chck_bingo_card([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
  chck_bingo_card([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
  chck_bingo_card([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
  chck_bingo_card([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
  print("Thank you for using this app.")
#**************************************************************
