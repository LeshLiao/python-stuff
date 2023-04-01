"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  for x in range(1):
    #client.send_message("/filter", random.random())
    #client.send_message("/volume", 100)
    
    #client.send_message("/volumeup", 1.0)
    
    #client.send_message("/1/toggle1", 1)
    #client.send_message("/volumetest", 1.0)

    client.send_message("/MatrixVelocity", "10,10,10,10,0,0,0,10,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0")
    time.sleep(1)
