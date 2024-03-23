#!/bin/bash
#**************************************************************
# Date: 030124 (Expected Solution with 24 Lines of Code)      *
# Title: Postal Codes                                         *
# Status: In Progress (In Progress / Testing / Working)       *
# In a Canadian postal code, the ﬁrst, third and ﬁfth         *
# characters are letters while the second, fourth and sixth   *
# characters are numbers. The province can be determined from *
# the ﬁrst character of a postal code, as shown in the        *
# following table. No valid postal codes currently begin with *
# D, F, I, O, Q, U, W, or Z. Province First character(s)      *
# Newfoundland A Nova Scotia B Prince Edward Island C New     *
# Brunswick E Quebec G, H and J Ontario K, L, M, N and P      *
# Manitoba R Saskatchewan S Alberta T British Columbia V      *
# Nunavut X Northwest Territories X Yukon Y The second        *
# character in a postal code identiﬁes whether the address is *
# rural or urban. If that character is a 0 then the address   *
# is rural. Otherwise it is urban. Create a program that      *
# reads a postal code from the user and displays the province *
# associated with it, along with whether the address is urban *
# or rural. For example, if the user enters T2N 1N4 then your *
# program should indicate that the postal code is for an      *
# urban address in Alberta. If the user enters X0A 1B2 then   *
# your program should indicate that the postal code is for a  *
# rural address in Nunavut or Northwest Territories. Use a    *
# dictionary to map from the ﬁrst character of the postal     *
# code to the province name. Display a meaningful error       *
# message if the postal code begins with an invalid           *
# character.                                                  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def pc_check(postal_code):
  province_dict = {'A': 'Newfoundland and Labrador', 
                   'B': 'Prince Edward Island', 
                   'C': 'New Brunswick', 
                   'E': 'Quebec', 
                   'G': 'Quebec', 
                   'H': 'Quebec', 
                   'J': 'Quebec', 
                   'K': 'Ontario', 
                   'L': 'Ontario', 
                   'M': 'Ontario', 
                   'N': 'Ontario', 
                   'P': 'Ontario', 
                   'R': 'Manitoba', 
                   'S': 'Saskatchewan' , 
                   'T': 'Alberta', 
                   'V': 'British Columbia', 
                   'X': 'Nunavut', 
                   'Y': 'Yukon'}
  if postal_code[1].isdigit() and postal_code[3].isdigit() and postal_code[5].isdigit() and postal_code[0].isalpha() and postal_code[2].isalpha() and postal_code[4].isalpha():
    if postal_code[0] in province_dict:
      if postal_code[1] == '0':
        print("This is an rural address in", province_dict[postal_code[0]])
      else:
        print("This is a urban address in", province_dict[postal_code[0]])
    else:
      print("Invalid postal code")
  else:
    print("Invalid postal code")
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  user_postal_code = input("Please enter a postal code: ")
  user_postal_code = user_postal_code.replace(" ", "")
  user_postal_code = user_postal_code.capitalize()
  print(user_postal_code)
  pc_check(user_postal_code)
  print("Thank you for using this app.")
#**************************************************************