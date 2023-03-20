# UART

**_Universal Asynchronous Receiver/Transmitter (UART)_** is a computer hardware communication protocol.[ <u>Asynchronous</u>](https://en.wikipedia.org/wiki/Asynchronous_communication) meaning that the endpoints of communication are not synchronized by a common clock signal, and [ <u>Serial</u>](), meaning that data is sent one bit at a time.

UART only requires two wires, one for transmitting and one for receiving, along with a ground connection. The UART protocol supports three modes of communication: simplex (data sent in one direction only), half-duplex (data can be sent in both directions, but not at the same time), and full-duplex (both sides can transmit data simultaneously).

Each UART has settings for the transmission speed (baud/s), data length/structure, and the use of START and STOP bits. Setting configurations must be the same on both the transmitter and receiver in order to establish communication. For example, since they don’t share a clock, each terminal must transmit at the same predetermined speed.

### History:

UART was one of the earliest serial communication protocols and was once used to connect typewriters to operator consoles. Though its popularity is decreasing as its usage by modern computers is being mostly replaced by alternatives such as Ethernet and USB. However, UART is still widely used in embedded systems, microcontrollers and other low-speed applications due to its low cost and simple implementation.
