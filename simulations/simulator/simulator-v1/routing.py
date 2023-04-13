from device import Device
from wire import Wire

def add_undirected_wire(i, device_one : Device, device_two : Device, devices):
    wire_one = Wire(i, device_one.get_id(), device_two.get_id(), devices, 1)
    wire_two = Wire(i + 1, device_two.get_id(), device_one.get_id(), devices, 1)
    return wire_one, wire_two

def init_routing():
    wires = {}
    devices = {}

    # example graph will be a cycle from 1 -> 2 -> 3 -> 4 -> 5 -> 1
    for i in range(0, 5):
        devices[i] = RoutingDevice(i)

    for i in range(0, 10, 2):
        wire_one, wire_two = add_undirected_wire(i, devices[i], devices[i+1], devices)
        wires[i] = wire_one
        wires[i + 1] = wire_two

    wires[9], wires[10] = add_undirected_wire(9, devices[0], devices[4], devices)



    return devices, wires

# 

class RoutingDevice(Device):

    def __init__(self, id, name=""):
        super().__init__(id, name)
        self.awake = False
        self.routing_table = {}
        if(name == "device " + str(id)):
            self.name = "routing device " + str(id)

    def add_routing(self, dev: Device, path):
        self.routing_table[dev.get_id()] = path

    def receive(self, content):
        super().receive(content)

