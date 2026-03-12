
from collections import defaultdict

count = defaultdict(int)

# print(count["device1"])

# filter、map、reduce


'''
[
"device1:ERROR",
"device2:OK",
"device1:ERROR",
"device3:OK",
"device2:ERROR"
]
'''

all_devices = [
  ("device1","ERROR"),
  ("device2","OK"),
  ("device1","ERROR"),
  ("device3","OK"),
  ("device2","ERROR")
]

def show_all_device(devices):

  for key, value in devices:
    if value == "ERROR":
      count[key] += 1
    return dict(count)

expected = {
  "device1": 2,
  "device2": 1
}

result = show_all_device(all_devices)

print(expected == result)