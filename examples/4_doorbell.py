import time

import RPi.GPIO as GPIO
from keyboard import is_pressed

touch_pin = 5
buzzer_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)

while not is_pressed("enter"):
    if GPIO.input(touch_pin):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(3)
        # TODO: Check if this works as desired
        # Might beep from initialisation until touch detection.
        GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()
