
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

import json

import device
from device import Device
from wire import Wire
import wire

time_steps = 10


def convert_states_into_json(world_devices, world_wires, global_time):
    # format: key = id, value = state

    for wire_it in world_wires.items():
            id = wire_it[0]
            state = wire_it[1]
            
    for device_it in world_devices.values():
        device_it.increment_time()

    pass


if __name__ == "__main__":

    print("hello world")

    '''
    Example configuration:
    [Device 1] --> [Device 2]
    
    '''
    world_devices = {}
    world_wires = {}
    D1 = Device()
    D2 = Device()
    world_devices[1] = D1
    world_devices[2] = D2

    w1 = Wire(1, 2, world_devices, 3)
    world_wires[1] = w1



    # processing loop:
    for global_clock in range(0, time_steps):
        print("global_clock: " + str(global_clock))

        # process each wire
        for wire_it in world_wires.values():
            wire_it.process(global_clock)


        # allow for sends from devices
        for device_it in world_devices.values():

            pass

        # update wire state info
        for wire_it in world_wires.values():
            wire_it.updateState(global_clock)

        # save into format for graphing
        convert_states_into_json(world_devices, world_wires, global_clock)
    
        # increment each device's local_clock
        for wire_it in world_wires.values():
            wire_it.increment_time()
        for device_it in world_devices.values():
            device_it.increment_time()
        print("\n")
