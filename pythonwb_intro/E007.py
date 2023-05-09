#**************************************************************
# Date: 040221                                                *
# Sum of Positive Interger                                    *
# Programmer: BoredManager                                    *
# Write a program that reads a positive integer, n, from the  * 
# user and then displays the sum of all of the integers from  * 
# 1 to n. The sum of the first n positive integers can be     * 
# computed using the formula:                                 *
#           sum = (n(n+1)) / 2                                *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iUser_Number = input("Please enter a number ==> ")
    try:
        ciUser_Number = int(iUser_Number)
        icheck = 0
    except:
        print("Please use whole number only.")
#--------------------------------------------------------------
computed_value = round((ciUser_Number * (ciUser_Number + 1)) / 2)
ciUser_Number = str(ciUser_Number)
final_value = str(computed_value)
#--------------------------------------------------------------
print("The the sum of the positive interger for "+iUser_Number+" is "+final_value+".")
print("Thank you for using this app.")

#**************************************************************
# what have I learned from this challenge?
# - unless i use the command round the interger will be 
#   displayed with a decimal point followed by a zero.
# - the challenges are now more focused on mathematical 
#   operation. It looks straight forward but i wonder if there 
#   are other ways to solve these challenges.
# - need to brush up on how to use % for string manipulation (A1)