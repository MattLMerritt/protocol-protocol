from simulation import Simulator
from generate_json import GenerateJson
from device import Device
from wire import Wire
from wakeup_protocol import WakeupDevice, init_wakeup

if __name__ == "__main__":

    print("version 1.0")

    '''
    Example 
    configuration:
    [Device 1] --> [Device 2]

    purpose:
    device send "hello world" to device 2 at timestep 2

    
    '''
    time_steps = 13
    
    world_devices, world_wires = init_wakeup()

    # export data
    gen_json = GenerateJson(time_steps, world_devices, world_wires)
    gen_json.generate_initial_state_to_json()

    # simulate data
    sim = Simulator(time_steps, world_devices, world_wires, gen_json)
    sim.simulate()

