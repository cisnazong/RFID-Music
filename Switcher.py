# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:09:40 2020

@author: zongnan
"""
import RPI.GPIO


class Switcher:
    
    # GPIO
    gpl = []
    
    def __init__(self):
        # GPIO all LOW
        # Set High to trigger
        GPIO.setmode(GPIO.BCM)
        GPIO.output(1,GPIO.HIGH)
        GPIO.output(2,GPIO.LOW)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        gpl = self.gpl
        gpl.append(1)
        for i in range(3):
            gpl.append(0)
        print('Initialized! ',gpl)
        
    
    def switch_off(self, boxid):
        # if GPIO of boxid is HIGH
        # then Set GPIO of boxid to Low
        gpl = self.gpl
        if self.gpl[boxid] != 0:
            gpl[boxid] = 0
            GPIO.output(boxid,GPIO.LOW)
        print('Switched off at box %d with volt: %s' %(boxid,"LOW"))
        
    def switch_on(self, boxid):
        # if GPIO of boxid is Low
        # then Set GPIO of boxid to HIGH
        gpl = self.gpl
        if gpl[boxid] != 1:
            gpl[boxid] = 1
            GPIO.output(boxid,GPIO.LOW)
        print('Switched on at box %d with volt: %s' %(boxid,"HIGH"))
        
    def show_state(self):
        print("Current state is : ", self.gpl)