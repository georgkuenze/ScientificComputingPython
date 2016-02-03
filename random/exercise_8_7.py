# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:45 2015

@author: Georg
"""
import sys
N = int(sys.argv[1])

from deck_as_class_example_1 import Deck
import random

def same_rank(hand, n_of_a_kind):
    ranks = [card[1:] for card in hand]
    counter = 0
    already_counted = []
    for rank in ranks:
        if rank not in already_counted and ranks.count(rank) == n_of_a_kind:
            counter += 1
            already_counted.append(rank)
    return counter

def same_suit(hand):
    suits = [card[0] for card in hand]
    counter = {}   #counter[suit] = how many cards of same suit
    for suit in suits:
        count = suits.count(suit)
        if count > 1:
            counter[suit] = count
    return counter

M_two_pairs = 0
M_same_suit = 0
M_4_of_a_kind = 0

counter = 0
while counter < N:
    deck = Deck()
    hand = deck.hand(5)
    event1 = same_rank(hand, 2)
    event2 = same_suit(hand)
    event3 = same_rank(hand, 4)
    if event1 == 2:
        M_two_pairs += 1
    elif (4 or 5) in event2.values():
        M_same_suit += 1
    elif event3 == 1:
        M_4_of_a_kind += 1
    counter += 1
    
p_tow_pairs = M_two_pairs/float(N)
p_same_suit = M_same_suit/float(N)
p_4_of_a_kind = M_4_of_a_kind/float(N)

print 'Probability of two pairs among 5 cards: %g' % p_tow_pairs
print 'Probability of four or five of the same suit among 5 cards: %g' % p_same_suit
print 'Probability of 4-of-a-kind among 5 cards: %g' % p_4_of_a_kind