# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:59:43 2015

@author: Georg
"""
import random

class Deck:
    
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(s+r)
        random.shuffle(self.deck)
    
    def hand(self, n=1):
        hand = [self.deck[i] for i in range(n)]
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