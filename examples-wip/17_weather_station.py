# Weather station

import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import adafruit_character_lcd.character_lcd_i2c as LCD

# set GPIO board mode
GPIO.setmode(GPIO.BCM)

sensor_type = 11
sensor_pin = board.D4  # temperature&humudity sensor pin
led_pin = 6

dht_sensor = adafruit_dht.DHTBase(True, sensor_pin, use_pulseio=True, trig_wait=100000)

GPIO.setup(led_pin, GPIO.OUT)
# define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2
# initialize the LCD using the pins
lcd = LCD.Character_LCD_I2C(board.I2C(), lcd_columns, lcd_rows, address=0x20)
# turn backlight on
lcd.backlight = True

try:
    while True:
        humidity, temperature = dht_sensor.temperature, dht_sensor.humidity
        if humidity is not None and temperature is not None:
            lcd.message = "Temp={0:0.1f}\nHumidity={1:0.1f}%".format(
                temperature, humidity
            )

            if temperature < 10 or temperature > 35:
                GPIO.output(led_pin, GPIO.HIGH)
            else:
                GPIO.output(led_pin, GPIO.LOW)
            time.sleep(1)
        lcd.clear()
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
    GPIO.cleanup()
