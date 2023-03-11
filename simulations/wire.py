# wire.py

"""
Note:
The wire will contain a <int, dataType> dictionary, 
the int is for the time step a message will be received by the device on the rec end and the dataType is the message being sent

^ data is asked to be sent in the wire and an index will be made with the wires "travel time offset"
added to the time-step when the data was asked to be sent by the send end of the wire

wire structure:
from_id -- content --> to_id

"""

from enum import Enum

class WireState(Enum):
    EMPTY = 0
    IN_USE = 1

class wire:
    def __init__(self, from_id, to_id, world_devices):
        self.local_time = 0
        self.time_and_data = {}
        self.time_and_data[-1] = "pre-init-receive"
        self.send_device_id = from_id
        self.rec_device_id = to_id
        self.world_devices = world_devices

    def increment_time(self):
        # increment local time
        self.local_time = self.local_time + 1
    
    def send(self, content):
        # add content sent from device to time_and_data to be processed later
        self.time_and_data[self.local_time] = content


    def process(self, global_time):
        # calls receive on rec_device if there is a message that should be received at the current time
        if(self.time_and_data.get(global_time) != None):
            self.world_devices[self.rec_device_id].receive(self.time_and_data.get(global_time))
