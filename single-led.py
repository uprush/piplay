#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

LED = 25
SLEEP = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

count = 0

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        sleep(SLEEP)
        GPIO.output(LED, GPIO.LOW)
        sleep(SLEEP)
        count += 1

        if count > 19 :
            break

except KeyboardInterrupt:
    pass

GPIO.cleanup()

