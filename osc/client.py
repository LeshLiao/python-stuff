import argparse
import random
import time

from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="172.20.10.4",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  for x in range(1):
    # client.send_message("/1/toggle1", 1)
    # client.send_message("/MatrixVelocity", "10,10,10,10,0,0,0,10,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0")
    
    #client.send_message("/0/65/brightness", "100")
    #client.send_message("/0/65/colortemperature", "200")

    client.send_message("/0/65/brightness", "123")
    time.sleep(1)
