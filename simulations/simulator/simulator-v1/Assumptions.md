# Simulator Assumptions:

## Overview

The simulator-v0 is a protocol simulator that runs by simulating devices and wire state on a step-by-step basis. At each step the simulator facilitates interactions between devices through wires. A wire exists between each device and carries messages between. To visualize the interactions between wires and devices a intermediate format is created and passed to a visualizer program. The parts of the simulator program are as follows:

1. Define setup (devices and wires)
2. Start step-by-step Loop
3. Package contents for visualizer

During the step by step loop, the states are retrieved from the devices and wires. The structure of the step-by-step loop places the requirement of routing messages to the structure of the graph (aka wires). The requirement of message handling is also the job of a particular wire.

This simulator format is best used for visualizing routing algorithms.

### Devices:

The possible states that a device and wire are bounded. The possible states of a device are as follows:

* IDLE = 0
* SENDING = 1
* RECEIVING = 2
* SENDING_AND_RECEIVING = 3

For different algorithms, different types of devices may be substituted in for use. 
<TODO: note types of algorithms that can be used as devices>

### Wires:

A wire requires two devices with a "source end" and a "target end" of the wire specified. 
<TODO: note FIFO structure of wires>
The possible states for a wire is as follows:

* EMPTY
* IN_USE

The current version of wires do not provide messages to devices if the other end goes down/becomes non-functional. As devices going "down" is not currently supported, all devices are assumed to always be on and functioning.




## Structure

## Assumptions