from device import Device, DeviceState
from wire import Wire
import random

# Gotcha, a better starting place would be a waking up protocol - typing it out rn
# Wake func: if not awake, sent awake variable true and message to wake message to neighbors

#On recieve func: call wake func

#Note: 
# *a device should have a variable “awake” initially set to false
# *a device at times et 0 should initially have awake message sent to it
# ^create awaking-device that inherits from device and override the Rec
# function w/ the “on receive func” noted above

#class WakeState(DeviceState):

def init_wakeup():
    
    devices, wires = randomized_devices_and_wires(2, 2)

    add_wires_to_all_devices(devices, wires)

    return devices, wires

def randomized_devices_and_wires(num_devices, num_wires, seed = 42):
    wires = {}
    devices = {}

    for i in range(0, num_devices):
        devices[i] = WakeupDevice(i)
    
    for i in range(0, num_wires):
        wires[i] = Wire(i, random.randint(0, num_devices), random.randint(0, num_devices-1), devices, random.randint(0, 10))

    return devices, wires

def add_wires_to_all_devices(devices, wires):
    for device in devices.values():
        for wire in wires.values():
            if(wire.get_send_device_id() == device.get_id()):
                device.add_wire(wire)

class WakeupDevice(Device):

    def __init__(self, id, name=""):
        super().__init__(id, name)
        self.awake = False
        self.wires = []
        if(name == "device " + str(id)):
            self.name = "wakeup device " + str(id)

    def add_wire(self, wire):
        self.wires.append(wire)

    def wakeup(self, content):
        self.awake = True
        print("device: " + self.name + " has been woken up")
        for wire in self.wires:
            self.send(wire, content)

    def receive(self, content):
        super().receive(content)
        self.wakeup(content)
        