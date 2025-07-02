import RPi.GPIO as GPIO
from keyboard import is_pressed

pir_pin = 5
led_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

while not is_pressed("enter"):
    if GPIO.input(pir_pin):
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
