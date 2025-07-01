import time
import RPi.GPIO as GPIO
import board
import adafruit_character_lcd.character_lcd_i2c as LCD


GPIO.setmode(GPIO.BCM)

def dis():
    trig = 15
    echo = 14
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, False)
    time.sleep(0.5)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance


# define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2
# initialize the I2C address for LCD
lcd = LCD.Character_LCD_I2C(board.I2C(), lcd_columns, lcd_rows, address=0x20) #LCD.Adafruit_CharLCDBackpack(address=0x20)

# turn backlight on
lcd.backlight = True

try:
    while True:
        lcd.message = "{0:0.2f}cm".format(dis())
        time.sleep(1)
        lcd.clear()

except KeyboardInterrupt:
    lcd.clear()
    lcd.backlight = False
    GPIO.cleanup()
