from device import Device
from wire import Wire
from collections import deque

def add_unweighted_undirected_wire(i, device_one : Device, device_two : Device, devices):
    wire_one = Wire(i, device_one.get_id(), device_two.get_id(), devices, 1)
    wire_two = Wire(i + 1, device_two.get_id(), device_one.get_id(), devices, 1)
    return wire_one, wire_two

def init_routing():
    wires = {}
    devices = {}

    # example graph will be a cycle from 1 -> 2 -> 3 -> 4 -> 5 -> 1
    for i in range(0, 5):
        devices[i] = RoutingDevice(i)

    j = 0
    for i in range(0, 8, 2):
        wires[i], wires[i + 1] = add_unweighted_undirected_wire(i, devices[j], devices[j+1], devices)
        j += 1

    wires[8], wires[9] = add_unweighted_undirected_wire(9, devices[0], devices[4], devices)

    for device in devices.values():
        device.print_device()

    for wire in wires.values():
        wire.print_wire()

    return devices, wires

# 

#def create_routing_tables(devices, wires):
#    break

#def create_routing_table(device):

def bfs(node):

    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }

    visited = [] # List to keep track of visited nodes.
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft(0) 
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

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

    #def send(self, wire, content):
    #    self.routing_table[] super().send(wire, content)

