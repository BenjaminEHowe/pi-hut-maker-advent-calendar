import machine
import time


RED_TIME_SECONDS = 5
AMBER_TIME_SECONDS = 1
GREEN_TIME_SECONDS = 8

RED = machine.Pin(18, machine.Pin.OUT)
AMBER = machine.Pin(19, machine.Pin.OUT)
GREEN = machine.Pin(20, machine.Pin.OUT)


def switch_leds_off():
    RED.value(0)
    AMBER.value(0)
    GREEN.value(0)


def switch_leds_on(leds, switch_off_delay=0):
    for led in leds:
        led.value(1)
    if switch_off_delay:
        time.sleep(switch_off_delay)
        for led in leds:
            led.value(0)


switch_leds_off()
switch_leds_on([GREEN], 1)
while True:
    switch_leds_on([AMBER], AMBER_TIME_SECONDS)
    switch_leds_on([RED], RED_TIME_SECONDS)
    switch_leds_on([RED, AMBER], AMBER_TIME_SECONDS)
    switch_leds_on([GREEN], GREEN_TIME_SECONDS)
