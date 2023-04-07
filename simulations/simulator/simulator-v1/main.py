from simulation import Simulator
from generate_json import GenerateJson
from device import Device
from wire import Wire
from wakeup_protocol import WakeupDevice, init_wakeup
from event import Events, StartEvent

if __name__ == "__main__":

    print("version 1.0")

    '''
    Example 
    configuration:
    [Device 1] --> [Device 2]

    purpose:
    device send "hello world" to device 2 at timestep 2

    
    '''
    time_steps = 100
    
    world_devices, world_wires = init_wakeup()

    # add events to waking up
    events = Events()
    events.add_event(StartEvent(world_devices[0], world_wires[0], "wakeup"), 2)

    # export data
    gen_json = GenerateJson(time_steps, world_devices, world_wires)
    gen_json.export_input_data_to_json()

    # simulate data
    sim = Simulator(time_steps, world_devices, world_wires, events, gen_json)
    sim.simulate()

