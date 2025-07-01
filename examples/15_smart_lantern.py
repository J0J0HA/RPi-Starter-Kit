# Smart lantern

import RPi.GPIO as GPIO
import time
from pi5neo import Pi5Neo

# Initialize the Pi5Neo class with 10 LEDs and an SPI speed of 800kHz
neo = Pi5Neo("/dev/spidev0.0", 4, 800)

# Fill the strip with a red color
neo.fill_strip(255, 0, 0)
neo.update_strip()  # Commit changes to the LEDs

time.sleep(3)
# Set the 5th LED to blue
neo.set_led_color(3, 0, 0, 255)
neo.update_strip()
time.sleep(3)


# GPIO.setmode(GPIO.BCM)
# pir_pin = 6
# GPIO.setup(pir_pin, GPIO.IN)

# # LED strip configuration:
# LED_COUNT = 4  # Number of LED pixels.
# LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM!).
# LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA = 10  # DMA channel to use for generating signal (try 5)
# LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
# LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)


# # Create NeoPixel object with appropriate configuration.
# strip = PixelStrip(
#     LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS
# )
# # Intialize the library (must be called once before other functions).
# strip.begin()
# colors = [Color(220, 20, 60), Color(178, 34, 34), Color(255, 0, 0), Color(139, 0, 0)]


# def loopColor(strip, colors):
#     for color in colors:
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, color)
#             strip.show()
#             time.sleep(0.2)


# def wipe(strip, color, wait_ms=50):
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, color)
#     strip.show()


# try:

#     while True:
#         if GPIO.input(pir_pin) == 1:
#             loopColor(strip, colors)
#         wipe(strip, Color(0, 0, 0), 10)
#         strip.show()
#         time.sleep(1)
# except KeyboardInterrupt:
#     wipe(strip, Color(0, 0, 0), 10)
#     strip.show()
#     GPIO.cleanup()
