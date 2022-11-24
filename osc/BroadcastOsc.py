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
        self.ip = "192.168.1.179"
        self.port = 2346
        self.client = udp_client.SimpleUDPClient(self.ip, self.port)
        self.t1 = threading.Thread(target=self.start)
        self.is_running = True
        self.brightness = 0

        input_file = open ('config/StationSetup.json')
        json_Data = json.load(input_file)
        self.stations_array = json_Data['MyStations']

        self.hashTable = {}
        self.clientList = []

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
            #for x in range(24):
            #    tempstr += str(self.brightness) + ","
            stationIndex = 0
            for station in self.stations_array:
                rules_array = station['Rules']
                tempstr = ""
                for rule in rules_array:
                    #key = str(rule['PadNo']) + "," + str(rule['Input'])
                    #print("key="+key)
                    tempstr +=  self.hashTable[str(rule['PadNo']) + "," + str(rule['Input'])]

                #self.client.send_message("/MatrixVelocity", tempstr)
                myClient = self.clientList[stationIndex]
                myClient.send_message("/MatrixVelocity", tempstr)
                #print(station['IP']+":"+str(station['Port'])+ " color:" + tempstr)
                stationIndex = stationIndex + 1

            #print(self.hashTable)
            time.sleep(0.02)
            print(datetime.now())

    def setBrightness(self, pad: str, particle: str, value: int):
        self.brightness = value
        color = str(value) + "," + str(value) + "," + str(value) + ","
        self.hashTable[pad+","+particle] = color

    def initHaspMap(self):
        for index in range(65,71):
            self.hashTable[str(0)+ "," + str(index)] = "0,0,0,"

    def initJson(self):
        for index in range(150):
            self.hashTable[str(0)+ "," + str(index)] = "0,0,0,"

        index = 0
        for station in self.stations_array:
            #self.clientList[index] = udp_client.SimpleUDPClient(station['IP'], station['Port'])
            self.clientList.append(udp_client.SimpleUDPClient(station['IP'], station['Port']) )
            index = index + 1
            print(station['IP']+":"+str(station['Port']))

    def ReadJsonFile(self):
        input_file = open ('config/StationSetup.json')
        json_Data = json.load(input_file)
        
        print("[ StationSetup.json ]")
        print("ProjectName:" +json_Data['ProjectName'])
        print("Timestamp  :" +json_Data['Timestamp'])
        
        json_array = json_Data['MyStations']
        CurrentRuleList = []
        #LeshLib.JsonTimestamp = json_Data['Timestamp']
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

        