#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 49 Lines of Code)      *
# Title: Redacting Text in a File                             *
# Status: Testing (In Progress / Testing / Working)           *
#  Sensitive information is often removed, or redacted, from  *
# documents before they are released to the public. When the  *
# documents are released it is common for the redacted text   *
# to be replaced with black bars. In this exercise you will   *
# write a program that redacts all occurrences of sensitive   *
# words in a text file by replacing them with asterisks. Your *
# program should redact sensitive words wherever they occur,  *
# even if they occur in the middle of another word. The list  *
# of sensitive words will be provided in a separate text ﬁle. *
# Save the redacted version of the original text in a new     *
# file. The names of the original text file, sensitive words  *
# file, and redacted file will all be provided by the user.   *
# You may find the replace method for strings helpful when    *
# completing this exercise. Information about the replace     *
# method can either be found in your textbook or on the       *
# internet. For an added challenge, extend your program so    *
# that it redacts words in a case insensitive manner. For     *
# example, if exam appears in the list of sensitive words     *
# then redactexam ,Exam ,ExaM andEXAM , among other possible  *
# capitalizations.                                            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
redact_list = []

def redact_func(user_in1, user_in2, user_in3, user_in4):
  file_in1 = user_in1 + "/" + user_in2
  file_in2 = user_in1 + "/" + user_in3
  file_in3 = user_in1 + "/" + user_in4

  with open(file_in3, "r") as f:
    file_data2 = f.readlines()

# Created a list of words to redact
  for index, lines in enumerate(file_data2):
    line = lines.split()
    for word in line:
      redact_list.append(word)
  print(redact_list)  

  with open(file_in1, "r") as f:
    file_data1 = f.readlines()

# Read input file and compares words to redact list
  for idx1, line in enumerate(file_data1):
    line = line.lower()
    line_temp = line.split()
    lines = line.split()

    for idx2, word in enumerate(lines):
      word = word.strip(",.:;'\"?!\\")
      if word in redact_list:
        if len(lines[idx2]) == len(word):
          line_temp[idx2] = line_temp[idx2].replace(word, "*" * len(word))
        else:
          mod_word = word.replace(word, "*" * len(word) + word[len(word):])
          line_temp[idx2] = line_temp[idx2].replace(word, mod_word)

    with open(file_in2, "w") as f:
      file_data1[idx1] = " ".join(line_temp) + "\n"
      f.writelines(file_data1)

  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input(str("Please enter the file location: "))
  file_to_redact = input(str("Please enter the file name: "))
  redacted_file = input(str("Please enter the file name for the redacted text: "))
  words_redact = input(str("Please enter the file name for the words to redact: "))
  redact_func(file_loc, file_to_redact, redacted_file, words_redact)
  print("Thank you for using this app.")
#**************************************************************