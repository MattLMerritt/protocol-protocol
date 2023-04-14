import React from "react";

const I2C = () => {
  return (
    <div className="container">
      <div className="content">
        <div>
          <h1 id="the-i2c-communication-protocol">
            The I2C Communication Protocol
          </h1>
          <h2 id="description">Description</h2>
          <p>
            The I2C bus is a very popular and powerful bus used for
            communication between a master device and a single or multiple slave
            devices. Each device connected by I2C protocol can be both a sender
            and a receiver. Only the master device is able to start a request
            for data from a slave device or start sending data to a slave
            device. Each time the master device can only communicate with one
            slave device. Every device on the I2C bus has a unique address so
            that the master device can find a specific slave device to
            communicate. Usually, adding an extra device or removing a slave
            device doesn’t have any impact on other devices.{" "}
          </p>

          <h2 id="instructions">Instructions</h2>
          <p>
            I2C uses only two bidirectional wires to transmit data between
            devices: SDA (Serial Data): the line for the master and slave to
            send and receive data. SCL (Serial Clock): the line that carries the
            clock signal.{" "}
          </p>
          <p>
            To connect multiple devices by using I2C, make sure first that each
            device supports I2C protocol. Then connect them through the SDA and
            SCL wires pulled up with resistors. Typical voltages used for Vcc
            are +3.3 V or +5 V. Now you can write the code and upload your
            program to the master device. Find the hardware address for each
            slave device as well as the memory address of data by checking the
            datasheet of them so that the master device can send or request data
            from the specific slave device.
          </p>

          <h2 id="examples">Examples</h2>
          <p>
            The I2C (Inter-Integrated Circuit) communication protocol is
            commonly used in electronic devices for communication between
            integrated circuits, such as between microcontrollers and sensors,
            memory devices, and other peripherals. It is often used in
            applications such as embedded systems and industrial automation.
            Here is an example of how we can use I2C to connect a
            microcontroller and an ultrasonic ranger.{" "}
          </p>
          <pre>
            <code>
              <span className="hljs-meta">
                #<span className="hljs-meta-keyword">include</span>{" "}
                <span className="hljs-meta-string">&lt;Wire.h&gt;</span>
                {"  "}
                <span className="hljs-comment">
                  // Include the Wire library for I2C communication
                </span>
              </span>
              {"\n"}
              {"\n"}
              <span className="hljs-meta">
                #<span className="hljs-meta-keyword">define</span> LED_PIN 12
                {"  "}
                <span className="hljs-comment">
                  // Define the pin number for the LED
                </span>
              </span>
              {"\n"}
              {"\n"}
              <span className="hljs-keyword">void</span>{" "}
              <span className="hljs-built_in">setup</span>() {"{"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">begin</span>();{"  "}
              <span className="hljs-comment">
                // Initialize I2C communication
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Serial</span>.
              <span className="hljs-built_in">begin</span>(
              <span className="hljs-number">9600</span>);{"  "}
              <span className="hljs-comment">
                // Start serial communication at 9600 bps
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">pinMode</span>(LED_PIN,{" "}
              <span className="hljs-literal">OUTPUT</span>);{"  "}
              <span className="hljs-comment">
                // Set the LED pin as an output
              </span>
              {"\n"}
              {"}"}
              {"\n"}
              {"\n"}
              <span className="hljs-keyword">int</span> reading ={" "}
              <span className="hljs-number">0</span>, pre ={" "}
              <span className="hljs-number">0</span>;{"  "}
              <span className="hljs-comment">
                // Declare variables for the distance reading and previous
                reading
              </span>
              {"\n"}
              {"\n"}
              <span className="hljs-keyword">void</span>{" "}
              <span className="hljs-built_in">loop</span>() {"{"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">beginTransmission</span>(
              <span className="hljs-number">112</span>);{"  "}
              <span className="hljs-comment">
                // Begin I2C transmission with device address 0x70 (112 in
                decimal)
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">write</span>(
              <span className="hljs-keyword">byte</span>(
              <span className="hljs-number">0x00</span>));{"  "}
              <span className="hljs-comment">
                // Send command to start distance reading
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">write</span>(
              <span className="hljs-keyword">byte</span>(
              <span className="hljs-number">0x51</span>));{"  "}
              <span className="hljs-comment">
                // Specify the distance measurement unit
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">endTransmission</span>();{"  "}
              <span className="hljs-comment">// End I2C transmission</span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">delay</span>(
              <span className="hljs-number">70</span>);{"  "}
              <span className="hljs-comment">
                // Wait for measurement to complete
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">beginTransmission</span>(
              <span className="hljs-number">112</span>); {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">write</span>(
              <span className="hljs-keyword">byte</span>(
              <span className="hljs-number">0x02</span>));{"  "}
              <span className="hljs-comment">
                // Send command to read the distance data
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">endTransmission</span>();{"  "}
              <span className="hljs-comment">// End I2C transmission</span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">requestFrom</span>(
              <span className="hljs-number">112</span>,{" "}
              <span className="hljs-number">2</span>);{"  "}
              <span className="hljs-comment">
                // Request 2 bytes of data from the ultrasonic ranger
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">if</span> (
              <span className="hljs-number">2</span> &lt;={" "}
              <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">available</span>()) {"{"}
              {"  "}
              <span className="hljs-comment">
                // If 2 bytes are available to read
              </span>
              {"\n"}
              {"\n"}
              {"    "}reading = <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">read</span>();{"  "}
              <span className="hljs-comment">// Read the first byte (MSB)</span>
              {"\n"}
              {"\n"}
              {"    "}reading = reading &lt;&lt;{" "}
              <span className="hljs-number">8</span>;{"  "}
              <span className="hljs-comment">
                // Shift the first byte to the left by 8 bits
              </span>
              {"\n"}
              {"\n"}
              {"    "}reading |= <span className="hljs-built_in">Wire</span>.
              <span className="hljs-built_in">read</span>();{"  "}
              <span className="hljs-comment">
                // Read the second byte (LSB) and combine it with the first byte
              </span>
              {"\n"}
              {"\n"}
              {"    "}
              <span className="hljs-built_in">Serial</span>.
              <span className="hljs-built_in">println</span>(reading);{"  "}
              <span className="hljs-comment">
                // Print the distance reading
              </span>
              {"\n"}
              {"\n"}
              {"    "}
              <span className="hljs-built_in">if</span> (reading &lt;={" "}
              <span className="hljs-number">20</span> &amp;&amp; pre &gt;{" "}
              <span className="hljs-number">20</span>) {"\n"}
              {"      "}
              <span className="hljs-built_in">digitalWrite</span>(LED_PIN,{" "}
              <span className="hljs-literal">HIGH</span>);{"  "}
              <span className="hljs-comment">
                // If the distance drops below 20, turn on the LED
              </span>
              {"\n"}
              {"\n"}
              {"    "}
              <span className="hljs-built_in">else</span>{" "}
              <span className="hljs-built_in">if</span> (reading &gt;{" "}
              <span className="hljs-number">20</span> &amp;&amp; pre &lt;={" "}
              <span className="hljs-number">20</span>) {"\n"}
              {"      "}
              <span className="hljs-built_in">digitalWrite</span>(LED_PIN,{" "}
              <span className="hljs-literal">LOW</span>);{"  "}
              <span className="hljs-comment">
                // If the distance rises above 20, turn off the LED
              </span>
              {"\n"}
              {"\n"}
              {"    "}pre = reading;{"  "}
              <span className="hljs-comment">
                // Set the previous reading to the current reading
              </span>
              {"\n"}
              {"\n"}
              {"  "}
              {"}"}
              {"\n"}
              {"  "}
              <span className="hljs-built_in">delay</span>(
              <span className="hljs-number">200</span>);{"  "}
              <span className="hljs-comment">
                // Wait for a short time before taking the next temperature
                reading
              </span>
              {"\n"}
              {"}"}
              {"\n"}
            </code>
          </pre>
        </div>
      </div>
    </div>
  );
};

export default I2C;
