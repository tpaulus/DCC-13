#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com
#For DCC 2013.1

import time
import spidev
import RPi.GPIO as GPIO


spi = spidev.SpiDev()
light_adc = 7
statusLED = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(statusLED, GPIO.OUT)

print "Press CTRL+Z to exit"


def analogRead(port):
    """Read the given ADC port and preform the necessary shifting of bits"""
    spi.open(0, 0)
    if (port > 7) or (port < 0):
        print 'analogRead -- Port Error, Must use a port between 0 and 7'
        return -1
    r = spi.xfer2([1, (8 + port) << 4, 0])
    value = ((r[1] & 3) << 8) + r[2]
    spi.close()
    return value


while True:
    GPIO.output(statusLED, True)   # Status Led On
    print analogRead(light_adc)    # Print read value
    time.sleep(.125)               # Wait a little
    GPIO.output(statusLED, False)  # Status Led Off
    time.sleep(.175)               # Wait a bit longer