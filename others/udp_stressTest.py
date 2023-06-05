#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import os
import time
import threading
import syslog
import serial, time
import logging

def showMessage(msg):
    print(msg)
    syslog.syslog(msg)
    logging.debug(msg)

def sendPowerKey1():
    showMessage("(1)ready to power in 15s...")
    time.sleep(15)
    showMessage('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file /home/pi/light.json power")

def sendPowerKey2():
    showMessage("(2)ready to power in 15s...")
    time.sleep(15)
    showMessage('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file /home/pi/light.json power")

def sendPowerKey3():
    showMessage("(3)ready to power in 15s...")
    time.sleep(15)
    showMessage('piir play --gpio 17 --file light.json power')
    os.system ("piir play --gpio 17 --file /home/pi/light.json power")

def shootingVideo():
    showMessage("shootingVideo...begin")
    cmd = "yes | ffmpeg -f video4linux2 -r 29 -s 640x480 -t 120 -i /dev/video0 /home/pi/Desktop/video0.avi"
    os.system (cmd)
    showMessage("shootingVideo...end")

def powerKey(delay):
    showMessage("powerKey," + delay)
    os.system ("piir play --gpio 17 --file /home/pi/light.json power")

KEY_UP = '~00140 10\r\n' #Up
KEY_DOWN = '~00140 14\r\n' #Down
KEY_LEFT = '~00140 11\r\n' #Left
KEY_RIGHT = '~00140 13\r\n' #Right
KEY_ENTER = '~00140 12\r\n' #Enter
KEY_POWER_ON = '~00140 1\r\n' #Power on

event = threading.Event()

def StressTesting_Case_3_1():
    showMessage("StressTesting_Case_3_1()")

    event.set()
    event.clear()

    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    sendRS232Command(KEY_RIGHT)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    showMessage("sleep 620s...")
    time.sleep(620)
    showMessage("sendRS232Command KEY_POWER_ON")
    sendRS232Command(KEY_POWER_ON)

def StressTesting_Case_3_2():
    showMessage("StressTesting_Case_3_2()")
    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    sendRS232Command(KEY_RIGHT)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    showMessage("sleep 20s")
    time.sleep(20)
    sendRelayOff()
    time.sleep(3)
    sendRelayOn()
    time.sleep(5)
    showMessage("Power on...")
    sendRS232Command(KEY_POWER_ON)

def StressTesting_Case_3_3():
    showMessage("StressTesting_Case_3_3()")
    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_DOWN)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    sendRS232Command(KEY_RIGHT)
    time.sleep(0.3)
    sendRS232Command(KEY_ENTER)
    time.sleep(1)

    showMessage("sleep 190s")
    time.sleep(190)
    sendRelayOff()
    time.sleep(3)
    sendRelayOn()
    time.sleep(5)
    showMessage("Power on...")
    sendRS232Command(KEY_POWER_ON)

def sendRS232Command(cmd):
    COM_PORT = "/dev/ttyUSB0"
    BAUD_RATES = 9600
    ser = serial.Serial(COM_PORT, BAUD_RATES)

    #COMMAND = '~00140 17\r\n' #volumn down
    COMMAND = cmd

    print(COMMAND.encode())
    print(COMMAND)
    ser.read(ser.inWaiting()) #drop data in buffer
    ser.write(COMMAND.encode())

    #HEXCOMMAND = b'\x2a\x50\x33\x31\x34\x30\x34\x39\x02\x01\x0d' #  string in hex (get mcu version)
    #HEXCOMMAND = b'\x2a\x50\x33\x31\x34\x30\x34\x39\x02\x01\x0d' #  string in hex
    #ser.write(HEXCOMMAND)

    time.sleep(0.5) #Wait for all data
    data= ser.read(ser.inWaiting())
    msg = "Respone:"+data.decode().lstrip()
    print(msg)

    ser.close()

def sendRelayOff():
    showMessage("sendRelayOff()")
    RELAY_COM_PORT = "/dev/ttyUSB1"
    RELAY_BAUD_RATES = 9600
    relay_ser = serial.Serial(RELAY_COM_PORT, RELAY_BAUD_RATES)

    packet = bytearray()
    packet.append (0xFE)
    packet.append (0x05)
    packet.append (0x00)
    packet.append (0x00)
    packet.append (0xFF)
    packet.append (0x00)
    packet.append (0x98)
    packet.append (0x35)
    relay_ser.write(packet)

    relay_ser.close()

def sendRelayOn():
    showMessage("sendRelayOn()")
    RELAY_COM_PORT = "/dev/ttyUSB1"
    RELAY_BAUD_RATES = 9600
    relay_ser = serial.Serial(RELAY_COM_PORT, RELAY_BAUD_RATES)

    packet = bytearray()
    packet.append (0xFE)
    packet.append (0x05)
    packet.append (0x00)
    packet.append (0x00)
    packet.append (0x00)
    packet.append (0x00)
    packet.append (0xD9)
    packet.append (0xC5)
    relay_ser.write(packet)

    relay_ser.close()

def PowerOnAfterFewSeconds():
    showMessage("PowerOnAfterFewSeconds, and delay 25s...")
    time.sleep(25)
    showMessage("sendRS232Command KEY_POWER_ON")
    sendRS232Command(KEY_POWER_ON)

def checkNextRound():
    showMessage("checkNextRound: wait event for 95s")
    is_set_by_event = event.wait(95)
    if is_set_by_event:
        showMessage("checkNextRound: Get event!")
    else:
        showMessage("checkNextRound:=================== Timeout!")
        #showMessage("checkNextRound:=================== Timeout! Do power on again!")
        #showMessage("KEY_POWER_ON")
        #sendRS232Command(KEY_POWER_ON)

HOST = '0.0.0.0'
PORT = 7038
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

logging.basicConfig(format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s',
                    filename=os.path.dirname(__file__)+'/my_logs.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    filemode='w')

showMessage('Current python dir:'+os.path.dirname(__file__))
showMessage('server start at: %s:%s' % (HOST, PORT))
showMessage('waiting for the commands...')


while True:
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    receiveStr = indata.decode()
    showMessage('receiveStr='+ receiveStr)

    paramList = receiveStr.split(",")

    if receiveStr == "autotest_finish":
        showMessage("AutoTesting Finish")
    elif receiveStr == "ready_to_power_on_1":
        t1 = threading.Thread(target = sendPowerKey1)
        t1.start()
    elif receiveStr == "ready_to_power_on_2":
        t2 = threading.Thread(target = sendPowerKey2)
        t2.start()
    elif receiveStr == "ready_to_power_on_3":
        t3 = threading.Thread(target = sendPowerKey3)
        t3.start()
    elif receiveStr == "StressTesting_Case_3_1":
        t31 = threading.Thread(target = StressTesting_Case_3_1)
        t31.start()
    elif receiveStr == "StressTesting_Case_3_2":
        t32 = threading.Thread(target = StressTesting_Case_3_2)
        t32.start()
    elif receiveStr == "StressTesting_Case_3_3":
        t33 = threading.Thread(target = StressTesting_Case_3_3)
        t33.start()
    elif receiveStr == "PowerOnAfterFewSeconds":
        t_poweron = threading.Thread(target = PowerOnAfterFewSeconds)
        t_poweron.start()
        t_checkNextRound = threading.Thread(target = checkNextRound)
        t_checkNextRound.start()
        t_shootingVideo = threading.Thread(target = shootingVideo)
        t_shootingVideo.start()
    else :
        if len(paramList) == 3:
            if paramList[0] == "udp" and paramList[1] == "power":
                powerKey(paramList[2])

        showMessage('else cmd:'+ receiveStr)

