from enum import Enum
from collections import deque

class DeviceState(Enum):
    empty = 0
    full = 1

class GlobalQueue:

    def processNext(self):
        function = self.global_queue.pop
        function.process()

    #def addEvent(timestamp: int)

    def __init__(self):
        self.global_queue = deque()

class Device:

    #def send(self, source: Device, buffer: int, dest: Device, timestamp: float) -> None:
    #    send_data = self.data
    #    self.data = None
    #    self.state = DeviceState.empty
    #    return send_data

    def send(self) -> int:
        send_data = self.data
        self.data = None
        self.state = DeviceState.empty
        return send_data

    def receive(self, buffer: int):
        self.data = buffer
        self.state = DeviceState.full

    def process(self):
        print(self.data)

    def __init__(self, id):
        self.id = id
        self.state = None
        self.data = None

def send(source: Device, buffer: int, dest: Device, timestamp: float) -> None:
    data = source.send()
    dest.receive(data)


device1 = Device(1)
device2 = Device(2)

device1.receive(10)
device1.process()
device2.process()
send(device1, 0, device2, 10)
device1.process()
device2.process()
