# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:36:09 2015

@author: Georg
"""

import random, sys

nrounds = int(sys.argv[1])   # no of rounds the die is thrown
ndice   = int(sys.argv[2])   # no of dice
N       = int(sys.argv[3])   # no of experiments


def roll_dice(ndice):
    return sum([random.randint(1,6) for i in range(ndice)])

def computer_guess(ndice):
    return random.randint(1*ndice, 6*ndice)

def player_guess(ndice):
    return round((ndice*6 - ndice*1)/2.0) + ndice*1 # number between 6*no - 1*no is most frequently represented by eye no.

def play_one_round(ndice, capital, guess_function):
    guess = guess_function(ndice)
    throw = roll_dice(ndice)
    if guess == throw:
        capital += guess
    else:
        capital -= 1
    return capital, throw, guess

def play(nrounds, ndice):
    player_capital = computer_capital = nrounds
    
    for i in range(nrounds):
        player_capital, throw, guess = play_one_round(ndice, player_capital, player_guess)
        computer_capital, throw, guess = play_one_round(ndice, computer_capital, computer_guess)

        if player_capital == 0 or computer_capital == 0:
            break
    
    if computer_capital > player_capital:     # Computer wins
        return 0
    elif computer_capital < player_capital:   # Player wins
        return 1
    else:                                     # ties
        return 2

winner = []
for i in range(N):
    winner.append(play(nrounds, ndice))
computer_wins = winner.count(0)/float(N)
player_wins   = winner.count(1)/float(N)
ties          = winner.count(2)/float(N)

print 'Overall result - frequency of wins:\nComputer: %.2f, Player: %.2f, Ties: %.2f' % \
(computer_wins, player_wins, ties)
