#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 26 Lines of Code)    *
# Title: Maximum Integer                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# This exercise examines the process of identifying the       *
# maximum value in a collection of integers. Each of the      *
# integers will be randomly selected from the numbers between *
# 1 and 100. The collection of integers may contain duplicate *
# values, and some of the integers between 1 and 100 may not  *
# be present.                                                 * 
# Take a moment and think about how you would handle this     *
# problem on paper. Many people would check each integer in   *
# sequence and ask themself if the number that they are       *
# currently considering is larger than the largest number     *
# that they have seen previously, If it is, then they forget  *
# the previous maximum number and remember the current number *
# as the new maximum number. This is a reasonable approach,   *
# and will result in the correct answer when the process is   *
# performed carefully, If you were performing this task, how  *
# many times would you expect to need to update the maximum   *
# value and remember a new number?                            *
# While we can answer the question posed at the end of the    *
# previous paragraph using probability theory, we are going   *
# to explore it by simulating the situation. Create a program *
# that begins by selecting a random integer between 1 and 100.*
# Save this integer as the maximum number encountered so far. *
# After the intial integer has been selected, generate 99     *
# additional random integers between 1 and 100. Check each    *
# integer as it is generated to see if it is larger than the  *
# maximum number encountered so far. If it is then your       *
# program should update the maximum number encountered and    *
# count the fact that you performed an update. Display each   *
# integer after you generate it. Include a notation with those*
# integers which represent a new maximum.                     *
# After you have dispalyed 100 integers your program should   *
# display the maximum value encountered, along with the       *
# number of times the maximum value was updated during the    *
# process. Partial output for the program is shown below      *
# with... representing the remaining integers that your       *
# program will display. Run your program several times. Is    *
# the number of updates performed on the maximum value what   *
# you expected?                                               *
# 30                                                          *
# 74 <== update                                               *
# 58                                                          *
# 17                                                          *
# 40                                                          *
# 37                                                          *
# 13                                                          *
# 34                                                          *
# 46                                                          *
# 52                                                          *
# 80 <== update                                               *
# 37                                                          *
# 97 <== update                                               *
# 45                                                          *
# 55                                                          *
# 73                                                          *
# . . .                                                       *
# The maximum value from was 100                             *
# The maximum value was updated 5 times                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************