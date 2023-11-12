#!/bin/bash
#**************************************************************
# Date: 110623 (Expected Solution with 51 Lines of Code)      *
# Title: Pig Latin Improved                                   *
# Status: Testing (In Progress / Testing / Working)           *
# Extend your solution to Exercise 115 so that it correctly   *
# handles uppercase letters and punctuation marks such as     *
# commas, periods, question marks and exclamation marks. If   *
# an English word begins with an uppercase letter then its    *
# Pig Latin representation should also begin with an          *
# uppercase letter and the uppercase letter moved to the end  *
# of the word should be changed to lowercase. For example,    *
# Computer should become Omputercay. If a word ends in a      *
# punctuation mark then the punctuation mark should remain at *
# the end of the word after the transformation has been       *
# performed. For example, Science! should become Iencescay! . *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def pig_ltn_trans2(user_str):
  pig_ltn_str = ""
  vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
  punc_mark = [".", ":", ";", "!", "?"]
  word_list = []
  ltr_case = "L"
  word_list = user_str.split()
  for word in word_list:  
    ctr = 0
    for ltr in word:
      if ltr in vowels:
      # words starting with vowels
        if ctr == 0 and word[-1] not in punc_mark:
          pig_ltn_str += word + "way "
          break
        elif ctr == 0 and word[-1] in punc_mark:
          pig_ltn_str += word[0:len(word)-1] + "way" + word[-1]
          break
        elif ctr > 0 and word[-1] in punc_mark:
          if any(ltr.isupper() for ltr in word):
            word = word.lower()
            pig_ltn_str += word[ctr:ctr+1].upper() + word[ctr+1:len(word)-1] + word[0:ctr] + "ay" + word[-1] + " "
          else:
            pig_ltn_str += word[ctr:len(word)-1] + word[0:ctr] + "ay" + word[-1] + " "
          break
        elif ctr > 0 and word[-1] not in punc_mark:
          if any(ltr.isupper() for ltr in word):
            word = word.lower()
            pig_ltn_str += word[ctr:ctr+1].upper() + word[ctr+1:] + word[0:ctr] + "ay "
          else:
            pig_ltn_str += word[ctr:] + word[0:ctr] + "ay "
          break
      else:
      # Words not starting with vowels
        ctr += 1
  return pig_ltn_str
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Enter a string of words in lowercase only: ")
  print("Translated string:", pig_ltn_trans2(user_input))
  print("Thank you for using this app.")
#**************************************************************