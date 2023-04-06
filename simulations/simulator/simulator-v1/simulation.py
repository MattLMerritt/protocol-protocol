
"""
Stateful Framework data flow:

1. Define setup (devices and wires)
2. Start processing Loop
3. Package contents for visualizer

Notes:
The structure of the processing loop is as follows:
- Check status of each wire and if there is a message at the "end" of a wire then it should call "receive" on the device at the rec end of the wire
- Check each device if any device is sending anything


The structure of this approach places importance on sending data to intermediate handlers (e.g. wires) to keep track of message status
instead of having a global queue that handles the status of message and routing of the message.

"""

import device
from device import Device
from wire import Wire
import wire
import generate_json
from generate_json import GenerateJson
'''
Program main: 
    a simple simulation and recording of how message passing happens among devices
Critical steps in the main function: 
    1. Create some devices as well as some wires to connect them. 
    2. Define the number of steps the simulation would have.
    3. Each iteration of the main loop represents its corresponding step.
        In each step, there are several different events that may occur:
            - A transmitter is trying to send a message to a receiver
            - A wire is passing a message from a transmitter to a receiver
            - A receive receive a message
    4. Record each step to a json file in order to show the whole process on the website. 
'''
class Simulator:
    
    def __init__(self, total_time, devices, wires, gen_json = None):
        self.total_time = total_time
        self.devices = devices
        self.wires = wires
        self.gen_json = gen_json    

    def process(self, time):
        # process each wire
        for wire_it in self.wires.values():
            wire_it.process(time)
        
        # update wire state info
        for wire_it in self.wires.values():
            wire_it.updateState(time)

        # save into format for graphing
        if self.gen_json is not None:
            self.gen_json.add_state_to_json(self.devices, self.wires, time)

        # increment each device's local_clock
        for wire_it in self.wires.values():
            wire_it.increment_time()
        for device_it in self.devices.values():
            device_it.increment_time()

    def simulate(self):
        # processing loop:
        for global_clock in range(0, self.total_time):
            self.process(global_clock)
            self.trigger_event(global_clock)

            # allow for sends from devices
            # special logic for example:
            #if(global_clock == 2):
            #    self.world_devices[1].send(self.world_wires[1], "hello world")
            #for device_it in self.world_devices.values():
            #    pass
            if global_clock == 1:
                self.devices[0].wakeup("hi")
        
        # exporting data
        if self.gen_json is not None:
            self.gen_json.export_data_to_json()
        
            