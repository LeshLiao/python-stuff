"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math
import os


from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))


def fun_volumnup(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))
  print("fun_volumnup()")
  if volume == 1.0:
    print("yes volumn up")
    os.system("piir play --gpio 17 --file /home/pi/stereo.json volumn_up")

def fun_volumndown(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))
  print("fun_volumndown()")
  if volume == 1.0:
    print("yes volumn down")
    os.system("piir play --gpio 17 --file /home/pi/stereo.json volumn_down")

def fun_power(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))
  if volume == 1.0:
    print("yes power")
    os.system("piir play --gpio 17 --file /home/pi/stereo.json power")

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def default_handler_function(address, *args):
  print(f"DEFAULT {address}: {args}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="192.168.1.155", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/filter", print)
  dispatcher.map("/volume", print_volume_handler, "Volume")
  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
  dispatcher.map("/volumeup", fun_volumnup, "VolumnUp")
  dispatcher.map("/volumedown", fun_volumndown, "VolumnDown")
  dispatcher.map("/power", fun_power, "Power")

  dispatcher.set_default_handler(default_handler_function)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
