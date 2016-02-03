# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:57:02 2015

@author: Georg
"""
import random

def draw_ball(hat):
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

class Hat:
    def __init__(self, **kwargs):
        colors = kwargs.keys()
        self.hat = [color for color in colors for n in range(kwargs[color])]
    
    def draw(self, n):
        balls = []
        for i in range(n):
            color, self.hat = draw_ball(self.hat)
            balls.append(color)
        return balls
    
    def putback(self, balls):
        self.hat += balls
    
    def __str__(self):
        return str(self.hat)
        
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.hat)

__all__ = ['draw_ball', 'Hat']