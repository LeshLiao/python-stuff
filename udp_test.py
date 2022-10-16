#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os
import time
import threading

def sendPowerKey1():
    print("(1)ready to power in 15s...")
    time.sleep(15)
    print('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file light.json power")

def sendPowerKey2():
    print("(2)ready to power in 15s...")
    time.sleep(15)
    print('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file light.json power")

def sendPowerKey3():
    print("(3)ready to power in 15s...")
    time.sleep(15)
    print('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file light.json power")

HOST = '0.0.0.0'
PORT = 7038
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('waiting for the commands...')

while True:
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    receiveStr = indata.decode()

    if receiveStr == "autotest_finish":
        print("AutoTesting Finish")
    elif receiveStr == "ready_to_power_on_1":
        t1 = threading.Thread(target = sendPowerKey1)
        t1.start()
    elif receiveStr == "ready_to_power_on_2":
        t2 = threading.Thread(target = sendPowerKey2)
        t2.start()
    elif receiveStr == "ready_to_power_on_3":
        t3 = threading.Thread(target = sendPowerKey3)
        t3.start()
    else :
        print('else cmd:'+ receiveStr)


