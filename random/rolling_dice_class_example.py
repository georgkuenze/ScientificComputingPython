# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:43:15 2015

@author: Georg
"""
import random, sys

def computer_guess(ndice):
    return random.randint(1*ndice, 6*ndice)

def player_guess(ndice):
    return int(raw_input('Guess the sum of the no of eyes in the next throw: '))

class Dice:
    def __init__(self, n):
        self.n = n
        
    def throw(self):
        return [random.randint(1, 6) for i in range(self.n)]

class Player:
    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)
    
    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.throw
        else:
            self.capital -= 1
        self.message()
        self.broke()
        
    def message(self):
        print '%s guessed %d, got %d' % (self.name, self.guess, self.throw)
            
    def broke(self):
        if self.capital == 0:
            print '%s lost!' % (self.name)
            sys.exit(0)

def play(nrounds, ndice):
    player = Player('YOU', nrounds, player_guess, ndice)
    computer = Player('MACHINE', nrounds, computer_guess, ndice)
    
    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        print 'Status: YOU have %d euros. MACHINE has %d euros' % (player.capital, computer.capital)
    
    if computer.capital > player.capital:
        print 'MACHINE won!'
    elif computer.capital < player.capital:
        print 'YOU won!'
    else:
        print 'Tie!'
    
nrounds = int(sys.argv[1])
ndice   = int(sys.argv[2])

play(nrounds, ndice)