import RPi.GPIO as GPIO
import spidev
from keyboard import is_pressed

GPIO.setmode(GPIO.BCM)
led_pin = 5
GPIO.setup(led_pin, GPIO.OUT)


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


def readadc(adcnum):
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout


while not is_pressed("enter"):
    value = readadc(0)
    if value < 500:
        GPIO.output(led_pin, GPIO.HIGH)
    else:
        GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()
