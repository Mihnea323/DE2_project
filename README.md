# DE2_project🤍

### Team Members
- Arseni Mihnea-Cristian
- Olariu Lenuța-Maria
- Radu Anca-Valentina
- Voican Delia

## Theoretical Description of the Project
  &nbsp;&nbsp;&nbsp;Our project consists of a GPS tracker that integrates an ESP-WROOM-32 board with a GPS module, I2C temperature and humidity sensor, and an OLED display to monitor location and environmental data in real time. The GPS module provides latitude, longitude, and altitude via UART, while the sensor measures temperature and humidity over I2C. The ESP32 processes this data and displays it on the OLED screen.

## Circuit Diagram
![Circuit Diagram](https://github.com/Mihnea323/DE2_project/blob/main/images/diagram.png)

## Hardware Description
  &nbsp;&nbsp;&nbsp;Our hardware setup includes:
  - **Microcontroller** (ESP-32): acts as the central processing unit, interfacing with the GPS module, temperature and humidity sensor, and the OLED display. <br>
    FireBeetle Board- ESP32 integrates a Dual-Core ESP-WROOM-32 module, which supports MCU and Wi-Fi & Bluetooth dual-mode communication. <br>
    The ESP32 microcontroller board has a number of GPIO (General Purpose Input/Output) pins that can be used for various purposes, such as digital input and output, analog input, communication interfaces (e.g., UART, SPI, I2C), PWM (Pulse Width Modulation) output, and more. <br> <br>
    ![esp32](https://github.com/Mihnea323/DE2_project/blob/main/images/DFR0478_pinout3.png)
  - **GPS module** (NEO-6M-0-001): receives signals from GPS satellites to compute geographical location, it provides the longitude, latitude and altitude. <br>
    The **NEO-6M-0-001** is a GPS module commonly used in embedded systems for accurate positioning and navigation. It features the NEO-6M chipset, offering high sensitivity and quick acquisition times. It supports GPS and is capable of providing real-time location data with a high level of precision. The module communicates via UART and can be easily integrated with microcontrollers like ESP32. It operates with a voltage range of 3.3V to 5V and is widely used in applications such as robotics, drones, and vehicle tracking systems. <br> <br>
    ![gps](https://github.com/Mihnea323/DE2_project/blob/main/images/gps.jpg)
  - **I2C temperature/humidity sensor** (DHT12): measures ambient temperature and humidity and transmits the data digitally via the I2C bus. <br>
    The **DHT12** is a digital temperature and humidity sensor that communicates via the I2C protocol. It provides accurate measurements of temperature (with a range of -20°C to 60°C) and humidity (0% to 100% RH) with a high degree of reliability. The sensor operates at a voltage of 3.3V to 5V and outputs data in a 2-wire I2C format, making it easy to interface with microcontrollers like ESP32.<br> <br>
    ![sensor](https://github.com/Mihnea323/DE2_project/blob/main/images/sensor.jpg)
  - **OLED display** (SH1106 I2C): displays the GPS data and the environmental data. <br>
    The **SH1106** is an OLED display controller that supports the I2C communication protocol. It is typically used with small, low-power OLED displays, offering a resolution of 128x128 or 128x64 pixels, depending on the specific model. The SH1106 provides high contrast and sharp images with deep blacks, as it does not require a backlight, making it energy-efficient. It operates at a voltage of 3.3V to 5V and is commonly used in projects where space and power efficiency are important, such as portable devices, wearables, and microcontroller-based systems like ESP32. <br> <br>
    ![oled](https://github.com/Mihnea323/DE2_project/blob/main/images/oled.jpeg)

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

## Instructions and Photos

## References and Tools

