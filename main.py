#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 49 Lines of Code)      *
# Title: Redacting Text in a File                             *
# Status: In Progress (In Progress / Testing / Working)       *
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
#--------------------------------------------------------------
def redact_func(user_in):
  with open(user_in, "r") as f:
    file_data = f.read()
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input(str("Please enter the file location: "))
  file_to_redact = input(str("Please enter the file name: "))
  file_with_redacted_text = input(str("Please enter the file name for the redacted text: "))
  file_with_words_to_redact = input(str("Please enter the file name for the words to redact: "))
  redact_func(file_loc)
  print("Thank you for using this app.")
#**************************************************************