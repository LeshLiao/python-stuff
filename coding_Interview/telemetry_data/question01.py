from collections import defaultdict

count = defaultdict(int)

# print(count["device1"])

# filter、map、reduce

'''
 - Container	Example
    List	[1, 2, 3]
    Tuple	(1, 2, 3)
    Set	{1, 2, 3}
    Dictionary	{"a":1, "b":2}
'''

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

def count_error_devices(devices):

  for key, value in devices:
    if value == "ERROR":
      count[key] += 1

  return dict(count)

expected = {
  "device1": 2,
  "device2": 1
}

result = count_error_devices(all_devices)

print(expected == result)