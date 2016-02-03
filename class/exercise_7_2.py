# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:23:23 2015

@author: Georg
"""

class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1
    
    def __str__(self):
        return ' name: %s\n account no.: %s\n balance: %s\n no. transactions: %s\n' \
        % (self.name, self.no, str(self.balance), str(self.transactions))