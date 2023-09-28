#!/bin/bash
#**************************************************************
# Date: 082323 (Expected Solution with 61 Lines of Code)      *
# Title: Arbitrary Base Conversions                           *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that allows the user to convert a number    *
# from one base to another. Your program should support bases *
# between 2 and 16 for both the input number and the result   *
# number. If the user chooses a base outside of this range    *
# then an appropriate error message should be displayed and   *
# the program should exit. Divide your program into several   *
# functions, including a function that converts from an       *
# arbitrary base to base 10, a function that converts from    *
# base 10 to an arbitrary base, and a main program that reads *
# the bases and input number from the user. You may ﬁnd your  *
# solutions to Exercises 77, 78 and 98 helpful when           *
# completing this exercise.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
in_list = []
digit_list = []
hex_val = ["A", "B", "C", "D", "E", "F"]
#--------------------------------------------------------------
def conv_dec_anybase(user_in1b, user_in1c):
  err_ind, fin_anybase_val = 0, ""
  if user_in1b >= 2 and user_in1b <= 16:
    for char in user_in1c:
      if char in hex_val:
        print("Input Error: Invalid Decimal Data")
        err_ind = 1
        break
    if err_ind != 1:
      proc_num = int(user_in1c)
      while proc_num != 0:
        BaseDgt = proc_num % int(user_in1b)
        digit_list.append(str(BaseDgt))
        proc_num //= int(user_in1b)
      digit_list.reverse()
      for digit in digit_list:
        fin_anybase_val += digit
      return fin_anybase_val
  else:
    print("Input Error: Invalid target base.")
  
def conv_anybase_dec(user_in2a, user_in2b):
  #reads the starting base
  #checks if it is a valid base then output an error and stop
  #reads the input number
  #check the max char for the base e.g. base 2 max is 1, base 3 max is 2
    #output ane error and stop if out of range for the base
  #process the request if it pass all checks then return the output.
    #starting base will be used for computation instead of creating separate processess
    #base 16 will have a special conversion
   return
#--------------------------------------------------------------
if __name__ == "__main__":
  user_data = input("Start & target base(2 to 16 only) then number e.g. 2 10 10110: ")
  in_list = user_data.split(" ")
  input_one, input_two, input_three = in_list[0], in_list[1], in_list[2]
  if input_two == "10":
    print_out = conv_anybase_dec(int(input_one),input_three)
  else:
    print_out = conv_dec_anybase(int(input_two),input_three)
    print("The converted value of %s to base %s is %s" % (input_three, input_two, print_out))
  print("Thank you for using this app.")
#**************************************************************