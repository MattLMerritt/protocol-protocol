from device import Device, DeviceState
from wire import Wire

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
    wires = {}
    devices = {}

    wires_inc_device_info = {}
    
    for i in range(5):
        devices[i] = WakeupDevice(i)
    
    wires[0] = Wire(0, 0, 1, devices, 1)
    #wires_inc_device_info[0] = {0, 1, wires[0]}
    wires[1] = Wire(1, 1, 2, devices, 2)
    #wires_inc_device_info[1] = {1, 2, wires[1]}
    wires[2] = Wire(2, 1, 3, devices, 5)
    #wires_inc_device_info[2] = {1, 3, wires[2]}
    wires[3] = Wire(3, 2, 4, devices, 1)
    #wires_inc_device_info[3] = {2, 4, wires[3]}
    wires[4] = Wire(4, 3, 5, devices, 1)
    #wires_inc_device_info[4] = {3, 5, wires[4]}

    add_wires_to_all_devices(devices, wires)

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
        