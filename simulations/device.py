# device.py

"""
Notes:

a live device loosely defined is a device that sends messages through wires autonomously.
"""

from enum import Enum

class DeviceState(Enum):
    IDLE = 0
    SENDING = 1
    RECEIVING = 2
    SENDING_AND_RECEIVING = 3


class device:
    def __init__(self):
        # timed_sends is randomized used to emulate a "live" device 
        # the key is the timestep when the message should be sent and the value is the data to be sent
        timed_sends = {}
        timed_sends[-1] = "pre-init-send"
