import RPi.GPIO as GPIO
from keyboard import is_pressed

led_pin = 5
button_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

while not is_pressed("enter"):
    if GPIO.input(button_pin):
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
