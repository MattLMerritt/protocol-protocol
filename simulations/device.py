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
        self.local_time = 0
        # timed_sends is randomized used to emulate a "live" device 
        # the key is the timestep when the message should be sent and the value is the data to be sent
        self.timed_sends = {}
        self.timed_sends[-1] = "pre-init-send"

        # received_content is to keep track of what content has been received by the device
        self.received_content = []

    def increment_time(self):
        self.local_time = self.local_time + 1

    def send(self, wire, content):
        wire.send(content)

    def receive(self, content):
        self.received_content.append(content)

