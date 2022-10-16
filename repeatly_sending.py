#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os
import time
import threading

def sendPowerKey():
    #cmd = 'piir play --gpio 17 --file stereo.json volumn_down'
    cmd = 'piir play --gpio 17 --file ac.json power'
    print(cmd)
    os.system (cmd)

x = 0
while x < 10:
    print("run {} times:".format(str(x+1)))
    x= x + 1
    sendPowerKey()
    time.sleep(2)

