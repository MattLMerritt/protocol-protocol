from simulation import Simulator
from generate_json import GenerateJson
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
    gen_json = GenerateJson(time_steps, world_devices, world_wires)
    gen_json.generate_initial_state_to_json()

    # simulate data
    sim = Simulator(time_steps, world_devices, world_wires, gen_json)
    sim.simulate()

