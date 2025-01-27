#!/bin/bash
#**************************************************************
# Date: 080324 (Expected Solution with 42 Lines of Code)      *
# Title: String Edit Distance                                 *
# Status: In Progress (In Progress / Testing / Working)       *
#  The edit distance between two strings is a measure of      *
# their similarity—the smaller the edit distance, the more    *
# similar the strings are with regard to the minimum number   *
# of insert, delete and substitute operations needed to       *
# transform one string into the other. Consider the strings   *
# kitten and sitting . The first string can be transformed    *
# into the second string with the following operations:       *
# Substitute the k with an s, substitute the e with an i, and *
# insert a g at the end of the string. This is the smallest   *
# number of operations that can be performed to               *
# transform kitten into sitting. As a result, the edit        *
# distance is 3.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def edit_dist(str1, str2):
  if len(str1) == 0:
    return len(str2)
  elif len(str2) == 0:
    return len(str1)
  else:
    if str1[0] == str2[0]:
      return edit_dist(str1[1:], str2[1:])
    else:
      return 1 + min(edit_dist(str1, str2[1:]), edit_dist(str1[1:], str2), edit_dist(str1[1:], str2[1:]))
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in1 = input("Enter the first string: ")
  user_in2 = input("Enter the second string: ")
  print("The edit distance between the two strings is: " + str(edit_dist(user_in1, user_in2)))
  print("Thank you for using this app.")
#**************************************************************
