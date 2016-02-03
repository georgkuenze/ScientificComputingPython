# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:07:21 2015

@author: Georg
"""

import random, sys

nrounds = int(sys.argv[1])
ndice   = int(sys.argv[2])

def roll_dice(ndice):
    return sum([random.randint(1,6) for i in range(ndice)])

def computer_guess(ndice):
    return random.randint(1*ndice, 6*ndice)

def player_guess(ndice):
    return int(raw_input('Guess the sum of the no of eyes in the next throw: '))

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
        print 'YOU guessed %d, got %d' % (guess, throw)
        
        computer_capital, throw, guess = play_one_round(ndice, computer_capital, computer_guess)
        print 'MACHINE guessed %d, got %d' % (guess, throw)
        
        print 'Status: YOU have %d euros. MACHINE has %d euros' % (player_capital, computer_capital)
        
        if player_capital == 0 or computer_capital == 0:
            break
    
    if computer_capital > player_capital:
        print 'MACHINE won!'
    elif computer_capital < player_capital:
        print 'YOU won!'
    else:
        print 'Tie!'

play(nrounds, ndice)