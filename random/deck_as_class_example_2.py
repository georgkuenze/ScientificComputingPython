# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:06:50 2015

@author: Georg
"""
import random

class Card:
    def __init__(self, suit, rank):
        self.card = suit + str(rank)
    def __str__(self):
        return str(self.card)
    def __repr__(self):
        return self.__str__()

class Hand:
    def __init__(self, list_of_cards):
        self.hand = list_of_cards
    def __str__(self):
        return str(self.hand)
    def __repr__(self):
        return self.__str__()

class Deck:
    
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))
        random.shuffle(self.deck)
    
    def hand(self, n=1):
        hand = Hand([self.deck[i] for i in range(n)])
        del self.deck[:n]
        return hand
    
    def deal(self, cards_per_hand, no_of_players):
        return [self.hand(cards_per_hand) for i in range(no_of_players)]
    
    def putpack(self, card):
        self.deck.append(card)
    
    def __str__(self):
        return str(self.deck)
    
    def __repr__(self):
        return self.__str__()
        
    def __len__(self):
        return len(self.deck)
    
__all__ = ['Card', 'Hand', 'Deck']