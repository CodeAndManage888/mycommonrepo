#!/bin/bash
#**************************************************************
# Date: 051124 (Expected Solution with 59 Lines of Code)      *
# Title: What’s that Element Again?                           *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads a file containing information    *
# about chemical elements and stores it in one or more        *
# appropriate data structures. Then your program should read  *
# and process input from the user. If the user enters an      *
# integer then your program should display the symbol and     *
# name of the element with the number of protons entered. If  *
# the user enters a string then your program should display   *
# the number of protons for the element with that name or     *
# symbol. Your program should display an appropriate error    *
# message if no element exists for the name, symbol or num-   *
# ber of protons entered. Continue to read input from the     *
# user until a blank line is entered.                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
if __name__ == "__main__":
  input_file = "test05.txt"
  temp_list = []
  element_dict = {}
  find_flag = False

  with open(input_file, "r") as chemelem:
    element_record = chemelem.readlines()

  for idx, readline in enumerate(element_record):
    temp_list = readline.split(", ")
    element_dict[int(temp_list[2])] = [temp_list[0], temp_list[1], temp_list[3], temp_list[4][0:-1]]

  while True:
    user_data = input("Please enter the element number, name, symbol or atomic number: ")

    if user_data == "":
      print("Thank you for using this app.")
      break

    if user_data.isdigit():
      if int(user_data) in element_dict:
        print("Element Number:", user_data)
        print("Element Name:", element_dict[int(user_data)][0])
        print("Element Symbol:", element_dict[int(user_data)][1])
        print("Number of Protons:", user_data)
      else:
        print("Element not found!")
    elif user_data.isalpha():
      for idx, keys in enumerate(element_dict):
        if user_data.capitalize() in element_dict[keys]:
          find_flag = True
          print("Element Number:", keys)
          print("Element Name:", element_dict[keys][0])
          print("Element Symbol:", element_dict[keys][1])
          print("Number of Protons:", keys)
          break
      if idx == len(element_dict) - 1 and find_flag == False:
        print("Element not found!")
#**************************************************************