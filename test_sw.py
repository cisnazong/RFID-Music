# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:18:11 2020

@author: zongnan
"""

from Switcher import Switcher
from Tuner import Tuner

num_switchers = 4

maxvolume = 100
maxspeed = 140

minvolume = 0
minspeed = 70

currentvolume = 95
currentspeed = 120

switch = Switcher(4)
switch.switch_off(1)
switch.switch_on(2)
switch.switch_off(2)
switch.switch_on(1)

switch.show_state()

tuner = Tuner()

currentvolume = tuner.turn_up(currentvolume,maxvolume,1)
print('vol: ',currentvolume)
currentvolume = tuner.turn_up(currentvolume,maxvolume,5)
print('vol: ',currentvolume)
currentvolume = tuner.turn_down(currentvolume,minvolume,98)
print('vol: ',currentvolume)
currentvolume = tuner.turn_down(currentvolume,minvolume,98)
print('vol: ',currentvolume)

currentspeed = tuner.turn_up(currentspeed,maxspeed,15)
print('spd: ',currentspeed)
currentspeed = tuner.turn_up(currentspeed,maxspeed,15)
print('spd: ',currentspeed)
currentspeed = tuner.turn_down(currentspeed,minspeed,80)
print('spd: ',currentspeed)
