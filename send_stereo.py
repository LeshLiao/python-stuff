#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os
import time
import threading

def sendPowerKey():
    print('piir play --gpio 17 --file stereo.json power')
    os.system ("piir play --gpio 17 --file stereo.json power")


#HOST = '0.0.0.0'
#PORT = 7038
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((HOST, PORT))

#print('server start at: %s:%s' % (HOST, PORT))
#print('waiting for the commands...')

sendPowerKey()


