from simulation import Simulator
from generate_json import GenerateJson
from device import Device
from wire import Wire
from wakeup_protocol import WakeupDevice, init_wakeup
from routing import RoutingDevice, StartRoutingEvent, init_routing
from event import Events, StartEvent
from generator import update_outward_wires_for_devices

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
    
    world_devices, world_wires = init_routing()

    # update_outward_wires_for_devices(world_devices, world_wires)

    # add events to waking up
    events = Events()
    #events.add_event(StartEvent(world_devices[0], world_wires[0], "start"), 2)
    events.add_event(StartRoutingEvent(world_devices[0], world_devices[5], "start"), 2)

    # export data
    gen_json = GenerateJson(time_steps, world_devices, world_wires)
    gen_json.export_input_data_to_json()

    # simulate data
    sim = Simulator(time_steps, world_devices, world_wires, events, gen_json)
    sim.simulate()

