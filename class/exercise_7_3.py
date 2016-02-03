# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:53:13 2015

@author: Georg
"""
from time import time, gmtime, strftime

class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.no_trans = 0
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.no_trans += 1
        t = time() # get current time in seconds since the epoch 12:00am, Jan1, 1970
        # convert seconds to time tuple and format to string
        self.date_trans = strftime("%b %d %Y %H:%M:%S", gmtime(t))
        self.transactions.append({'amount': 1.0*amount, 'date': self.date_trans})
    
    def withdraw(self, amount):
        self.balance -= amount
        self.no_trans += 1
        t = time() # get current time in seconds since the epoch 12:00am, Jan1, 1970
        # convert seconds to time tuple and format to string
        self.date_trans = strftime("%b %d %Y %H:%M:%S", gmtime(t))
        self.transactions.append({'amount': -1.0*amount, 'date': self.date_trans})
    
    def __str__(self):
        s = ''        
        for element in self.transactions:
            s += (str(element)+'\n')
        return 'name: %s\naccount no.: %s\nbalance: %s\nno. transactions: %s\n' \
        % (self.name, self.no, str(self.balance), str(self.no_trans)) + s