# Smart lantern

import RPi.GPIO as GPIO
import time
import board
import neopixel

GPIO.setmode(GPIO.BCM)
pir_pin = 6
GPIO.setup(pir_pin, GPIO.IN)

# LED strip configuration:
LED_COUNT = 4  # Number of LED pixels.
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)


# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(
    board.D12,
    LED_COUNT,
    pixel_order=neopixel.GRB,
    brightness=LED_BRIGHTNESS,
    auto_write=False,
)
# Intialize the library (must be called once before other functions).

colors = [(220, 20, 60), (178, 34, 34), (255, 0, 0), (139, 0, 0)]


def loopColor(strip, colors):
    for color in colors:
        for i in range(strip.numPixels()):
            strip[i] = color
            strip.show()
            time.sleep(0.2)


def wipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip[i] = color
    strip.show()


try:
    while True:
        strip.begin()
        if GPIO.input(pir_pin) == 1:
            loopColor(strip, colors)
        wipe(strip, (0, 0, 0), 10)
        strip.show()
        time.sleep(1)
except KeyboardInterrupt:
    wipe(strip, (0, 0, 0), 10)
    strip.show()
    GPIO.cleanup()
