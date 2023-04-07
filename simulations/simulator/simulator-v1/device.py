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


class Device():
    def __init__(self, id, name=""):
        self.id = id
        self.local_time = 0
        self.state = DeviceState.IDLE
        self.outward_wire_ids = []
        # timed_sends is randomized used to emulate a "live" device 
        # the key is the time-step when the message should be sent and the value is the data to be sent 
        self.timed_sends = {}
        self.timed_sends[-1] = "pre-init-send"

        # received_content is to keep track of what content has been received by the device
        self.received_content = []

        self.name = name
        if(name == ""):
            self.name = "device " + str(id)


    def increment_time(self):
        # increment local time
        self.local_time = self.local_time + 1
        self.state = DeviceState.IDLE
    
    def get_all_outgoing_wires(self):
        return self.outward_wire_ids

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def add_outgoing_wire(self, wire):
        self.outward_wire_ids.append(wire.get_id())

    def send(self, wire, content):
        # send content to wire and update device state
        wire.send(content)
        if(self.state == DeviceState.RECEIVING):
            self.state = DeviceState.SENDING_AND_RECEIVING
        else:
            self.state = DeviceState.SENDING


    def receive(self, content):
        # receive logic and update state
        self.received_content.append(content)
        self.state = DeviceState.RECEIVING


    def getStateString(self):
        # return string of state
        if(self.state == DeviceState.IDLE): 
            return "IDLE"
        elif(self.state == DeviceState.SENDING): 
            return "SENDING"
        elif(self.state == DeviceState.RECEIVING): 
            return "RECEIVING"
        elif(self.state == DeviceState.SENDING_AND_RECEIVING): 
            return "SENDING_AND_RECEIVING"
        else:
            return "UNKNOWN-STATE"