#!/bin/bash
#**************************************************************
# Date: 080523 (Expected Solution with xe Lines of Code)      *
# Title:The Twelve Days of Christmas 41                       *
# Status: In Progress (In Progress / Testing / Working)       *
#  (Solved—48 Lines ) The Twelve Days of Christmas is a repe  *
# itive song that describes an increasingly long list of gif  *
# s sent to one’s true love on each of 12 days. A single gif  *
#  is sent on the ﬁrst day. A new gift is added to the colle  *
# tion on each additional day, and then the complete collect  *
# on is sent. The ﬁrst three verses of the song are shown be  *
# ow. The complete lyrics are available on the internet. On   *
# he ﬁrst day of Christmas my true love sent to me: A partri  *
# ge in a pear tree. On the second day of Christmas my true   *
# ove sent to me: Two turtle doves, And a partridge in a pea  *
#  tree. On the third day of Christmas my true love sent to   *
# e: Three French hens, Two turtle doves, And a partridge in  *
# a pear tree. Your task is to write a program that displays  *
# the complete lyrics for The Twelve Days of Christmas. Writ  *
#  a function that takes the verse number as its only parame  *
# er and displays the speciﬁed verse of the song. Then call   *
# hat function 12 times with integers that increase from 1 t  *
#  12. Each item that is sent to the recipient in the song s  *
# ould only appear once in your program, with the possible e  *
# ception of the partridge. It may appear twice if that help  *
#  you handle the difference between “A partridge in a pear   *
# ree” in the ﬁrst verse and “And a partridge in a pear tree  *
#  in the subsequent verses. Import your solution to Exercis  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************