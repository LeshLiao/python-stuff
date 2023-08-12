#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

from req import post_data
from buzzier import one_sound
from buzzier import four_sound

reader = SimpleMFRC522()

try:
    while(True):
        id, text = reader.read()
        print(id)
        print(text)
        one_sound(37, 0.1)
        post_data(id, text)
        sleep(2)
except Exception as e:
    print(e)
    four_sound(37, 0.1)
finally:
        GPIO.cleanup()
