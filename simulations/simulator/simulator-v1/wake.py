from device import Device, DeviceState

# Gotcha, a better starting place would be a waking up protocol - typing it out rn
# Wake func: if not awake, sent awake variable true and message to wake message to neighbors

#On recieve func: call wake func

#Note: 
# *a device should have a variable “awake” initially set to false
# *a device at times et 0 should initially have awake message sent to it
# ^create awaking-device that inherits from device and override the Rec
# function w/ the “on receive func” noted above

#class WakeState(DeviceState):


class Wake(Device):

    def __init__(self, id, wires, name=""):
        super().__init__(id, name)
        self.awake = False
        self.wires = wires

    def wakeup(self):
        self.awake = True

    def receive(self, content):
        super().receive(content)
        for wire in self.wires:
            self.send(wire, content)
        