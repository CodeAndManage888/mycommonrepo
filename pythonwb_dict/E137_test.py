#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 18 Lines of Code)      *
# Title: Scrabble™ Score                                      *
# Status: Testing (In Progress / Testing / Working)           *
# In the game of Scrabble™, each letter has points associated *
# with it. The total score of a word is the sum of the scores *
# of its letters. More common letters are worth fewer points  *
# while less common letters are worth more points. The points *
# associated with each letter are shown below: One point A,   *
# E, I, L, N, O, R, S, T and U Two points D and G Three       *
# points B, C, M and P Four points F, H, V, W and Y Five      *
# points K Eight points J and X Ten points Q and Z Write a    *
# program that computes and displays the Scrabble™ score for  *
# a word. Create a dictionary that maps from letters to point *
# values. Then use the dictionary to compute the score. A     *
# Scrabble™ board includes some squares that multiply the     *
# value of a letter or the value of an entire word. We will   *
# ignore these squares in this exercise.                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def comp_points(user_str):
  point_dict = {"A":1, "E":1, "I":1, "L":1, "N":1, "O":1, "R":1, 
                "S":1, "T":1, "U":1, "D":2, "G":2, "B":3, "C":3, 
                "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, 
                "K":5, "J":8, "X" :8, "Q":10, "Z":10}
  points = 0
  for i in user_str:
    points += point_dict[i]
  return points
#--------------------------------------------------------------
if __name__ == "__main__":
  user_str = input("Enter a word: ")
  print("The Scrabble™ score for the word", user_str, "is", comp_points(user_str.upper()))
  print("Thank you for using this app.")
#**************************************************************
