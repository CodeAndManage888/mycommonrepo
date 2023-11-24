#!/bin/bash
#**************************************************************
# Date: 111323 (Expected Solution with 48 Lines of Code)      *
# Title: Shuffling a Deck of Cards                            *
# Status: Testing (In Progress / Testing / Working)           *
# A standard deck of playing cards contains 52 cards. Each    *
# card has one of four suits along with a value. The suits    *
# are normally spades, hearts, diamonds and clubs while the   *
# values are 2 through 10, Jack, Queen, King and Ace. Each    *
# playing card can be represented using two characters. The   *
# first character is the value of the card, with the values 2 *
# through 9 being represented directly. The characters “T”,   *
# “J”, “Q”, “K” and “A” are used to represent the values 10,  *
# Jack, Queen, King and Ace respectively. The second          *
# character is used to represent the suit of the card. It is  *
# normally a lowercase letter: “s” for spades, “h” for        *
# hearts, “d” for diamonds and “c” for clubs. The following   *
# table provides several examples of cards and their          *
# two-character representations.                              *
#                                                             *
#           Card             | Abbreviation                   *
#          ----------------------------------                 *
#           Jack of spades   | Js                             *
#           Two of clubs     | 2c                             *
#           Ten of diamonds  | Td                             *
#           Ace of hearts    | Ah                             *
#           Nine of spades   | 9s                             *
#                                                             *
# Card Abbreviation Jack of spades Js Two of clubs 2c Ten of  *
# diamonds Td Ace of hearts Ah Nine of spades 9s Begin by     *
# writing a function named createDeck . It will use loops to  *
# create a complete deck of cards by storing the two-character*
# abbreviations for all 52 cards into a list. Return the list *
# of cards as the function’s only result. Your function will  *
# not take any parameters. Write a second function named      *
# shuffle that randomizes the order of the cards in a list.   *
# One technique that can be used to shuffle the cards is to   *
# visit each element in the list and swap it with another     *
# random element in the list. You must write your own loop    *
# for shufﬂing the cards. You cannot make use of Python’s     *
# built-in shufﬂe function. Use both of the functions         *
# described in the previous paragraphs to create a main       *
# program that displays a deck of cards before and after it   *
# has been shuffled. Ensure that your main program only runs  *
# when your functions have not been imported into another     *
# file.                                                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
#--------------------------------------------------------------
deck_of_cards = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                 'Ts', 'Js', 'Qs', 'Ks', 'As', '2h', '3h', '4h', 
                 '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 
                 'Kh', 'Ah', '2d', '3d', '4d', '5d', '6d', '7d', 
                 '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', '2c', 
                 '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 
                 'Jc', 'Qc', 'Kc', 'Ac']
deck_shuffled = []
idx = 0
#--------------------------------------------------------------
def createDeck(deckcard_list):
  idx = random.randint(0,len(deckcard_list)-1)
  while len(deckcard_list) != 0:
    deck_shuffled.append(deckcard_list.pop(idx))
    if len(deckcard_list) != 0:
      idx = random.randint(0,len(deckcard_list)-1)
  return deck_shuffled
#--------------------------------------------------------------
if __name__ == "__main__":
  print("deck_of_cards = ", deck_of_cards)
  print("deck_of_cards = ", createDeck(deck_of_cards))
  print("Thank you for using this app.")
#**************************************************************