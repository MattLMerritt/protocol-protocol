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

class Wire():
    def __init__(self, id, from_id, to_id, world_devices, wire_delay = 0):
        self.id = id
        self.local_time = 0
        self.state = WireState.EMPTY
        self.time_and_data = {}
        self.time_and_data[-1] = "pre-init-receive"
        self.send_device_id = from_id
        self.rec_device_id = to_id
        self.world_devices = world_devices
        self.wire_delay = wire_delay + 1 # wire delay arg must be non-zero

    def get_id(self) -> int:
        return self.id

    def get_send_device_id(self) -> int:
        return self.send_device_id
    
    def get_rec_device_id(self) -> int:
        return self.rec_device_id
    
    def get_delay(self) -> int:
        return self.wire_delay

    def increment_time(self):
        # increment local time
        self.local_time = self.local_time + 1
    
    def send(self, content):
        # add content sent from device to time_and_data to be processed later
        self.time_and_data[self.local_time + self.wire_delay] = content
        print("device " + str(self.send_device_id) + " sent off a message[" + str(content) + "] to device" + str(self.rec_device_id))


    def process(self, global_time):
        # calls receive on rec_device if there is a message that should be received at the current time
        if(self.time_and_data.get(global_time) != None):
            self.world_devices[self.rec_device_id].receive(self.time_and_data.get(global_time))
            print("device " +  str(self.rec_device_id) + " received a message[" + str(self.time_and_data.get(global_time)) + "] from device " + str(self.send_device_id))

    def updateState(self, global_time):
        # update self state if there are any message left to be sent
        self.state = WireState.EMPTY
        for val in self.time_and_data.keys():
            if val > (global_time-1):
                self.state = WireState.IN_USE
            
    def getStateString(self, global_time):
        # return string of state
        res = {}
        if(self.state == WireState.EMPTY):
            res["STATE"] = "EMPTY"
            res["DATA"] = ""
        else:
            res["STATE"] = "IN_USE"
            message = ""
            for it in self.time_and_data.items():
                if (it[0] >= global_time):
                    message += '(' + it[1] + ') '
            res["DATA"] = message.strip()
        return res

    def print_wire(self):
        print(f"wire {self.id}: ( {self.rec_device_id} ) --> ( {self.send_device_id} )")
