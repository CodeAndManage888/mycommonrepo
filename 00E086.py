#!/bin/bash
#**************************************************************
# Date: 081023 (Expected Solution with 48 Lines of Code)      *
# Title: The Twelve Days of Christmas                         *
# Status: In Progress (In Progress / Testing / Working)       *
# The Twelve Days of Christmas is a repetitive song that      *
# describes an increasingly long list of gifts sent to one’s  *
# true love on each of 12 days. A single gift is sent on the  *
# ﬁrst day. A new gift is added to the collection on each     *
# additional day, and then the complete collection is sent.   *
# The ﬁrst three verses of the song are shown below. The      *
# complete lyrics are available on the internet.              *
#                                                             *
# On the ﬁrst day of Christmas                                *
# my true love sent to me:                                    *
# A partridge in a pear tree.                                 *
#                                                             *
# On the second day of Christmas                              *
# my true love sent to me:                                    *
# Two turtle doves,                                           *
# And a partridge in a pear tree.                             *
#                                                             *
# On the third day of Christmas                               *
# my true love sent to me:                                    *
# Three French hens,                                          *
# Two turtle doves,                                           *
# And a partridge in a pear tree.                             *
#                                                             *
# Your task is to write a program that displays the           *
# complete lyrics for The Twelve Days of Christmas. Write a   *
# function that takes the verse number as its only parameter  *
# and displays the speciﬁed verse of the song. Then call that *
# function 12 times with integers that increase from 1 to 12. *
# Each item that is sent to the recipient in the song should  *
# only appear once in your program, with the possible         *
# exception of the partridge. It may appear twice if that     *
# helps you handle the difference between “A partridge in a   *
# pear tree” in the ﬁrst verse and “And a partridge in a pear *
# tree” in the subsequent verses. Import your solution to     *
# Exercise 85 to help you complete this exercise.             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
num_of_days = 1
ordinal_dict = {1:"First_A partridge in a pear tree", 
                2:"Second_Two turtle doves", 
                3:"Third", 4:"Fourth",
                5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eighth", 
                9:"Ninth:", 10:"Tenth", 11:"Eleventh", 12:"Twelfth"}
#--------------------------------------------------------------
def song_verse(input_num):


#--------------------------------------------------------------
if __name__ == "__main__":
  while num_of_days <= 12:
    song_verse(num_of_days)
    num_of_days += 1



print("Thank you for using this app.")
#**************************************************************