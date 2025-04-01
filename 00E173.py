#!/bin/bash
#**************************************************************
# Date: 091324 (Expected Solution with 33 Lines of Code)      *
# Title: Run-Length Decoding                                  *
# Status: In Progress (In Progress / Testing / Working)       *
#  Run-length encoding is a simple data compression technique *
# that can be effective when repeated values occur at         *
# adjacent positions within a list. Compression is achieved by*
# replacing groups of repeated values with one copy of the    *
# value, followed by the number of times that the value       *
# should be repeated. For example, the list ["A",             *
# "A","A","A","A","A","A","A","A","A","A","A","B","B", "B",   *
# "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed *
# as["A", 12, "B", 4, "A", 6, "B", 1] . Decompression is      *
# performed by replicating each value in the list the number  *
# of times indicated. Write a recursive function that         *
# decompresses a run-length encoded list. Your recursive      *
# function will take a run-length compressed list as its only *
# parameter. It will return the decompressed list as its only *
# result. Create a main program that displays a run-length    *
# encoded list and the result of decoding it.                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def decode_func(user_list):
  if len(user_list) == 0:
    return []
  else:
    if user_list[0] == user_list[1]:
      return [user_list[0]] + [user_list[1]] + decode_func(user_list[2:])
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
  print("The encoded list is", encoded_list)
  print("The decoded list is", decode_func(encoded_list))
  print("Thank you for using this app.")
#**************************************************************
