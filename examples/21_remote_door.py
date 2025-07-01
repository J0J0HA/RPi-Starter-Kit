#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import lirc

# define relay pin
servo_pin = 12

a = 45
b = 18.0
fpwm = 50


def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, fpwm)
    pwm.start(2.5)


def setDirection(direction):
    duty = (direction + a) / b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)


# setup the IR pins
Lirc = lirc.Client("keys")

Lirc.
try:
    setup()
    print("starting")
    while True:
        output = lirc.nextcode()[0]
        print(output)
        if output == "VOL_UP":
            # rotate to 180
            setDirection(180)
        elif output == "VOL_DWN":
            # rotate to 0
            setDirection(0)
except KeyboardInterrupt:
    GPIO.cleanup()
