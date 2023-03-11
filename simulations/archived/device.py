# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:13:33 2023

@author: Runbin Chen
"""

import random
import timer
from enum import Enum

class DeviceState(Enum):
    EMPTY = 0
    FULL = 1

class Device: 
    def __init__(self):
        self.device_id = 0
        self.address = 0x00
        self.timers = []
    
    def __str__(self):
        return f"device id: {self.device_id}  address: {self.address}"
    
    def setId(self, new_id):
        self.device_id = new_id
        
    def setAddress(self, new_address):
        self.address = new_address
    
    def addTimer(self, timer_id, timer_curtime):
        self.timers.append(timer.Timer())
        self.timers[-1].setId(timer_id)
        self.timers[-1].setCurtime(timer_curtime)
    
    def send(self):
        
    
    def generateRandomMessage(self):
        randstr = ""
        for i in range(random.randint(1, 10)):
            randstr += chr(random.randint(33, 126))
        return randstr

