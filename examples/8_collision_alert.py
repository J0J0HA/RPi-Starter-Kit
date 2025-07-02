import time

import RPi.GPIO as GPIO
from keyboard import is_pressed

GPIO.setmode(GPIO.BCM)
collision_pin = 4
buzzer_pin = 5
led_pin = 6

GPIO.setup(collision_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

while not is_pressed("enter"):
    if GPIO.input(collision_pin):
        GPIO.output(buzzer_pin, GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)
    else:
        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
