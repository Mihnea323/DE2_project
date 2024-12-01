# DE2_project🤍

### Team Members
- Arseni Mihnea-Cristian
- Olariu Lenuța-Maria
- Radu Anca-Valentina
- Voican Delia

## Theoretical Description of the Project
  &nbsp;&nbsp;&nbsp;Our project consists of a GPS tracker that integrates an ESP-WROOM-32 board with a GPS module, I2C temperature and humidity sensor, and an OLED display to monitor location and environmental data in real time. The GPS module provides latitude, longitude, and altitude via UART, while the sensor measures temperature and humidity over I2C. The ESP32 processes this data and displays it on the OLED screen.

## Circuit Diagram
![Circuit Diagram](https://github.com/Mihnea323/DE2_project/blob/main/images/diagram.png) <br>

## Hardware Description
  &nbsp;&nbsp;&nbsp;Our hardware setup includes:
  - **Microcontroller** (ESP-32): acts as the central processing unit, interfacing with the GPS module, temperature and humidity sensor, and the OLED display. <br>
    FireBeetle Board- ESP32 integrates a Dual-Core ESP-WROOM-32 module, which supports MCU and Wi-Fi & Bluetooth dual-mode communication. <br>
    The ESP32 microcontroller board has a number of GPIO (General Purpose Input/Output) pins that can be used for various purposes, such as digital input and output, analog input, communication interfaces (e.g., UART, SPI, I2C), PWM (Pulse Width Modulation) output, and more. <br> <br>
    ![esp32](https://github.com/Mihnea323/DE2_project/blob/main/images/DFR0478_pinout3.png) <br>
  - **GPS module** (NEO-6M-0-001): receives signals from GPS satellites to compute geographical location, it provides the longitude, latitude and altitude. <br>
    The **NEO-6M-0-001** is a GPS module commonly used in embedded systems for accurate positioning and navigation. It features the NEO-6M chipset, offering high sensitivity and quick acquisition times. It supports GPS and is capable of providing real-time location data with a high level of precision. The module communicates via UART and can be easily integrated with microcontrollers like ESP32. It operates with a voltage range of 3.3V to 5V and is widely used in applications such as robotics, drones, and vehicle tracking systems. <br> <br>
    ![gps](https://github.com/Mihnea323/DE2_project/blob/main/images/gps.jpg) <br>
  - **I2C temperature/humidity sensor** (DHT12): measures ambient temperature and humidity and transmits the data digitally via the I2C bus. <br>
    The **DHT12** is a digital temperature and humidity sensor that communicates via the I2C protocol. It provides accurate measurements of temperature (with a range of -20°C to 60°C) and humidity (0% to 100% RH) with a high degree of reliability. The sensor operates at a voltage of 3.3V to 5V and outputs data in a 2-wire I2C format, making it easy to interface with microcontrollers like ESP32.<br> <br>
    ![sensor](https://github.com/Mihnea323/DE2_project/blob/main/images/sensor.jpg) <br>
  - **OLED display** (SH1106 I2C): displays the GPS data and the environmental data. <br>
    The **SH1106** is an OLED display controller that supports the I2C communication protocol. It is typically used with small, low-power OLED displays, offering a resolution of 128x128 or 128x64 pixels, depending on the specific model. The SH1106 provides high contrast and sharp images with deep blacks, as it does not require a backlight, making it energy-efficient. It operates at a voltage of 3.3V to 5V and is commonly used in projects where space and power efficiency are important, such as portable devices, wearables, and microcontroller-based systems like ESP32. <br> <br>
    ![oled](https://github.com/Mihnea323/DE2_project/blob/main/images/oled2.webp) <br>

## Software Description
The software consists of several classes.

#### 1. I2C class
   &nbsp;&nbsp;&nbsp;This class simplifies communication with I2C-enabled devices like the OLED display and temperature/humidity sensor. It ensures smooth and efficient integration of peripherals with minimal wiring and code complexity. <br>
   **Example of usage**: i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
#### 2. SH1106 class
   &nbsp;&nbsp;&nbsp;This class is used for communication with the OLED, which is used to display the longitude, latitude, altidude, as well as temperature and humidty. <br>
    **Example of usage**: oled = SH1106_I2C(i2c) <br>
    **Source file**: [sh1106.py](https://github.com/Mihnea323/DE2_project/blob/main/src/sh1106.py)
#### 3. DHT12 class
   &nbsp;&nbsp;&nbsp;This class is designed to interface with the temperature/humidity sensor. It continuously reads environmental conditions and display them on the OLED screen alongside GPS data. <br>
    **Example of usage**: sensor = dht12.DHT12(i2c) <br>
    **Source file**: [dht12.py](https://github.com/Mihnea323/DE2_project/blob/main/src/dht12.py)
#### 4. MicropyGPS class
   &nbsp;&nbsp;&nbsp;The code processes GPS NMEA sentences received from a GPS module, parses them character by character, validates them, and extracts useful information like location, time, speed, and satellite data. It converts latitude and longitude between decimal degrees, degrees-minutes-seconds, and other formats and determines the cardinal direction based on the course. <br>
   &nbsp;&nbsp;&nbsp;How the code works:
   - **Sentence parsing**: each character of a GPS sentence is passed to ***update***, then the ***update*** method segments the sentence and validates it.
   - **Validation**: checks if the checksum matches to ensure no data corruption and if valid, parses the sentence type and extracts relevant data.
   - **Data storage**: updates attributes like ***latitude***, ***longitude***, ***altitude***, etc. <br>
   
 **Example of usage**: my_gps = MicropyGPS() <br>
 **Source file**: [micropyGPS.py](https://github.com/Mihnea323/DE2_project/blob/main/src/micropyGPS.py)

## FlowCharts
### 1. FlowChart for the main code
![flowchart1](https://github.com/Mihnea323/DE2_project/blob/main/images/flowchart2.jpg)

### 2. FlowChart for the MicropyGPS class
![flowchart2](https://github.com/Mihnea323/DE2_project/blob/main/images/flowchart1.jpg)
   
## Instructions and Photos
### 1. Circuit Setup
Firstly we would have to connect the components to the breadboard and to the microcontroller using jumper wires. <br>
- **GPS Module NEO-6M-0-001** <br>
  - connect Tx to Rx using GPIO16 on ESP32
  - connect Rx to Tx using GPIO17 on ESP32
  - connect Vcc to 3V3 pin on ESP32
  - connect GND to GND on ESP32
- **I2C Temperature and Humidity Sensor DHT12** <br>
  - connect SDA to GPIO21 on ESP32
  - connect SCL to GPIO22 on ESP32
  - connect Vcc to 3V3 pin on ESP32
  - connect GND to GND pin on ESP32
- **OLED Display SH1106** <br>
  - connect SDA to GPIO21 on ESP32
  - connect SCL to GPIO22 on ESP32
  - connect Vcc to 3V3 pin on ESP32
  - connect GND to GND pin on ESP32
 
### 2. Install Required Libraries 
To run the code correctly, we would have to install the following libraries on the microcontroller ESP32: <br>
- for the OLED Display: [sh1106.py](https://github.com/Mihnea323/DE2_project/blob/main/src/sh1106.py)
- for the I2C Temperature/Humidity Sensor:  [dht12.py](https://github.com/Mihnea323/DE2_project/blob/main/src/dht12.py)
- for the GPS Module: [micropyGPS.py](https://github.com/Mihnea323/DE2_project/blob/main/src/micropyGPS.py)

### 3. Run the Main Code
Lastly, we would have to write the main code and run it. Here is the main code: <br>
``` MicroPython
import machine
from time import sleep
from micropyGPS import MicropyGPS
from machine import I2C
from machine import Pin
from sh1106 import SH1106_I2C

import time
import dht12

# Instantiate the micropyGPS object
my_gps = MicropyGPS()
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
print(f"I2C configuration : {str(i2c)}")

# Init OLED display
oled = SH1106_I2C(i2c)
sensor = dht12.DHT12(i2c)

# Define the UART pins and create a UART object
gps_serial = machine.UART(2, baudrate=9600, tx=17, rx=16)

while True:
    try:
        while gps_serial.any():
            data = gps_serial.read()
            for byte in data:
                stat = my_gps.update(chr(byte))
                if stat is not None:
                    # Print parsed GPS data
                    
                    oled.text(f"Lat:{my_gps.latitude_string()}",0,0 )
                    print('Latitude:', my_gps.latitude_string())
                    print('Longitude:', my_gps.longitude_string())
                    oled.text(f"Alt: {my_gps.altitude}",0,20)
                    print('Altitude:', my_gps.altitude)
                    oled.text(f"Long:{my_gps.longitude_string()}",0,10)
                    
                    temp, humidity = sensor.read_values()
                    print(f"Temperature: {temp}°C, Humidity: {humidity}%")
                    
                    oled.text(f"Temperature:{temp}", 0, 40)
                    oled.text(f"Humidity:{humidity}", 0, 52)
                    oled.text("*",0,30)
                    
                    oled.show()
                    oled.fill(0)
                    time.sleep(5)
     
            
    except Exception as e:
        print(f"An error occurred: {e}")

```
### 4. Test the Circuit
To test the GPS tracker, first we would have to power the ESP32 using a Micro-USB and then run the code. <br>
To make sure that we get data, we will have to place the circuit next to a window and most likely wait a few minutes until it can get data from the satelites. When it's ready, the NEO-6M GPS module’s LED will start blinking. 

### 5. Troubleshooting
- **If the GPS is not getting the signal**: Ensure you're in an open space with a clear view of the sky. You may also try increasing the baud rate or adjusting your GPS library.
- **If the OLED is not displaying**: Check the I2C connections and verify the screen is properly powered. Ensure the correct I2C address is being used.
- **If there are issues with the DHT12 sensor**: Make sure the I2C address matches and the sensor is properly connected.

### 6. Photos and Videos of the Circuit
![circuit](https://github.com/Mihnea323/DE2_project/blob/main/images/circuit.jpg) <br> <br>
![circuit2](https://github.com/Mihnea323/DE2_project/blob/main/images/circuit2.jpg)
## References and Tools

