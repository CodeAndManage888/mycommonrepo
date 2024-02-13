#!/bin/bash
#**************************************************************
# Date: 112523 (Expected Solution with 44 Lines of Code)      *
# Title: Does a List contain a Sublist?                       *
# Status: In Progress (In Progress / Testing / Working)       *
# A sublist is a list that makes up part of a larger list. A  *
# sublist may be a list containing a single element, multiple *
# elements, or even no elements at all. For example, [1],     *
# [2],[3] and [4] are all sublists of [1, 2, 3, 4] . The      *
# list [2, 3] is also a sublist of [1, 2, 3, 4], but [2, 4] is*
# not a sublist [1, 2, 3, 4] because the elements 2 and 4 are *
# not adjacent in the longer list. The empty list is a sublist*
# of any list. As a result, [] is a sublist of [1, 2, 3, 4]. A*
# list is a sublist of itself, meaning that [1, 2, 3, 4] is   *
# also a sublist of [1, 2, 3, 4]. In this exercise you will   *
# create a function, is Sublist, that determines whether or   *
# not one list is a sublist of another. Your function should  *
# take two lists, larger and smaller, as its only parameters. *
# It should return True if and only if smaller is a sublist of*
# larger . Write a main program that demonstrates your        * 
# function.                                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def sublist_chk(subl1, subl2):
  if subl1 == subl2 or subl2 == []:
    return True
  elif subl1 == [] and subl2 != []:
    return False
  elif len(subl1) > 1 and len(subl2) > 1:
    if subl1[1] != subl2[1]:
      return False
  elif subl1[0] == subl2[0]:
    return sublist_chk(subl1, subl2[1:])
  elif subl1[0] != subl2[0] and len(subl1) > 1:
    return sublist_chk(subl1[1:], subl2)
#--------------------------------------------------------------
if __name__ == "__main__":
  sublist_in1 = input("Enter a first list of numbers separated by spaces: ")
  sublist_in2 = input("Enter a second list of numbers separated by spaces: ")
  sublist_1 = sublist_in1.split()
  sublist_2 = sublist_in2.split()
  print("List 1: ", sublist_1)
  print("List 2: ", sublist_2)
  if sublist_chk(sublist_1, sublist_2):
    print("List 2 is a sublist of List 1")
  else:
    print("List 2 is not a sublist of List 1")
  print("Thank you for using this app.")
#**************************************************************