import collections

# Simple event system, have a queue and pop through the queue to process
# an event at certain intervals
# NOTE: here we assume that all events in the queue are sorted chronologically
#          i.e. [(event1, 2), (event2, 2), (event3, 5)] 

class Event:
    ...

class StartEvent(Event):
    
    call():
        super.call()
        device.send()
    
class RecieveEvent(Event):
    call():
        super.call()
        device.wakeup()

class Events:

    def __init__(self):
        event_queue = queue()

        [(Event, 2), (RecieveEvent, 2), (SendEvent, 5)] 


    def trigger_event(self):

