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
