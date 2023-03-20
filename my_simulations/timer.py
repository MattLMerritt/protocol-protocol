# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:35:02 2023

@author: Runbin Chen
"""

class Timer:
    def __init__(self):
        self.timer_id = 0
        self.curtime = 0
    
    def __str__(self):
        return f"timer id: {self.timer_id}  current time: {self.curtime}"
    
    def setId(self, new_id):
        self.timer_id = new_id
    
    def setCurtime(self, new_curtime):
        self.curtime = new_curtime
    
    