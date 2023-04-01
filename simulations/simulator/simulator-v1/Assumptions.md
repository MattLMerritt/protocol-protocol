# Simulator Assumptions:

## Overview

The simulator-v0 is a protocol simulator that runs by simulating devices and wire state on a step-by-step basis. At each step the simulator facilitates interactions between devices through wires. A wire exists between each device and carries messages between. To visualize the interactions between wires and devices a intermediate format is created and passed to a visualizer program. The parts of the simulator program are as follows:

1. Define setup (devices and wires)
2. Start step-by-step Loop
3. Package contents for visualizer

During the step by step loop, the states are retrieved from the devices and wires. The possible states that a device and wire are bounded. The possible states of a wire are 

* IDLE = 0
* SENDING = 1
* RECEIVING = 2
* SENDING_AND_RECEIVING = 3

The possible states for a wire is as follows:

* EMPTY
* IN_USE


## Structure

## Assumptions