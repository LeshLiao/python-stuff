import argparse
import math
import os

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from typing import List, Any

def brightness_filter(address: str, *args: List[Any]) -> None:
    value = args[0]
    num = address.split('/')
    print(f"Setting filter {address} values: {value} pad: {num[1]} particle: {num[2]} ")

def colortemp_filter(address: str, *args: List[Any]) -> None:
    value = args[0]
    num = address.split('/')
    print(f"Setting filter {address} values: {value} pad: {num[1]} particle: {num[2]} ")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/*/*/brightness", brightness_filter)
  dispatcher.map("/*/*/colortemp", colortemp_filter)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
