#!/bin/bash
#*************************************************************
# Date: 072824 (Expected Solution with 56 Lines of Code)     *
# Title: Gender Neutral Names                                *
# Status: In Progress (In Progress / Testing / Working)      *
#  Some names, like Ben and Jonathan, are normally only used *
# for boys while names like Rebbecca and Flora are normally  *
# only used for girls. Other names, like Chris and Alex, may *
# be used for both boys and girls. Write a program that      *
# determines and displays all of the baby names that were    *
# used for both boys and girls in a year speciﬁed by the     *
# user. Your program should generate an appropriate message  *
# if there were no gender neutral names in the selected year.*
# Display an appropriate error message if you do not have    *
# data for the year requested by the user. Additional details*
# about the baby names data set are included in Exercise 154.*
#                                                            *
# Computed Result Validated:                                 *
#*************************************************************
input_list = []
non_binary_list = []
non_binary_names = [
    "Alex", "Avery", "Bailey", "Blair", "Cameron", "Casey", "Charlie", "Dakota", "Drew", "Elliot",
    "Emery", "Finley", "Harley", "Hayden", "Hunter", "Jaden", "Jamie", "Jay", "Jesse", "Jordan",
    "Kai", "Kendall", "Lee", "Logan", "London", "Morgan", "Parker", "Phoenix", "Quinn", "Reese",
    "River", "Rory", "Rowan", "Riley", "Sage", "Sam", "Shiloh", "Sky", "Skyler", "Taylor",
    "Toby", "Toni", "Tyler", "Val", "Winter", "Wren", "Ash", "Blaine", "Brook", "Caden",
    "Campbell", "Carter", "Dak", "Devon", "Dylan", "Emerson", "Frankie", "Gray", "Hollis", "Indigo",
    "Jules", "Justice", "Keegan", "Kieran", "Lane", "Leighton", "Lennon", "Levi", "Marlowe", "Micah",
    "Milan", "Noah", "Oakley", "Ocean", "Peyton", "Reagan", "Remi", "Rory", "Shane", "Skylar",
    "Spencer", "Stevie", "Tegan", "Terry", "Tristan", "West", "Zion", "Arden", "August", "Blake",
    "Ellis", "Harper", "Jessie", "Kit", "Lake", "Laurie", "Linden", "Marley", "Monroe", "Sasha",
    "Adrian", "Amari", "Angel", "Arlo", "Ashton", "Aspen", "Bellamy", "Billie", "Blaze", "Briar",
    "Cairo", "Cato", "Chandler", "Clarke", "Cleo", "Cory", "Dallas", "Darian", "Easton", "Echo",
    "Eden", "Emory", "Evan", "Ezra", "Fallon", "Flynn", "Forest", "Gabriel", "Genesis", "Greer",
    "Halston", "Haven", "Hollis", "Ira", "Ivory", "Jael", "Jess", "Jordan", "Kasey", "Keaton",
    "Kendrick", "Kiah", "Lake", "Lark", "Laurence", "Lior", "Lux", "Lyric", "Mack", "Madden",
    "Mason", "Max", "Memphis", "Mika", "Murphy", "Nova", "Ollie", "Onyx", "Paisley", "Palmer",
    "Paris", "Pax", "Piper", "Rafe", "Reed", "Reign", "Rex", "Rio", "Robin", "Sailor",
    "Scout", "Shay", "Storm", "Sunny", "Tatum", "Toby", "Torrence", "True", "Vesper", "Wynne",
    "Zephyr", "Zuri", "Axel", "Beau", "Bo", "Brady", "Cai", "Cedar", "Cody", "Dara"
]
#--------------------------------------------------------------
def read_files(user_in1, user_in2):
  input_list.append(user_in2+"f")
  input_list.append(user_in2+"m")
  non_binary_count = 0
  for file_name in input_list:
    file_path = f"{user_in1}/{file_name}"
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
    for line_item in file_data:
      temp_name, temp_count = line_item.split(",")
      if temp_name in non_binary_names:
        non_binary_count += 1
        non_binary_names.append(temp_name)
  if non_binary_count > 0:
    print("There are", non_binary_count, "non-binary names in the data set.")
    print(non_binary_names)
  else:
    print("There are no non-binary names in the data set.")
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Enter file location: ")
  target_year = input("Enter target year: ")
  read_files(file_location, target_year)
  print("Thank you for using this app.")
#**************************************************************
