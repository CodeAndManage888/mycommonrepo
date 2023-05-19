#**************************************************************
# Date: 051923                                                *
# Title: Vowel or Consonant                                   *
# Status: Testing (In Progress / Testing / Working)           *
# In this esercise you will create a program that reads a     *
# letter of the alphabet from the user. If the user enters a, *
# e, i, o or u then you r program should display a message    *
# indicating that the entered letter is a vowel. If the uswer *
# enters y then your program should display a message         *
# indicating that sometimes y is a vowel, and sometimes y is  *
# a consonant. Otherwise your program should display a        *
# message indicating that the letter is a consonant.          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sometimes_list = ["y", "Y"]
consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", 
                  "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", 
                  "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
iOneCharOnly = " "
#-------------------------------------------------------------- 
iOneCharOnly = input("What character is in your mind (One Character Only)?==> ")
if len(iOneCharOnly) > 1:
  print("Invalid input data! One charater data only.")
  print("Thank you for using this app.")
else:
  if iOneCharOnly in sometimes_list:
    print("Sometimes " + "'" +  iOneCharOnly + "'" +  " is a vowel sometimes it's a consonant")
    print("Thank you for using this app.")
  else: 
    if iOneCharOnly in vowel_list:
      print("'" + iOneCharOnly + "'" + " is a vowel.")
      print("Thank you for using this app.")    
    else:
      if iOneCharOnly in consonant_list:
        print("'" + iOneCharOnly + "'" + " is a consonant.")
        print("Thank you for using this app.")
      else:
        print("'" + iOneCharOnly + "'" + " is an invalid input data(Alphabet Only).")
        print("Thank you for using this app.")   
#**************************************************************
# Open Items:
#
# CHistory:
# C0519230900
# - completed the code for exercise 36 ready for testing
# 