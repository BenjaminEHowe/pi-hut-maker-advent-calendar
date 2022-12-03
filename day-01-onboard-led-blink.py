import machine
import time


onboardLED = machine.Pin(25, machine.Pin.OUT)


def switch_led_off():
    onboardLED.value(0)
    print("LED has been switched off")


def switch_led_on():
    onboardLED.value(1)
    print("LED has been switched on")


while True:
    switch_led_on()
    time.sleep(1)
    switch_led_off()
    time.sleep(1)
