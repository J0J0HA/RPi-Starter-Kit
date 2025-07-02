import time

import RPi.GPIO as GPIO
from keyboard import is_pressed

hall_pin = 4
green_pin = 5
red_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(hall_pin, GPIO.IN)

while not is_pressed("enter"):
    if not GPIO.input(hall_pin):
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.LOW)
        time.sleep(0.5)
    else:
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.LOW)

GPIO.cleanup()
