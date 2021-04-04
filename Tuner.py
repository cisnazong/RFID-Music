# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:26:24 2020

@author: zongnan
"""
#Notice: unit is the chiffre in front of %
#import

class Tuner:
    
    # GPIO
    
    def __init__(self):
        # GPIO all LOW
        # Set High to trigger
        print('Initialized!')
        
    
    def turn_up(self, value, maxvalue, step):
        # if GPIO of boxid is HIGH
        # then Set GPIO of boxid to Low
        sumv = (value + step)
        if sumv >= maxvalue:
            outvalue = maxvalue
        else:
            outvalue = sumv
        print('Turn up to ',outvalue)
        return outvalue
        
    def turn_down(self, value, minvalue, step):
        # if GPIO of boxid is Low
        # then Set GPIO of boxid to HIGH
        diff = (value - step)
        if diff <= minvalue:
            outvalue = minvalue
        else:
            outvalue = diff
        print('Turn down to ',outvalue)
        return outvalue