import evdev
import RPi.GPIO as GPIO

# define relay pin
servo_pin = 13

a = 45
b = 18.0
fpwm = 50


def set_direction(direction):
    duty = (direction + a) / b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)


def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == "gpio_ir_recv":
            print("Using device", device.path, "n")
            return device
    print("No device found!")


dev = get_ir_device()

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, fpwm)
pwm.start(2.5)

try:
    for output in dev.read_loop():
        if output.value == 21:  # VOL_UP
            set_direction(180)
        elif output.value == 7:  # VOL_DOWN
            set_direction(0)
        elif output.value == 64:  # NEXT
            GPIO.output(5, GPIO.HIGH)
        elif output.value == 68:  # PREV
            GPIO.output(5, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
