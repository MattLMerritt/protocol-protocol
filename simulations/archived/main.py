from enum import Enum
from collections import deque
from heapq import heapify, heappush, heappop
from device import Device

class EventState(Enum):
    IDLE = 0
    SENDING = 1
    RECEIVING = 2
    SENDING_AND_RECEIVING = 3

class Event:

    def __init__(self, event_type, device: Device, timestamp):
        self.event_type = event_type
        self.timestamp = timestamp
        self.device = device
    
    def process_device(self):
        self.device.process()
    
    def __lt__(self, next):
        return self.timestamp < next.timestamp

class GlobalQueue:

    def __init__(self):
        self.global_queue = []
        heapify(self.global_queue)
    
    def addEvent(self, event: Event):
        self.global_queue.append(event)
        heapify(self.global_queue)

    def processNext(self):
        event = heappop(self.global_queue)
        event.process_device()

    #def addEvent(timestamp: int)

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

    def receive(self, buffer: tuple[int, int]):
        self.data = buffer
        self.state = DeviceState.full
        self.timer = buffer

    def process(self):
        print(self.data)

    def __init__(self, id):
        self.id = id
        self.state = None
        self.data = None
        self.timer = 0



#    82     19       8
#[[1000], [1001], [1011]]

#UART1 UART2

#UART2.rec([queue]) -> remove from the queue and process [1000]

#rec([1000])

class Logger():
    def __init__(self):
        print("hi")

    def write(self):
        print("write info")

def send(source: Device, buffer: int, dest: Device, timestamp: float) -> None:
    data = source.send()
    dest.receive(data)


#device1 = Device(1)
#device2 = Device(2)

#device1.receive(10)
#device1.process()
#device2.process()
#send(device1, 0, device2, 10)
#device1.process()
#device2.process()

