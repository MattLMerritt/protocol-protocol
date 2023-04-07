import React from "react";

const Uart = () => {
  return (
    <div className="container">
      <div className="content">
        <h1>Universal Asynchronous Receiver/Transmitter (UART) Protocol</h1>

        <p id="description">
          The Universal Asynchronous Receiver/Transmitter (UART) is a computer
          hardware communication protocol that supports asynchronous serial
          communication, meaning that the endpoints of communication are not
          synchronized by a common clock signal.
        </p>
        <p>
          UART only requires two wires, one for transmitting and one for
          receiving, along with a ground connection. The protocol supports three
          modes of communication:
        </p>
        <ul>
          <li>Simplex: data sent in one direction only</li>
          <li>
            Half-duplex: data can be sent in both directions, but not at the
            same time
          </li>
          <li>Full duplex: both sides can transmit data simultaneously</li>
        </ul>
        <p>
          Each UART has settings for the transmission speed (baud/s), data
          length/structure, and the use of START and STOP bits. Setting
          configurations must be the same on both the transmitter and receiver
          in order to establish communication. For example, since they don't
          share a clock, each terminal must transmit at the same predetermined
          speed.
        </p>
        <p>
          UART was one of the earliest serial communication protocols and was
          once used to connect typewriters to operator consoles. Though its
          popularity is decreasing as its usage by modern computers is being
          mostly replaced by alternatives such as Ethernet and USB. However,
          UART is still widely used in embedded systems, microcontrollers and
          other low-speed applications due to its low cost and simple
          implementation.
        </p>
        <h2 id="examples">Examples</h2>
        <p>
          UART is used in various applications such as GPS Receivers, Bluetooth
          Modules, GSM, GPRS Modems, Wireless Communication Systems, and
          RFID-based applications.
        </p>
        <h2 id="instructions">Instructions</h2>
        <p>The following steps illustrate how UART works:</p>
        <ol>
          <li>
            At the start of the UART simulation, the line is held high in an
            idle state to detect damaged wires.
          </li>
          <li>
            A start bit indicates when data is coming. It is a transition from
            the high idle state to a low state.
          </li>
          <li>
            The data bits are read. The data bits can be either 0 or 1, where 1
            indicates high voltage or a high state, and 0 indicates a low
            voltage and therefore a lower state.
          </li>
          <li>
            The data bits are usually 5 to 9 bits in length and are translated
            in the order of LEAST SIGNIFICANT BIT, or LSB, where the least
            significant bit is translated first from the user data and so on.
          </li>
          <li>
            A parity bit can be used for error detection. The parity bit will be
            0 if the number of 1 bits in the user data is even. The parity bit
            will be 1 if the number of 1 bits in the user data is odd. (This
            step is optional)
          </li>
          <li>
            The stop bit indicates the end of user data. It is a transition back
            to the high or even remain at the idle state as well.
          </li>
        </ol>
        <h2>Example of how the ASCII char ‘S’ is read with UART:</h2>
        <p>
          <img src="images/image1.png" alt="UART Simulation" />
        </p>
        <p>
          <em>
            Reference:{" "}
            <a href="https://www.youtube.com/watch?v=sTHckUyxwp8" target="_new">
              https://www.youtube.com/watch?v=sTHckUyxwp8
            </a>
          </em>
        </p>
      </div>
    </div>
  );
};

export default Uart;
