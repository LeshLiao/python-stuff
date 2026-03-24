from collections import defaultdict

events = [
  ("device1", "CONNECTED"),
  ("device2", "CONNECTED"),
  ("device1", "DISCONNECTED"),
  ("device3", "CONNECTED")
]

expected = ["device2", "device3"]

events_length = len(events)

#print(events_length)

devices_status = defaultdict(str)

for device, status in reversed(events):
  if (devices_status[device] == ""):
    devices_status[device] = status

result = []

for key in reversed(devices_status):
  if (devices_status[key] == "CONNECTED"):
    result.append(key)


print("Test result:")
print(expected == result)


#print(dict(devices_status))
