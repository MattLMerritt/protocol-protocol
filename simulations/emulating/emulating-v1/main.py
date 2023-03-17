
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

def add_state_to_json(world_devices, world_wires, global_time, all_states_dict):
    # create dictionary of each device and wire with their assoisated state

    step_states = {}

    # add states of devices
    id_counter = 0
    for i in world_devices.keys():
        step_states["d-" + str(id_counter)] = world_devices[i].getStateString()
        id_counter = id_counter + 1
    
    # add states of wires
    id_counter = 0
    for i in world_wires.keys():
        step_states["w-" + str(id_counter)] = world_wires[i].getStateString()
        id_counter = id_counter + 1
    
    # add all of the devices and wires to the state index in the dictionary
    all_states_dict["step-" + str(global_time)] = step_states
    pass



if __name__ == "__main__":

    print("hello world")

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
    D1 = Device()
    D2 = Device()
    world_devices[1] = D1
    world_devices[2] = D2

    w1 = Wire(1, 2, world_devices, 1)
    world_wires[1] = w1



    # prepare export data for steps
    # populate fields of data
    export_data = {}
    export_data["steps"] = time_steps
    export_data["devices"] = len(world_devices)
    export_data["wires"] = len(world_wires)



    # processing loop:
    for global_clock in range(0, time_steps):
        print("global_clock: " + str(global_clock))

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
        add_state_to_json(world_devices, world_wires, global_clock, export_data)
    
        # increment each device's local_clock
        for wire_it in world_wires.values():
            wire_it.increment_time()
        for device_it in world_devices.values():
            device_it.increment_time()
        print("\n")


    


    data_json = json.dumps(export_data, indent=4)
    print(data_json)

    with open("test.json", "w") as outfile:
        outfile.write(data_json)
