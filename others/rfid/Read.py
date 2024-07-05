#!/usr/bin/env python

import RPi.GPIO as GPIO
import syslog
import json
import threading
import time

from mfrc522 import SimpleMFRC522
from time import sleep
from req import post_data
from req import get_all_data
from buzzier import one_sound
from buzzier import four_sound
from buzzier import long_sound


def polling_backend():
    sleep_time = 840 # 14 minutes
    index = 0
    while True:
        index = index + 1
        showMessage("get_all_data() loop_"+str(index))
        get_all_data()
        showMessage("sleep for "+str(sleep_time)+" seconds")
        time.sleep(sleep_time)

def showMessage(msg):
    print(msg)
    syslog.syslog(msg)

reader = SimpleMFRC522()

try:
    t1 = threading.Thread(target = polling_backend)
    t1.start()

    while(True):
        id, text = reader.read()
        one_sound(37, 0.1)
        showMessage(str(id))
        showMessage(text)
        if text == "" or text == None:
            print("Warning:text is empty!")
            text = "<empty>"
        json_data, res_code = post_data(id, text)
        data = json.dumps(json_data)
        if res_code != "200":
            four_sound(37, 0.1)
        showMessage(data)
        showMessage(res_code)
        sleep(2)
except requests.exceptions.Timeout:
    four_sound(37, 0.1)
    showMessage("except:request Timeout!")
except Exception as e:
    long_sound(37, 3)
    showMessage("except:"+str(e))
finally:
    showMessage("finally:GPIO.cleanup")
    GPIO.cleanup()
