from collections import deque, defaultdict

graph = defaultdict()

graph[0] = [1,2]
graph[1] = [3,4]
graph[2] = [5,6]
graph[3] = []
graph[4] = []
graph[5] = []
graph[6] = []

# ===== dfs =====

visited = set()

visited.clear()

def dfs(node):
  if node in visited:
    return

  visited.add(node)
  print(str(node) + ",")

  for neighbor in graph[node]:
    if neighbor not in visited:
      dfs(neighbor)

dfs(0)

# ===== bfs =====

visited.clear()

def bfs(node):

  queue = deque()
  queue.append(node)

  while queue:
    node = queue.popleft()
    visited.add(node)
    print(str(node) + ",")

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

bfs(0)