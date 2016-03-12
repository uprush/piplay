#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

def sendLEDdata(data, ser, rclk, srclk):
    n = len(data)

    GPIO.output(rclk, GPIO.LOW)
    GPIO.output(srclk, GPIO.LOW)

    for i in range(n):
        if data[i] == 1:
            GPIO.output(ser, GPIO.HIGH)
        else:
            GPIO.output(ser, GPIO.LOW)

        GPIO.output(srclk, GPIO.HIGH)
        GPIO.output(srclk, GPIO.LOW)

    GPIO.output(rclk, GPIO.HIGH)
    GPIO.output(rclk, GPIO.LOW)

SER = 25
RCLK = 24
SRCLK = 23

SLEEP = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)

LEDdata1 = [0, 0, 0, 1, 0, 0, 0]
LEDdata2 = [0, 1, 0, 0, 0, 1, 0]
LEDdata3 = [0, 1, 0, 1, 0, 1, 0]
LEDdata4 = [1, 1, 0, 0, 0, 1, 1]
LEDdata5 = [1, 1, 0, 1, 0, 1, 1]
LEDdata6 = [1, 1, 1, 0, 1, 1, 1]

try:
    while True:
        sendLEDdata(LEDdata1, SER, RCLK, SRCLK)
        sleep(SLEEP)
        sendLEDdata(LEDdata2, SER, RCLK, SRCLK)
        sleep(SLEEP)
        sendLEDdata(LEDdata3, SER, RCLK, SRCLK)
        sleep(SLEEP)
        sendLEDdata(LEDdata4, SER, RCLK, SRCLK)
        sleep(SLEEP)
        sendLEDdata(LEDdata5, SER, RCLK, SRCLK)
        sleep(SLEEP)
        sendLEDdata(LEDdata6, SER, RCLK, SRCLK)
        sleep(SLEEP)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

