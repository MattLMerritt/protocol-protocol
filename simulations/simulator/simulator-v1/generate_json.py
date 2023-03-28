# generate_json.py

import json

"""
Generating a JSON format for the state of the protocol
"""
class GenerateJson:

    def __init__(self, total_time, world_devices, world_wires, initial_filename="initial.json"):
        self.data = {}
        self.data["steps"] = total_time
        self.data["devices"] = len(world_devices)
        self.data["wires"] = len(world_wires)
        self.world_devices = world_devices
        self.world_wires = world_wires

    def add_state_to_json(self, world_devices, world_wires, global_time):
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
        self.data["step-" + str(global_time)] = step_states
        pass

    def export_input_data_to_json(self, filename="input.json"):
        # export inital data of wires and devices
        export_init_data = {}
        export_devices = [None] * len(self.world_devices)
        export_wires = [None] * len(self.world_wires)

        # create dictionary of each device and wire
        for i in self.world_devices.keys():
            export_devices[i] = {}
            export_devices[i]["id"] = "d-" + str(self.world_devices[i].get_id())
            export_devices[i]["group"] = i

        export_init_data["nodes"] = export_devices

        # create dictionary of each device and wire
        for i in self.world_wires.keys():
            export_wires[i] = {}
            export_wires[i]["source"] = "d-" + str(self.world_wires[i].get_send_device_id())
            export_wires[i]["target"] = "d-" + str(self.world_wires[i].get_rec_device_id())
            export_wires[i]["value"] = 1

        export_init_data["links"] = export_wires

        # add this data to a json
        data_json = json.dumps(export_init_data, indent=4)

        with open(filename, "w") as outfile:
            outfile.write(data_json)

    def export_data_to_json(self, filename="data.json"):
        data_json = json.dumps(self.data, indent=4)
        with open(filename, "w") as outfile:
            outfile.write(data_json)
