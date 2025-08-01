#!/bin/bash
#**************************************************************
# Date: 082424 (Expected Solution with 36 Lines of Code)      *
# Title: Run-Length Encoding                                  *
# Status: In Progress (In Progress / Testing / Working)       *
#  Write a recursive function that implements the run-length  *
# compression technique described in Exercise 173. Your       *
# function will take a list or a string as its only para-     *
# meter. It should return the run-length compressed list as   *
# its only result. Include a main program that reads a string *
# from the user, compresses it, and displays the run-length   *
# encoded result. Hint: You may want to include a loop inside *
# the body of your recursive function.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#---- Auto Generated by ChatGPT ------------------------------
def run_length_encode(data):
  # Base case: if the data is empty, return an empty list
  if not data:
      return []

  # Initialize count
  count = 1
  # Loop to count how many times the first character repeats
  for i in range(1, len(data)):
      if data[i] == data[0]:
          count += 1
      else:
          break

  # Recursive call on the rest of the list/string
  return [(data[0], count)] + run_length_encode(data[count:])

def main():
  user_input = input("Enter a string to compress using run-length encoding: ")
  result = run_length_encode(user_input)
  print("Run-length encoded result:", result)

if __name__ == "__main__":
  main()