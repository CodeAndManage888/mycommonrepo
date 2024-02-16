#!/bin/bash
#**************************************************************
# Date: 112623 (Expected Solution with 40 Lines of Code)      *
# Title: Generate All Sublists of a List                      *
# Status: In Progress (In Progress / Testing / Working)       *
# Using the deﬁnition of a sublist from Exercise 125, write a *
# function that returns a list containing every possible      *
# sublist of a list. For example, the sublists of [1, 2, 3]   *
# are[],[1],[2],[3],[1, 2] ,[2, 3] and [1, 2, 3] . Note that  *
# your function will always return a list containing at       *
# least the empty list because the empty list is a sublist of *
# every list. Include a main program that demonstrate your    *
# function by displaying all of the sublists of several       *
# different lists.                                            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def extract_sublst(olist):
  nlist = []
  ilist = []
  glist = []
  ctrgrp_rng, ctr = 0, 0
  while ctrgrp_rng <= len(olist) - 2:
    glist.append(ctrgrp_rng)
    ctrgrp_rng += 1
  print(glist)
  for g in glist:
    if g == 0:
      nlist.append(ilist)
    else:
      while ctr < len(olist) - 1:
        ilist.append(olist[ctr])
        ctr += g
        nlist.append(ilist)
        ilist = []
  return nlist
#--------------------------------------------------------------
if __name__ == "__main__":
  sublist_in = input("Enter a first list of numbers separated by spaces: ")
  sublist = sublist_in.split()
  print(extract_sublst(sublist))
  print("Original List: ", sublist)
  print("Thank you for using this app.")
#**************************************************************