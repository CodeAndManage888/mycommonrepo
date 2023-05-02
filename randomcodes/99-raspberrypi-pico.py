import usb_hid
from adafruit_hid.mouse import Mouse
import time

mouse = Mouse(usb_hid.devices)

while True:
    mouse.move(x=150)
    time.sleep(20)
    mouse.move(x=-150)
    time.sleep(20)
    mouse.move(y=150)
    time.sleep(20)
    mouse.move(y=-150)
    time.sleep(20)