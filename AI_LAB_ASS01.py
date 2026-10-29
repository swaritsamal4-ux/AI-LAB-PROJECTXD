# Converted from AI_LAB_ASS01.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
print("welcome to CSEAIML")

# %% Code Cell 2
from collections import deque

def bfs(graph, start):
  visited = set()
  queue = deque([start])
  visited.add(start)
  print("BFS Traversal:", end="")

  while queue:
    vertex = queue.popleft()
    print(vertex, end=" ") # Added space for better output formatting
    for neighbor in graph.get(vertex, []): # Use .get() to handle cases where a vertex might not have neighbors
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

# Code for graph input and calling BFS
graph = {}
n = int(input("Enter the number of vertices:"))
for i in range(n):
  vertex = input(f"Enter vertex {i+1}:")
  neighbors = input(f"Enter adjacent vertices of {vertex} (space-separated):").split()
  graph[vertex] = neighbors

start = input("Enter the starting vertex:")

print("\nGraph:", graph)
bfs(graph, start)
