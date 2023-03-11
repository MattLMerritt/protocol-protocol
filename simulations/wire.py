# wire.py

"""
Note:
The wire will contain a <int, dataType> dictionary, 
the int is for the time step a message will be received by the device on the rec end and the dataType is the message being sent

^ data is asked to be sent in the wire and an index will be made with the wires "travel time offset"
added to the time-step when the data was asked to be sent by the send end of the wire

"""

from enum import Enum

# time_and_data is 

class WireState(Enum):
    EMPTY = 0
    IN_USE = 1

class wire:
    def __init__(self):
        time_and_data = {}
        time_and_data[-1] = "pre-init-receive"