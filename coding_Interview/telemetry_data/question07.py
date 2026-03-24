

'''

val transactions : listOf(
    "id" : "tx_101", "amount" : 5000, "currency" : "USD", "status" : "SUCCESS"),
    "id" : "tx_102", "amount" : 2500, "currency" : "USD", "status" : "FAILED"),
    "id" : "tx_103", "amount" : 3000, "currency" : "TWD", "status" : "SUCCESS"),  #93
    "id" : "tx_104", "amount" : 1500, "currency" : "HKD", "status" : "SUCCESS"),  #195
    "id" : "tx_105", "amount" : 4500, "currency" : "USD", "status" : "SUCCESS")
)

'''

transactions = [
    {"id" : "tx_101", "amount" : 5000, "currency" : "USD", "status" : "SUCCESS"},
    {"id" : "tx_102", "amount" : 2500, "currency" : "USD", "status" : "FAILED"},
    {"id" : "tx_103", "amount" : 3000, "currency" : "TWD", "status" : "SUCCESS"},
    {"id" : "tx_104", "amount" : 1500, "currency" : "HKD", "status" : "SUCCESS"},
    {"id" : "tx_105", "amount" : 4500, "currency" : "USD", "status" : "SUCCESS"}
]

def get_total_by_currency(currency):
  total = 0
  for t in transactions:
    if t["currency"] == currency and t["status"] == "SUCCESS":
      total += t["amount"]
  return total

def converter_total_by_currency(base):
  currency_table = {
    ("TWD","USD"): 0.031,
    ("HKD","USD"): 0.13 ,
    ("USD","USD"): 1,

    ("USD","TWD"): 32.19,
    ("USD","HKD"): 7.83,
  }

  total_usd_dollar = 0
  for t in transactions:
    key = (t["currency"], "USD")
    total_usd_dollar += t["amount"] * currency_table[key]

  base_key = ("USD",base)

  return total_usd_dollar * currency_table[base_key]

def is_refund_success(id, amount):

  for t in transactions:
    if t["id"] == id:
      if amount <= t["amount"]:
        return True
      else:
        print("your refund amount is invalid.")
        return False

  print("your refund is not found.")
  return False

def run_all_test():
  result_01 = get_total_by_currency("USD")
  expected_01 = 9500
  assert result_01 == expected_01
  print("1. passed!")

  result_02 = converter_total_by_currency("TWD")
  expected_02 = 395550.72
  assert (abs(result_02 - expected_02) < 0.00001)
  print("2. passed!")


  result_03 = is_refund_success("tx_105", 4000)
  expected_03 = True
  assert result_03 == expected_03
  print("3. passed!")

  result_03_1 = is_refund_success("tx_105", 6000)
  expected_03_1 = False
  assert result_03_1 == expected_03_1
  print("3_1. passed!")

  result_03_2 = is_refund_success("tx_110", 3000)
  expected_03_2 = False
  assert result_03_2 == expected_03_2
  print("3_2. passed!")


run_all_test()