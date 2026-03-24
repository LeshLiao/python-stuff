from collections import defaultdict

transactions = [
    {"id": "t1", "amount": 100, "currency": "USD", "status": "APPROVED", "timestamp": 1000},
    {"id": "t2", "amount": 200, "currency": "USD", "status": "FAILED",   "timestamp": 1010},
    {"id": "t3", "amount": 50,  "currency": "EUR", "status": "APPROVED", "timestamp": 1020},
    {"id": "t4", "amount": 100, "currency": "USD", "status": "APPROVED", "timestamp": 1050},
    {"id": "t5", "amount": 50,  "currency": "EUR", "status": "FAILED",   "timestamp": 1100},
    {"id": "t6", "amount": 100, "currency": "USD", "status": "APPROVED", "timestamp": 1080},
]

sorted_list = transactions.copy()
sorted_list.sort(key=lambda x: x["timestamp"])


def solution_01():
  result = defaultdict(int)
  for item in transactions:
    if (item["status"] == "APPROVED"):
      currency = item["currency"]
      amount = item["amount"]
      result[currency] += amount
  return dict(result)


def find_failed_transaction(sorted_list, start, end):
  failed_list = []

  for item in sorted_list:
    if item["status"] != "FAILED":
      continue
    if (item["timestamp"] >= start and item["timestamp"] <= end):
      failed_list.append(item)

  return failed_list

def solution_03(window = 60):

  seem = {}
  duplicates = []

  for t in sorted_list:
    key = (t["amount"], t["currency"])
    #print(key)
    #break
    if key in seem:
      #print(t["id"])
      previous = seem[key]
      #print(previous["id"])
      #print(t["timestamp"] - previous["timestamp"])
      if t["timestamp"] - previous["timestamp"] <= window:
        #print("append")
        duplicates.append((previous["id"], t["id"]))

    seem[key] = t
  return duplicates





def run_all_test():

  print("1. test case")
  expected = {
    "USD": 300,
    "EUR": 50
  }
  sum_amount = solution_01()
  assert expected == sum_amount
  print("passed!")



  print("2. test case")
  expected_02 = [
      {"id": "t2", "amount": 200, "currency": "USD", "status": "FAILED",   "timestamp": 1010},
      {"id": "t5", "amount": 50,  "currency": "EUR", "status": "FAILED",   "timestamp": 1100},
  ]
  result_02 = find_failed_transaction(sorted_list, 1010, 1100)
  assert result_02 == expected_02
  print("passed!")



  print("3. test case")
  expected_03 = [('t1', 't4'), ('t4', 't6')]
  result_03 = solution_03(60)
  assert result_03 == expected_03
  print("passed!")

run_all_test()