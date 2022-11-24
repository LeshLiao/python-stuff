import argparse
import random
import time
import threading
import json
import socket

from datetime import datetime
from pythonosc import udp_client

class BroadcastOsc:
    def __init__(self):
        self.t1 = threading.Thread(target=self.start)
        self.is_running = True
        self.brightness = 0

        input_file = open ('config/StationSetup.json')
        json_Data = json.load(input_file)
        self.stations_array = json_Data['MyStations']

        self.hashTable = {}
        self.clientList = []
        self.lastStrList = []

        self.initHaspMap()
        self.ReadJsonFile()
        self.initJson()

    def stop(self):
        print("BroadcastOsc stop()")
        self.is_running = False

    def run(self):
        self.t1.start()

    def start(self):
        print("BroadcastOsc start()")
        while self.is_running:
            #print("thread is_running = True")
            stationIndex = 0
            for station in self.stations_array:
                rules_array = station['Rules']
                tempstr = ""
                for rule in rules_array:
                    tempstr +=  self.hashTable[str(rule['PadNo']) + "," + str(rule['Input'])]

                if tempstr != self.lastStrList[stationIndex]:
                    ########### TODO
                    self.clientList[stationIndex].send_message("/MatrixVelocity", tempstr)
                    self.lastStrList[stationIndex] = tempstr
                    print(station['IP']+":"+str(station['Port'])+ " color:" + tempstr)
                
                stationIndex = stationIndex + 1

            #print(self.hashTable)
            #print(datetime.now())
            time.sleep(0.03)

    def setBrightness(self, pad: str, particle: str, value: int):
        self.brightness = value
        color = str(value) + "," + str(value) + "," + str(value) + ","
        self.hashTable[pad+","+particle] = color

    def setLightXY(self, pad: str, particle: str, valueX: float, valueY: float):
        #color = str(value) + "," + str(value) + "," + str(value) + ","
        self.hashTable[pad+","+particle] = self.calculateLightColor(valueX,valueY)
        #print("valueX="+str(valueX)+",valueY="+str(valueY))

    def calculateLightColor(self, valueTemp: float, valueBrightness: float):
        r = 255
        g = 255 - (130 * valueTemp)
        b = 255 - (255 * valueTemp)
        r = int(r * valueBrightness)
        g = int(g * valueBrightness)
        b = int(b * valueBrightness)
        return str(r) + "," + str(g) + "," + str(b) + ","

    def initHaspMap(self):
        for index in range(65,71):
            self.hashTable[str(0)+ "," + str(index)] = "0,0,0,"

    def initJson(self):
        for index in range(150):
            self.hashTable[str(0)+ "," + str(index)] = "0,0,0,"

        for station in self.stations_array:
            self.clientList.append(udp_client.SimpleUDPClient(station['IP'], station['Port']) )
            self.lastStrList.append("")
            print(station['IP']+":"+str(station['Port']))

    def ReadJsonFile(self):
        input_file = open ('config/StationSetup.json')
        json_Data = json.load(input_file)
        
        print("[ StationSetup.json ]")
        print("ProjectName:" +json_Data['ProjectName'])
        print("Timestamp  :" +json_Data['Timestamp'])
        
        json_array = json_Data['MyStations']
        CurrentRuleList = []
        MatchDeviceIP = False
        
        for item in json_array:
            print("IP:" + item['IP'])
            print("Port:" + str(item['Port']))
            '''
            if(GetLocalIp() == item['IP']):
                CurrentRuleList = item['Rules']
                LeshLib.MyOscPort = item['Port']
                LeshLib.RuleListSize = len(CurrentRuleList)
                LeshLib.DeviceConfigList = item['Devices']
                print("We found RuleList():"+GetLocalIp()+",Rule list size:"+str(LeshLib.RuleListSize))
                MatchDeviceIP = True
                break
            '''

        
