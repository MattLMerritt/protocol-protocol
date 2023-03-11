
"""
Stateful Framework data flow:

1. Define setup (devices and wires)
2. Start processing Loop
3. Package contents for visualizer

Notes:
The structure of the processing loop is as follows:
- Check status of each wire and if there is a message at the "end" of a wire then it should call "receive" on the device at the rec end of the wire
- Check each device if any device is sending anything


The structure of this approach places importance on sending data to intermediate handlers (e.g. wires) to keep track of message status
instead of having a global queue that handles the status of message and routing of the message.

"""

import device
import wire


if __name__ == "__main__":

    print("hello world")
