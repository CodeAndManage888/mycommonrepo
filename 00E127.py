#!/bin/bash
#**************************************************************
# Date: 112823 (Expected Solution with 33 Lines of Code)      *
# Title: The Sieve of Eratosthenes                            *
# Status: In Progress (In Progress / Testing / Working)       *
# The Sieve of Eratosthenes is a technique that was developed *
# more than 2,000 years ago to easily ﬁnd all of the prime    *
# numbers between 2 and some limit, say 100. A description of *
# the algorithm follows: Write down all of the numbers from 0 *
# to the limit Cross out 0 and 1 because they are not prime   *
# Set p equal to 2 While p is less than the limit do Cross out*
# all multiples of p (but not pitself) Set p equal to the next*
# number in the list that is not crossed out Report all of    *
# the numbers that have not been crossed out as prime The key *
# to this algorithm is that it is relatively easy to cross    *
# out every nth number on a piece of paper. This is also an   *
# easy task for a computer a for loop can simulate this       *
# behavior when a third parameter is provided to the range    *
# function. When a number is crossed out, we know that it is  *
# no longer prime, but it still occupies space on the piece   *
# of paper, and must still be considered when computing later *
# prime numbers.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def prime_num_func(user_in):
  all_num_list = []
  prime_num_list = []
  prime_num = 2
  for num in range(user_in):
      all_num_list.append(num)
  print(all_num_list)
  if 0 in all_num_list:
    all_num_list.remove(0)
  if 1 in all_num_list:
    all_num_list.remove(1)
  print(all_num_list)
  while prime_num < user_in:
    for num in all_num_list:
      if num % prime_num == 0 and num != prime_num:
        all_num_list.remove(num)
      else:
        prime_num_list.append(num)
        prime_num = num
  return prime_num_list
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in = input("Enter the number limit: ")
  print("Number Limit: ", int(user_in))
  print("Extracted Prime List: ", prime_num_func(int(user_in)))
  print("Thank you for using this app.")
#**************************************************************