import RPi.GPIO as GPIO
from time import sleep

LED = 25
SLEEP = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        sleep(SLEEP)
        GPIO.output(LED, GPIO.LOW)
        sleep(SLEEP)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

