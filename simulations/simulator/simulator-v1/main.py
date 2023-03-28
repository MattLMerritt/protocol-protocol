from simulation import Simulator
from device import Device
from wire import Wire

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

    # export data
    gen_json = GenerateJson(time_steps, world_devices=world_devices, world_wires=world_wires)

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
        gen_json.add_state_to_json(world_devices, world_wires, global_clock)

        # increment each device's local_clock
        for wire_it in world_wires.values():
            wire_it.increment_time()
        for device_it in world_devices.values():
            device_it.increment_time()

    gen_json.export_data_to_json()
    