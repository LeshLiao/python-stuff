import argparse
import math
import os
import sys

from BroadcastOsc import BroadcastOsc
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from typing import List, Any

def brightness_filter(address: str, *args: List[Any]) -> None:
    value = int(args[0])
    num = address.split('/')
    print(f"Setting filter {address} values: {str(value)} pad: {num[1]} particle: {num[2]} ")
    bb.setBrightness(num[1],num[2],value)
    
def colortemp_filter(address: str, *args: List[Any]) -> None:
    value = int(args[0])
    num = address.split('/')
    print(f"Setting filter {address} values: {str(value)} pad: {num[1]} particle: {num[2]} ")

def lightxy_filter(address: str, *args: List[Any]) -> None:
    #value = int(args[0])
    num = address.split('/')
    #print(f"Setting filter {address} values: {str(value)} pad: {num[1]} particle: {num[2]} ")
    bb.setLightXY(num[1],num[2],args[0],args[1])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  parser.add_argument("--config",
      default="config/StationSetup.json", help="The config to load")

  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/*/*/brightness", brightness_filter)
  dispatcher.map("/*/*/colortemp", colortemp_filter)
  dispatcher.map("/*/*/lightxy", lightxy_filter)

  bb = BroadcastOsc(args.config)
  bb.run()
  
  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  
  try:
    server.serve_forever()
  except:
    print("exception:", sys.exc_info()[0], "occurred.")
    bb.stop()


  