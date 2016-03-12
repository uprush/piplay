#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import random
import threading

def my_callback(channel):
    if channel == 22:
        t = threading.Thread(target=randomizeDice)
        t.start()

def randomizeDice():
    delay = 0.1
    for i in range(0, 3):
        sendLEDdata(LEDdata1, SER, RCLK, SRCLK)
        sleep(delay)
        sendLEDdata(LEDdata2, SER, RCLK, SRCLK)
        sleep(delay)
        sendLEDdata(LEDdata3, SER, RCLK, SRCLK)
        sleep(delay)
        sendLEDdata(LEDdata4, SER, RCLK, SRCLK)
        sleep(delay)
        sendLEDdata(LEDdata5, SER, RCLK, SRCLK)
        sleep(delay)
        sendLEDdata(LEDdata6, SER, RCLK, SRCLK)
        sleep(delay)

    dice = random.randint(0, 7)
    if dice == 0:
        sendLEDdata(LEDdata0, SER, RCLK, SRCLK)
    if dice == 1:
        sendLEDdata(LEDdata1, SER, RCLK, SRCLK)
    elif dice == 2:
        sendLEDdata(LEDdata2, SER, RCLK, SRCLK)
    if dice == 3:
        sendLEDdata(LEDdata3, SER, RCLK, SRCLK)
    elif dice == 4:
        sendLEDdata(LEDdata4, SER, RCLK, SRCLK)
    if dice == 5:
        sendLEDdata(LEDdata5, SER, RCLK, SRCLK)
    elif dice == 6:
        sendLEDdata(LEDdata6, SER, RCLK, SRCLK)
    elif dice == 7:
        sendLEDdata(LEDdata7, SER, RCLK, SRCLK)


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

SWITCH = 22
SER = 25
RCLK = 24
SRCLK = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(SWITCH, GPIO.RISING, callback=my_callback, bouncetime=200)

LEDdata0 = [0, 0, 0, 0, 0, 0, 0]
LEDdata1 = [0, 0, 0, 1, 0, 0, 0]
LEDdata2 = [0, 1, 0, 0, 0, 1, 0]
LEDdata3 = [0, 1, 0, 1, 0, 1, 0]
LEDdata4 = [1, 1, 0, 0, 0, 1, 1]
LEDdata5 = [1, 0, 1, 1, 0, 1, 1]
LEDdata6 = [1, 0, 1, 1, 1, 1, 1]
LEDdata7 = [1, 1, 1, 1, 1, 1, 1]

sendLEDdata(LEDdata0, SER, RCLK, SRCLK)

try:
    while True:
        sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

