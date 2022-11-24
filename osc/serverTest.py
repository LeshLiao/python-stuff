import argparse
import math
import os
import sys

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from typing import List, Any

def all_filter(address: str, *args: List[Any]) -> None:
    #value = int(args[0])
    #num = address.split('/')
    print(f"Setting filter {address} args: {args}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/*", all_filter)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  
  try:
    server.serve_forever()
  except:
    print("exception:", sys.exc_info()[0], "occurred.")
    #bb.stop()


  