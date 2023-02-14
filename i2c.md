### The I2C Communication Protocol


#### Description

The I2C bus is a very popular and powerful bus used for communication between a master device and a single or multiple slave devices. Each device connected by I2C protocol can be both a sender and a receiver. Only the master device is able to start a request for data from a slave device or start sending data to a slave device. Each time the master device can only communicate with one slave device. Every device on the I2C bus has a unique address so that the master device can find a specific slave device to communicate. Usually, adding an extra device or removing a slave device doesn’t have any impact on other devices. 


----------

#### Instructions

I2C uses only two bidirectional wires to transmit data between devices:
SDA (Serial Data): the line for the master and slave to send and receive data.
SCL (Serial Clock): the line that carries the clock signal. 

To connect multiple devices by using I2C, make sure first that each device supports I2C protocol. Then connect them through the SDA and SCL wires pulled up with resistors. Typical voltages used for Vcc are +3.3 V or +5 V. Now you can write the code and upload your program to the master device. Find the hardware address for each slave device as well as the memory address of data by checking the datasheet of them so that the master device can send or request data from the specific slave device.  

----------

#### Examples

The I2C (Inter-Integrated Circuit) communication protocol is commonly used in electronic devices for communication between integrated circuits, such as between microcontrollers and sensors, memory devices, and other peripherals. It is often used in applications such as embedded systems and industrial automation.
Here is an example of how we can use I2C to connect a microcontroller and an ultrasonic ranger. 

```
#include <Wire.h>  // Include the Wire library for I2C communication

#define LED_PIN 12  // Define the pin number for the LED

void setup() {
  Wire.begin();  // Initialize I2C communication

  Serial.begin(9600);  // Start serial communication at 9600 bps

  pinMode(LED_PIN, OUTPUT);  // Set the LED pin as an output
}

int reading = 0, pre = 0;  // Declare variables for the distance reading and previous reading

void loop() {
  Wire.beginTransmission(112);  // Begin I2C transmission with device address 0x70 (112 in decimal)

  Wire.write(byte(0x00));  // Send command to start distance reading

  Wire.write(byte(0x51));  // Specify the distance measurement unit

  Wire.endTransmission();  // End I2C transmission

  delay(70);  // Wait for measurement to complete

  Wire.beginTransmission(112); 

  Wire.write(byte(0x02));  // Send command to read the distance data

  Wire.endTransmission();  // End I2C transmission

  Wire.requestFrom(112, 2);  // Request 2 bytes of data from the ultrasonic ranger

  if (2 <= Wire.available()) {  // If 2 bytes are available to read

    reading = Wire.read();  // Read the first byte (MSB)

    reading = reading << 8;  // Shift the first byte to the left by 8 bits

    reading |= Wire.read();  // Read the second byte (LSB) and combine it with the first byte

    Serial.println(reading);  // Print the distance reading

    if (reading <= 20 && pre > 20) 
      digitalWrite(LED_PIN, HIGH);  // If the distance drops below 20, turn on the LED

    else if (reading > 20 && pre <= 20) 
      digitalWrite(LED_PIN, LOW);  // If the distance rises above 20, turn off the LED

    pre = reading;  // Set the previous reading to the current reading

  }
  delay(200);  // Wait for a short time before taking the next temperature reading
}
```
