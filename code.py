import time
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
import digitalio
import random

mouse = Mouse(usb_hid.devices)
time.sleep(2)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

led.value = False
mouse.move(y=800)

click = 1
while click < 2:
    led.value=True
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    i = 1000
    while i <= 9999:
        key = i
        pin =str(key)
        keyboard_layout.write(pin)
        time.sleep(1.5)
        i += 1
        click = click+1

led.value=False
