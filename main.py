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
user_x, user_y = " ", " "
xy_coordinate = []
#--------------------------------------------------------------
def line_best_fit(user_lst):
  ctr, sum_x, sum_y, sum_xy, sum_x_squared, = 0, 0, 0, 0, 0
  while ctr <= len(user_lst) - 1:
    sum_x += float(user_lst[ctr])
    sum_x_squared += float(user_lst[ctr]) ** 2
    sum_y += float(user_lst[ctr + 1])
    sum_xy += float(user_lst[ctr]) * float(user_lst[ctr + 1])
    ctr += 2
  num_data_pts = len(user_lst) / 2
  comp_m_val = (sum_xy - (sum_x * sum_y) / num_data_pts) / (sum_x_squared - ((sum_x ** 2) / num_data_pts))
  comp_b_val = (sum_y/num_data_pts) - (comp_m_val * (sum_x/num_data_pts))
  return comp_m_val, comp_b_val
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_x != "":
    user_x = input("Enter x coordinates: ")
    if user_x != "" and float(user_x) >= 0:
      xy_coordinate.append(user_x)
      while user_y == "" or user_y == " ":
        user_y = input("Enter y coordinates: ")
      xy_coordinate.append(user_y)
      user_x, user_y = " ", " "
  print(xy_coordinate)
  fin_m_val, fin_b_val = line_best_fit(xy_coordinate)
  print(f"y = {fin_m_val:.2f}x + {fin_b_val:.2f}")
  print("Thank you for using this app.")
#**************************************************************