
from collections import defaultdict


transactions = [
  ("store1", 100),
  ("store2", 200),
  ("store1", 50),
  ("store3", 300)
]


def count_stores_amount():
  amount = defaultdict(int)
  for key, value in transactions:
    amount[key] += value

  return dict(amount)

result2 = count_stores_amount()

expected2 = {
  'store1': 150,
  'store2':200,
  'store3':300
}

print(expected2 == result2)
