#!/bin/bash
#**************************************************************
# Date: 081523 (Expected Solution with 33 Lines of Code)      *
# Title: Random Password                                      *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function that generates a random password. The      *
# password should have a random length of between 7 and 10    *
# characters. Each character should be randomly selected from *
# positions 33 to 126 in the ASCII table. Your function will  *
# not take any parameters. It will return the randomly        *
# generated password as its only result. Display the randomly *
# generated password in your file’s main program. Your main   *
# program should only run when your solution has not been     *
# imported into another ﬁle. Hint: You will probably ﬁnd the  *
# chr function helpful when completing this exercise.         *
# Detailed information about this function is available       *
# online.                                                     *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
#--------------------------------------------------------------
def ran_password():
  final_value = ""
  ctr = random.randint(8, 10)
  while ctr != 0:
    final_value += chr(random.randint(33, 126))
    ctr -= 1
  return final_value
#--------------------------------------------------------------
if __name__ == "__main__":
  print("The generated password is", ran_password())
  print("Thank you for using this app.")
#**************************************************************