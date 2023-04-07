from collections import deque

# Simple event system, have a queue and pop through the queue to process
# an event at certain intervals
# NOTE: here we assume that all events in the queue are sorted chronologically
#          i.e. [(event1, 2), (event2, 2), (event3, 5)] 

class Event:
    
    def __init__(self, device, test = False):
        self.test_mode = test
        self.device = device

    def call(self):
        print("default event called")

class StartEvent(Event):
    
    def __init__(self, device, wire, content, test = False):
        super().__init__(device, test)
        self.wire = wire
        self.content = content

    def call(self):
        self.device.send(self.wire, self.content)
    

class Events:

    def __init__(self):
        self.event_queue = deque()

    def add_event(self, event, time):
        self.event_queue.append([event, time])

    def trigger_events(self, time):
        # check if the queue has time according to that time 
        while(len(self.event_queue) > 0 and self.event_queue[0][1] <= time):
            self.event_queue.pop()[0].call()

