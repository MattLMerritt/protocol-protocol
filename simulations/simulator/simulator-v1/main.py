
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
import generate_json as gj

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
if __name__ == "__main__":

    print("version 1.0")

    '''
    Example 
    configuration:
    [Device 1] --> [Device 2]

    purpose:
    device send "hello world" to device 2 at timestep 2

    
    '''
    time_steps = 10
    world_devices = {}
    world_wires = {}
    D1 = Device(1)
    D2 = Device(2)
    world_devices[1] = D1
    world_devices[2] = D2

    w1 = Wire(1, 1, 2, world_devices, 1)
    w2 = Wire(2, 2, 1, world_devices, 2)
    world_wires[1] = w1
    world_wires[2] = w2

    # prepare export data for steps
    # populate fields of data
    export_data = {}
    export_data["steps"] = time_steps
    export_data["devices"] = len(world_devices)
    export_data["wires"] = len(world_wires)

    gj.generate_initial_state_to_json(world_devices, world_wires)

    # processing loop:
    for global_clock in range(0, time_steps):
        print("global_clock:", global_clock)

        # process each wire
        for wire_it in world_wires.values():
            wire_it.process(global_clock)


        # allow for sends from devices
        # special logic for example:
        if(global_clock == 2):
                world_devices[1].send(world_wires[1], "hello world")
        for device_it in world_devices.values():
            pass

        # update wire state info
        for wire_it in world_wires.values():
            wire_it.updateState(global_clock)

        # save into format for graphing
        gj.add_state_to_json(world_devices, world_wires, global_clock, export_data)

        # increment each device's local_clock
        for wire_it in world_wires.values():
            wire_it.increment_time()
        for device_it in world_devices.values():
            device_it.increment_time()
        print("\n")


    


    data_json = gj.json.dumps(export_data, indent=4)
    print(data_json)

    with open("test.json", "w") as outfile:
        outfile.write(data_json)
