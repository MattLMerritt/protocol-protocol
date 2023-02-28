from collections import deque
import random
import device

# creates a bunch of devices
class Generator:
    def __init__(self):
        # input seed: 42
        input_seed = 42
        random.seed(input_seed)

        # total devices
        total_devices = 10
        devices = []
        #for i in range(total_devices):
        #    device = Device()
        #    device 
        #    devices.append()

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

        #while(buffers.count() > 0):
        #    if((buffers.index(0)))