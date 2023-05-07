#**************************************************************
# Date: 050723                                                *
# Title: Sum of the Digits in an Integer                      *
# Status: In Progress (In Progress / Testing / Working)       *
# Develop a program that reads a four-digit integer from the  *
# user and displays the sum of the digits in the number. For  *
# example, if the user enters 3141 then your program should   *
# display 3+1+4+1=9.                                          *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
#--------------------------------------------------------------
sample_text = "123456"
num_list = []
sum_num = 0

for i in range(len(sample_text)):
    print(sample_text[i])
#    num_list.apppend(sample_text[i])

for i in range(len(sample_text)):
    sum_num = sum_num + int(sample_text[i])

print(sum_num)

print("<---------->")

for char in sample_text:
    print(char)
#--------------------------------------------------------------
#**************************************************************
# Open Items:
#
# CHistory:
# C05072200
# - test possible ways to break down a string
# 
