import argparse
import math
import os

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server


def fun_volumnup(unused_addr, args, volume):
  #print("[{0}] ~ {1}".format(args[0], volume))
  print("[{0}] ~ {1} : {2}".format(args[0], volume, unused_addr))
  #print("fun_volumnup()")
  if volume == 1.0:
    print("yes volumn up")

def fun_volumndown(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))
  print("fun_volumndown()")
  if volume == 1.0:
    print("yes volumn down")

def default_handler_function(address, *args):
  print(f"DEFAULT {address}: {args}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/volumeup", fun_volumnup, "VolumnUp")
  dispatcher.map("/volumedown", fun_volumndown, "VolumnDown")

  dispatcher.set_default_handler(default_handler_function)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
