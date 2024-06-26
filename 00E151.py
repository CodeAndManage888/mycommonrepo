#!/bin/bash
#**************************************************************
# Date: 051024 (Expected Solution with 37 Lines of Code)      *
# Title:Two Word Random Password 73                           *
# Status: In Progress (In Progress / Testing / Working)       *
# While generating a password by selecting random characters  *
# generally gives a relatively secure password, it also       *
# generally gives a password that is difﬁcult to memorize. As *
# an alternative, some systems construct a password by taking *
# two English words and concatenating them. While this        *
# password isn’t as secure, it is much easier to memorize.    *
# Write a program that reads a file containing a list of words*
# randomly selects two of them, and concatenates them to      *
# produce a new password. When producing the password ensure  *
# that the total length is between 8 and 10 characters, and   *
# that each word used is at least three letters long.         *
# Capitalize each word in the password so that the user can   *
# easily see where one word ends and the next one begins.     *
# Display the password for the user.                          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
#--------------------------------------------------------------
if __name__ == "__main__":
  input_file = input(str("Please enter the name of the file: "))
  with open(input_file, "r") as worddict:
    word_record = worddict.readlines()
    print(word_record)
    word_list = []
    for idx3, readline in enumerate(word_record):
      word_list += readline.split(" ")
    print(word_list)
    tot_len = len(word_list)
    word_concat, gen_ctr = "", 0
    tot_pair = (tot_len * (tot_len - 1)) / 2
    while len(word_concat) < 10 or len(word_concat) < 8 or gen_ctr > tot_pair :
      rand_idx = random.randint(0, tot_len - 1)
      if len(word_list[rand_idx]) >= 3:
        word_concat += word_list[rand_idx].capitalize()
      rand_idx = random.randint(0, tot_len - 1)
      if len(word_list[rand_idx]) >= 3:
        word_concat += word_list[rand_idx].capitalize()
      gen_ctr += 1
    print(word_concat)
  print("Thank you for using this app.")
#**************************************************************be