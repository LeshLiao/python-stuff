from collections import defaultdict

graph = defaultdict(list)

# ============
# graph[0] = [1,2]
# graph[1] = [2]
# graph[2] = [0,3]
# graph[3] = [3]

# ============
# graph[0] = [1, 2, 3]
# graph[1] = [4, 5]
# graph[2] = [0, 6]
# graph[3] = [7]
# graph[4] = [8]
# graph[5] = [9, 10]
# graph[6] = [2, 11]
# graph[7] = [3, 12]
# graph[8] = []
# graph[9] = []
# graph[10] = [13]
# graph[11] = [6]
# graph[12] = []
# graph[13] = []



# ============

# graph = {
#     0: [10],
#     1: [4],
#     2: [8],
#     3: [7, 9, 1],
#     4: [1, 2, 11],
#     5: [],
#     6: [7, 6],
#     7: [7],
#     8: [2, 12],
#     9: [0, 8, 9],
#     10: [6],
#     11: [4],
#     12: [12],
#     13: [2]
# }

# ============
# Define the graph as an adjacency list
# graph = {
#     0: [10],
#     1: [4],
#     2: [8],
#     3: [7, 9, 1],
#     4: [1, 2, 11],
#     5: [],
#     6: [7, 6],
#     7: [7],
#     8: [2, 12],
#     9: [0, 8, 9],
#     10: [6],
#     11: [4],
#     12: [12],
#     13: [2]
# }


# visited = set()

# def DFS(index):

#     if index in visited:
#         return

#     visited.add(index)

#     print(index, end = " ")
#     for neighbor in graph[index]:
#         DFS(neighbor)


# DFS(0)  # 0 1 4 8 5 9 10 13 2 6 11 3 7 12



# ================================================

# Create a list
# queue = []
# visited = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# def popQueueFromLeft():
#   if len(queue) > 0:
#     value = queue.pop(0)
#     # print(value)
#     return value


# def BFS(index):

#   if visited[index]:
#     return
#   queue.append(index)
#   visited[index] = True

#   while queue:
#     index = popQueueFromLeft()
#     print(index)

#     for neighbor in graph[index]:
#       if visited[neighbor] == False:
#         queue.append(neighbor)
#         visited[neighbor] = True

# BFS(0)




# output: [0, 10, 6, 7]




# import sys
# print(sys.version)
# import networkx as nx
# import matplotlib.pyplot as plt

# Define the graph as an adjacency list
# graph = {
#     0: [10],
#     1: [4],
#     2: [8],
#     3: [7, 9, 1],
#     4: [1, 2, 11],
#     5: [],
#     6: [7, 6],
#     7: [7],
#     8: [2, 12],
#     9: [0, 8, 9],
#     10: [6],
#     11: [4],
#     12: [12],
#     13: [2]
# }

# graph[0] = [1,2]
# graph[1] = [2]
# graph[2] = [0,3]
# graph[3] = [3]


# # Initialize a directed graph
# G = nx.DiGraph()

# # Add edges to the graph
# for node, neighbors in graph.items():
#     for neighbor in neighbors:
#         G.add_edge(node, neighbor)

# # Draw the graph
# plt.figure(figsize=(10, 8))
# pos = nx.spring_layout(G)  # Positioning the nodes using the spring layout
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrowstyle='->', arrowsize=15)
# plt.title('Graph Visualization')
# plt.show()



graph[0] = [1, 2, 3]
graph[1] = [4, 5]
graph[2] = [0, 6]
graph[3] = [7]
graph[4] = [8]
graph[5] = [9, 10]
graph[6] = [2, 11]
graph[7] = [3, 12]
graph[8] = []
graph[9] = []
graph[10] = [13]
graph[11] = [6]
graph[12] = []
graph[13] = []


visited = set()

def my_dfs(index):
    if index in visited:
        return
    visited.add(index)

    for node in graph[index]:
        if node not in visited:
            my_dfs(node)

    print(index, end = " ")


my_dfs(0)