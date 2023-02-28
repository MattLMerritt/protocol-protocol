from enum import Enum
from collections import deque
import random

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

# input seed: 42
input_seed = 42
random.seed(input_seed)

# total devices
total_devices = 10
devices = []
for i in range(total_devices): 
    devices.append(Device(i))

# range of time
start_time_range = [0, 5]
stay_time_range = [0, 5]

# generate information tuple to send from CPU: ((send_time, (buffer, stay_time)), ...)
total_information_to_send = 100
buffers = deque()
random_start_time = 0
for i in range(total_information_to_send):
    # create a random buffer
    buffer = random.randint(0, 64)
    random_start_time += random.randint(start_time_range[0], start_time_range[1])
    buffers.append((random_start_time, (bin(buffer), random.randint(stay_time_range[0], stay_time_range[1]))))

# print(buffers)

while(buffers.count() > 0):
    if((buffers.index(0)))