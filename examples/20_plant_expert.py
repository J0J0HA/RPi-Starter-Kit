import time

import adafruit_character_lcd.character_lcd_i2c as LCD
import adafruit_dht
import board
import RPi.GPIO as GPIO
import spidev

# set GPIO board mode
GPIO.setmode(GPIO.BCM)
sensor_pin = board.D5  # temperature & humudity sensor pin

# define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2
# initialize the LCD using the pins
lcd = LCD.Character_LCD_I2C(board.I2C(), lcd_columns, lcd_rows, address=0x20)
# turn backlight on
lcd.backlight = True

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

dht_device = adafruit_dht.DHT11(sensor_pin)


def readadc(adcnum):
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout


try:
    while True:
        moisture_value = readadc(0)
        lcd.message = "Mois={}".format(moisture_value)
        time.sleep(2)
        lcd.clear()
        light_value = readadc(1)
        lcd.message = "light={}".format(light_value)
        time.sleep(2)
        lcd.clear()
        try:
            humidity, temperature = dht_device.humidity, dht_device.temperature
        except RuntimeError as e:
            # Reading from the sensor failed, skip this iteration
            print("Failed to read from DHT sensor: ", e)
            humidity = None
            temperature = None
        if humidity is not None and temperature is not None:
            lcd.message(
                "Temp={0:0.1f}\nHumidity={1:0.1f}%".format(temperature, humidity)
            )
            time.sleep(2)
        lcd.clear()

except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
    GPIO.cleanup()
