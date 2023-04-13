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

    # example graph will be a cycle from 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 1
    for i in range(0, 8):
        devices[i] = RoutingDevice(i)

    j = 0
    for i in range(0, 14, 2):
        wires[i], wires[i + 1] = add_unweighted_undirected_wire(i, devices[j], devices[j+1], devices)
        j += 1

    wires[14], wires[15] = add_unweighted_undirected_wire(9, devices[0], devices[7], devices)

    for device in devices.values():
        device.print_device()

    for wire in wires.values():
        wire.print_wire()
    
    graph = create_adjacency_list(devices, wires)

    create_routing_table(graph, devices[0])
    devices[0].print_routing_table()

    return devices, wires

def create_adjacency_list(devices, wires):
    graph = {}
    for device_id in devices:
        graph[device_id] = []
    
    for wire in wires.values():
        graph[wire.get_rec_device_id()].append(wire.get_send_device_id())

    return graph

def create_routing_table(graph, device : Device):

    visited = []
    queue = deque()

    visited.append(device.get_id())
    queue.append(device.get_id())

    while queue:
        s = queue.popleft() 
        for node in graph[s]:
            if node not in visited:
                # if the previous node is the same as the starting node we just add the routing to itself
                if s is device.get_id():
                    device.add_routing(node, node)
                else:
                    device.add_routing(node, s)
                visited.append(node)
                queue.append(node)

class RoutingDevice(Device):

    def __init__(self, id, name=""):
        super().__init__(id, name)
        self.awake = False
        self.routing_table = {}
        if(name == "device " + str(id)):
            self.name = "routing device " + str(id)

    def add_routing(self, target_device_id, from_device_id):
        self.routing_table[target_device_id] = from_device_id

    def receive(self, content):
        super().receive(content)
    
    def print_routing_table(self):
        print(f"==== Routing Table for device {self.id} ====")
        for key, value in self.routing_table.items():
            print(f"{key} : {value}")
        print(f"============================================")

    #def send(self, wire, content):
    #    self.routing_table[] super().send(wire, content)

