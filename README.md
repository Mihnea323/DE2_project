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
  - **Microcontroller** (ESP-32): acts as the central processing unit, interfacing with the GPS module, temperature and humidity sensor, and the OLED display.
  - **GPS module** (NEO-6M-0-001): receives signals from GPS satellites to compute geographical location, it provides the longitude, latitude and altitude.
  - **I2C temperature/humidity sensor** (DHT12): measures ambient temperature and humidity and transmits the data digitally via the I2C bus.
  - **OLED display** (SH1106 I2C): displays the GPS data and the environmental data.

## Software Description
The software consists of several classes.

#### 1. I2C class
   &nbsp;&nbsp;&nbsp;This class simplifies communication with I2C-enabled devices like the OLED display and temperature/humidity sensor. It ensures smooth and efficient integration of peripherals with minimal wiring and code complexity. <br>
   **Example of usage**: i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400_000)
#### 2. SH1106 class
   &nbsp;&nbsp;&nbsp;This class is used for communication with the OLED, which is used to display the longitude, latitude, altidude, as well as temperature and humidty. <br>
    **Example of usage**: oled = SH1106_I2C(i2c) <br>
    **Source file**: 
#### 3. DHT12 class
   &nbsp;&nbsp;&nbsp;This class is designed to interface with the temperature/humidity sensor. It continuously reads environmental conditions and display them on the OLED screen alongside GPS data. <br>
    **Example of usage**: sensor = dht12.DHT12(i2c) <br>
    **Source file**: 
#### 4. MicropyGPS class
   &nbsp;&nbsp;&nbsp;The code processes GPS NMEA sentences received from a GPS module, parses them character by character, validates them, and extracts useful information like location, time, speed, and satellite data. It converts latitude and longitude between decimal degrees, degrees-minutes-seconds, and other formats and determines the cardinal direction based on the course. <br>
   &nbsp;&nbsp;&nbsp;How the code works:
   - **Sentence parsing**: each character of a GPS sentence is passed to ***update***, then the ***update*** method segments the sentence and validates it.
   - **Validation**: checks if the checksum matches to ensure no data corruption and if valid, parses the sentence type and extracts relevant data.
   - **Data storage**: updates attributes like ***latitude***, ***longitude***, ***altitude***, etc. <br>
   
 **Example of usage**: my_gps = MicropyGPS() <br>
 **Source file**: 

## Instructions and Photos

## References and Tools

