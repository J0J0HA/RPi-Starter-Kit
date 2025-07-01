import time

import adafruit_character_lcd.character_lcd_i2c as LCD
import board
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
hall_pin = 4
buzzer_pin = 5
led_pin = 6
GPIO.setup(hall_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)


start_timer = time.time()
taketime = 10


# define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2
# initialize the I2C
lcd = LCD.Character_LCD_I2C(
    board.I2C(), lcd_columns, lcd_rows, address=0x20
)
# turn backlight on
lcd.backlight = True


def hall_pulse(channel):
    global pulses
    pulses += 1


GPIO.add_event_detect(hall_pin, GPIO.FALLING, callback=hall_pulse, bouncetime=50)

pulses = 0

try:
    while True:
        if time.time() > (start_timer + taketime):
            lcd.clear()
            print("{} pulses".format(pulses))
            lcd.message = "rpm={}".format(pulses)
            if pulses > 20 and pulses < 30:
                GPIO.output(buzzer_pin, GPIO.LOW)
                GPIO.output(led_pin, GPIO.HIGH)
            elif pulses > 30:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(led_pin, GPIO.LOW)
            else:
                GPIO.output(buzzer_pin, GPIO.LOW)
                GPIO.output(led_pin, GPIO.LOW)

            start_timer = time.time() + taketime
            pulses = 0
            time.sleep(1)
except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
    GPIO.cleanup()
