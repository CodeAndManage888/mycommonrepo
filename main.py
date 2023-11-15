#!/bin/bash
#**************************************************************
# Date: 111323 (Expected Solution with 41 Lines of Code)      *
# Title: Line of Best Fit                                     *
# Status: In Progress (In Progress / Testing / Working)       *
# A line of best fit is a straight line that best approximates*
# a collection of n data points. In this exercise, we will    *
# assume that each point in the collection has an x coordinate*
# and a y coordinate. The symbols ¯x and ¯y are used to       *
# represent the average x value in the collection and the     *
# average y value in the collection respectively. The line of *
# best fit is represented by the equation y = mx + b where m  *
# and b are calculated using the following formulas:          *
#                                                             *
#                       (summation x) * (summation y)         *
#        summation xy − ----------------------------          *
#                                  n                          *
#   m =  -------------------------------------------          *
#           (summation x**2) − (summation x)**2               *
#                              ----------------               *
#                                     n                       *
#           b = ¯y − m¯x                                      *
#                                                             *
# Write a program that reads a collection of points from the  *
# user. The user will enter the x part of the ﬁrst coordinate *
# on its own line, followed by the y part of the ﬁrst         *
# coordinate on its own line. Allow the user to continue      *
# entering coordinates, with the x and y parts each entered   *
# on their own line, until your program reads a blank line for*
# the x coordinate. Display the formula for the line of best  *
# fit in the form y = mx + b by replacing m and b with the    *
# values you calculated using the preceding formulas. For     *
# example, if the user inputs the coordinates (1,1),(2,2.1)   *
# and (3,2.9) then your program should display y = 0.95x + 0.1*
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def line_best_fit(user_in):
  return
def compute_m(user_in):
  return
def compute_b(user_in):
  fin_val = ave_y - m*ave_x
  return fin_val
#--------------------------------------------------------------
if __name__ == "__main__":
  print("Thank you for using this app.")
#**************************************************************