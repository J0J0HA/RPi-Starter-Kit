import RPi.GPIO as GPIO
from keyboard import is_pressed

GPIO.setmode(GPIO.BCM)
ir_pin = 4
green_pin = 5
red_pin = 6

GPIO.setup(ir_pin, GPIO.IN)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)

while not is_pressed("enter"):
    if GPIO.input(ir_pin):
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(red_pin, GPIO.LOW)
        print("on track")
    else:
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.HIGH)
        print("off track")

GPIO.cleanup()
