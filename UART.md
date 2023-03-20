
```


# DESCRIPTION

```

* `Universal synchronous receiver / transmitter`
* `Asynchronous Serial communication`
    * `Serial Meaning it sends data one bit following another`
    * `Asynchronous meaning that the endpoints of communication are not synchronized by a common clock signal`
    * `Thus both must transmit at the same (known) speed most commonly`
    * `From least sig to most`
* `3 Modes of communication:`
    * `Simplex: data sent in one direction only`
    * `Half-duplex: where data can be sent in each direction, though not simultaneously `
    * `Full duplex: both sides can transmit simultaneously`
* `Only needs 2 wires: one for transmitting one for receiving (in addition to a ground connection)`
* `UART have a shift register to convert the parallel data it receives to serial data it can transmit`
* `UART is one of the earliest computer hardware communication protocols.`
    * `Once used to connect typewriters to operators`
    * ` Still used today mainly in embedded systems and microcontrollers`
    * `Very simple, low cost, easy to implement`
* `Each transmitter and receiver must have the same configuration`
    * `Transmission speed (commonly 9600 bauds /s)`
    * `Data length`
    * `START and STOP Bits`


```
The Universal Asynchronous Receiver/Transmitter (UART) is a computer hardware communication protocol. Asynchronous meaning that the endpoints of communication are not synchronized by a common clock signal, and serial, meaning that data sent one bit at a time. 

UART only requires two wires, one for transmitting and one for receiving, along with a ground connection. The UART protocol supports three modes of communication: simplex (data sent in one direction only), half-duplex (data can be sent in both directions, but not at the same time), and full-duplex (both sides can transmit data simultaneously). 

Each UART has settings for the transmission speed (baud/s), data length/structure, and the use of START and STOP bits. Setting configurations must be the same on both the transmitter and receiver in order to establish communication. For example, since they don't share a clock, each terminal must transmit at the same predetermined speed. 

UART was one of the earliest serial communication protocols and was once used to connect typewriters to operator consoles. Though its popularity is decreasing as its usage by modern computers is being mostly replaced by alternatives such as Ethernet and USB. However, UART is still widely used in embedded systems, microcontrollers and other low-speed applications due to its low cost and simple implementation.
```


**Examples:**



* UART is used in applications such as:
    * GPS Receivers,
    * Bluetooth Modules
    * GSM
    * GPRS Modems
    * Wireless Communication Systems
    * RFID based applications

**Instructions:**



1. At the start of the UART simulation, the line is held high in an idle state. This helps with detecting damaged wires
2. Then there will be a start bit. Start bits indicate when data is coming. It is a transition from the high idle state to a low state.
3. Then the data bits are read. The data bits can be either 0 or 1, where 1 indicates high voltage or a high state, and 0 indicates a low voltage and therefore a lower state.
4. The data bits are usually 5 to 9 bits in length and are translated in the order of LEAST SIGNIFICANT BIT, or LSB, where the least significant bit is translated first from the user data and so on.
5. **NOTE THIS STEP IS OPTIONAL: **a parity bit can be used for error detection. The parity bit will be 0 if the number of 1 bits in the user data is even. The parity bit will be 1 if the number of 1 bits in the user data is odd. 
6. The next and last step of the UART simulation is when the stop bit comes up. The stop bit indicates the end of user data. It is a transition back to the high or even remain at the idle state as well.

**EXAMPLES OF UART SIMULATION ON THE NEXT PAGE:**

**The general flow of UART:**

**Example of how the ASCII char ‘S’ is read with UART:**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


**Reference: https://www.youtube.com/watch?v=sTHckUyxwp8**