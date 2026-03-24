
'''

val logs = listOf(
    "2026-03-14 10:00:01,DEV_001,ERR_CHIP_READ,Timeout",
    "2026-03-14 10:01:20,DEV_002,ERR_CHIP_READ,Power failure",
    "2026-03-14 10:02:05,DEV_001,SUCCESS,Transaction complete",
    "2026-03-14 10:03:45,DEV_001,ERR_CHIP_READ,Incomplete read",
    "2026-03-14 10:05:12,DEV_003,ERR_NETWORK,No route to host"
)



'''

from enum import Enum
from collections import defaultdict

class FILED(Enum):
    DATE = 0
    DEVICE = 1
    ERROR = 2
    MESSAGE = 3

logs = [
    "2026-03-14 10:00:01,DEV_001,ERR_CHIP_READ,Timeout",
    "2026-03-14 10:01:20,DEV_002,ERR_CHIP_READ,Power failure",
    "2026-03-14 10:02:05,DEV_001,SUCCESS,Transaction complete",
    "2026-03-14 10:03:45,DEV_001,ERR_CHIP_READ,Incomplete read",
    "2026-03-14 10:05:12,DEV_003,ERR_NETWORK,No route to host"
]


data_list = []  # 2D list

for log in logs:
  data_list.append(log.split(","))

#print(data_list)

def filter_out_by_error(error_name):
  result = []
  for index ,data in enumerate(data_list):
    if data[FILED.ERROR.value] == error_name:
      result.append(logs[index])
  return result



expected = [
  "2026-03-14 10:05:12,DEV_003,ERR_NETWORK,No route to host"
]

result = filter_out_by_error("ERR_NETWORK")

#print(result)

#print("test case:")
print(result == expected)

'''
find out the error: if error name start with "ERR"
'''


def get_the_failing_most_device_id():
  my_map = defaultdict(int)
  for element in data_list:
    if "ERR" in element[FILED.ERROR.value]:
      device_id = element[FILED.DEVICE.value]
      my_map[device_id] += 1

  max_device_id = ""
  max_count = 0
  for key in my_map:
    if my_map[key] > max_count:
      max_count = my_map[key]
      max_device_id = key

  return max_device_id

expected_02 = "DEV_001"
result_02 = get_the_failing_most_device_id()

print(result_02 == expected_02)

'''

window_range = 3
len(data_list) = 5

0 1 [2 3 4]


'''

def check_log_health(failed_num, window_range):

  for i in range(len(data_list)-window_range+1):
    count = 0
    for j in range(window_range):
      if "ERR" in data_list[i+j][FILED.ERROR.value]:
        count += 1
        if count >= failed_num:
          return False

  return True

result_03 = check_log_health(2,3)
expected_03 = False

print(result_03 == expected_03)



def check_log_health_sliding_window(failed_num, window_range):

  left = 0
  window = []
  count = 0
  for right in range(len(data_list)):

    #window.append(data_list[right])
    if "ERR" in data_list[right][FILED.ERROR.value]:
      count += 1

    if (right-left+1) > window_range:
      #left_item = window.pop()
      left_item = data_list[left]
      left += 1
      if "ERR" in left_item[FILED.ERROR.value]:
        count -= 1

    if count >= failed_num:
      return False

result_03_1 = check_log_health(2,3)
print(result_03_1 == False)