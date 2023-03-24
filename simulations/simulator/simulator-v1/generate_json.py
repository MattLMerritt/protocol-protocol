# generate_json.py

"""
This file holds some helper functions to generate a json file
"""

import json

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
        step_states["w-" + str(id_counter)] = world_wires[i].getStateString(global_time)
        id_counter = id_counter + 1
    
    # add all of the devices and wires to the state index in the dictionary
    all_states_dict["step-" + str(global_time)] = step_states
    pass

def generate_initial_state_to_json(world_devices, world_wires):
    # export inital data of wires and devices
    export_init_data = {}
    export_init_data["num-devices"] = len(world_devices)
    export_init_data["num-wires"] = len(world_devices)

    export_devices = {}

    # create dictionary of each device and wire
    for i in world_devices.keys():
        export_devices["d-" + str(world_devices[i].get_id())] = {}
        export_devices["d-" + str(world_devices[i].get_id())]["name"] = world_devices[i].get_name()

    export_init_data["devices"] = export_devices
    
    export_wires = {}

    # create dictionary of each device and wire
    for i in world_wires.keys():
        export_wires["w-" + str(world_wires[i].get_id())] = {}
        export_wires["w-" + str(world_wires[i].get_id())]["send"] = "d-" + str(world_wires[i].get_send_device_id())
        export_wires["w-" + str(world_wires[i].get_id())]["rec"] = "d-" + str(world_wires[i].get_rec_device_id())

    export_init_data["devices"] = export_devices
    export_init_data["wires"] = export_wires

    # add this data to a json
    data_json = json.dumps(export_init_data, indent=4)

    with open("result.json", "w") as outfile:
        outfile.write(data_json)
