import time
import sys

import board
import busio
import digitalio

import adafruit_max31865


# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3, ref_resistor=430.0, rtd_nominal=100)

msg = round(sensor.temperature, 2)
print(msg)
