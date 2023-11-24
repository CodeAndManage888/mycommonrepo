#!/bin/bash
#**************************************************************
# Date: 111323 (Expected Solution with 44 Lines of Code)      *
# Title: Dealing Hands of Cards                               *
# Status: Testing (In Progress / Testing / Working)           *
# In many card games each player is dealt a speciﬁc number of *
# cards after the deck has been shufﬂed. Write a function,    *
# deal , which takes the number of hands, the number of cards *
# per hand, and a deck of cards as its three parameters. Your *
# function should return a list containing all of the hands   *
# that were dealt. Each hand will be represented as a list of *
# cards. When dealing the hands, your function should modify  *
# the deck of cards passed to it as a parameter, removing     *
# each card from the deck as it is added to a player’s hand.  *
# When cards are dealt, it is customary to give each player a *
# card before any player receives an additional card. Your    *
# function should follow this custom when constructing the    *
# hands for the players. Use your solution to Exercise 118 to *
# help you construct a main program that creates and shufﬂes  *
# a deck of cards, and then deals out four hands of ﬁve cards *
# each. Display all of the hands of cards, along with the     *
# cards remaining in the deck after the hands have been       *
# dealt.                                                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
import E118
#--------------------------------------------------------------
deck_of_cards = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 
                 'Ts', 'Js', 'Qs', 'Ks', 'As', '2h', '3h', '4h', 
                 '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 
                 'Kh', 'Ah', '2d', '3d', '4d', '5d', '6d', '7d', 
                 '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad', '2c', 
                 '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 
                 'Jc', 'Qc', 'Kc', 'Ac']
deck_shuffled = []
deck_remain = []
#--------------------------------------------------------------
def deal_func(ShuffledDeck):
  deal_hand1, deal_hand2, deal_hand3, deal_hand4 = [], [], [], []
  idx = 0
  while idx <= 5:
    deal_hand1.append(ShuffledDeck.pop(0))
    deal_hand2.append(ShuffledDeck.pop(0))
    deal_hand3.append(ShuffledDeck.pop(0))
    deal_hand4.append(ShuffledDeck.pop(0))
    idx += 1
  return [deal_hand1, deal_hand2, deal_hand3, deal_hand4, ShuffledDeck]
#--------------------------------------------------------------
if __name__ == "__main__":
  print("This program will shuffle a deck of cards and then deal out four hands of five cards each.")
  print("Deck of Cards: ", deck_of_cards)
  deck_shuffled = E118.createDeck(deck_of_cards)
  print("Deck of Cards Before Dealing: ", deck_shuffled)
  player_1, player_2, player_3, player_4, deck_remain = deal_func(deck_shuffled)
  print("First Player Cards: ", player_1)
  print("Second Player Cards: ", player_2)
  print("Third Player Cards: ", player_3)
  print("Fourth Player Cards: ", player_4)
  print("Remaining Cards: ", deck_remain)
  print("Thank you for using this app.")
#**************************************************************