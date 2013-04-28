#!/usr/bin/python

import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)
    gpio.setup(11, gpio.OUT)

def teardown():
    gpio.cleanup()

def red(state):
    gpio.output(8, state)

def yellow(state):
    gpio.output(7, state)

def green(state):
    gpio.output(11, state)

def main():
    setup()

    for i in range(1, 10):
        red(i % 2 == 0)
        yellow(i % 2 == 0)
        green(i % 2 == 0)
        time.sleep(0.5)
    
    teardown()
    return 2

if __name__ == "__main__":
    main()
