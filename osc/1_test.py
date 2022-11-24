from pythonosc.dispatcher import Dispatcher
from typing import List, Any

import argparse
import random
import time
import threading

import json
import socket
from datetime import datetime


def testWhileLoop():
    print("testWhileLoop()")
    count = 0
    while True:
        time.sleep(0.3)
        #count = count + 1
        #if count%10 == 0:
        #    print(datetime.now())
        print(datetime.now())

input_file = open ('config/StationSetup.json')
json_Data = json.load(input_file)

print("[ StationSetup.json ]")
print("ProjectName:" +json_Data['ProjectName'])
print("Timestamp  :" +json_Data['Timestamp'])
stations_array = json_Data['MyStations']


for station in stations_array:
    print("IP:" + station['IP'])
    print("Port:" + str(station['Port']))

    rules_array = station['Rules']

    #for rule in rules_array:
    #    print("IP:" + str(rule['Input']))


hashTable = {"0,65": "1,1,1,", "0,66": "2,2,2,", "0,67": "3,3,3"}
print(hashTable)
pad = 0
particle = 66
key = str(pad)+ "," + str(particle)
print(hashTable[key])

newparticle = 100
#key = str(pad)+ "," + str(newparticle)
#hashTable[key] = "9,9,9,"

for index in range(10):
    hashTable[str(pad)+ "," + str(index)] = "0,0,0,"

print(hashTable)


testWhileLoop()
