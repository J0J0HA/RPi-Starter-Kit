import time

import RPi.GPIO as GPIO
import spidev
from keyboard import is_pressed

GPIO.setmode(GPIO.BCM)
led_pin = 12
GPIO.setup(led_pin, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

pwm = GPIO.PWM(led_pin, 80)
pwm.start(0)


def readadc(adcnum):
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout


def brightness_func(x):
    return x / 4 / 2.56


while not is_pressed("enter"):
    value = readadc(0)
    brightness = brightness_func(value)
    pwm.ChangeDutyCycle(brightness)
    time.sleep(0.1)

GPIO.cleanup()
