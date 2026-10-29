# Converted from AI_LAB_ASS02.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
def dfs(graph,node,visited):
  if node not in visited:
    print(node, end=" ")
    visited.add(node)
    for neighbor in graph.get(node, []):
       dfs(graph,neighbor,visited)

graph={}
n= int(input("Enter the number of vertices:"))
for i in range(n):
  vertex=input(f"enter vertex {i+1}:")
  neighbors=input(f"Enter adjacent vertices of {vertex}(space-separated):").split()
  graph[vertex]= neighbors
start=input("Enter the starting vertex:")
print("\nGraph:",graph)
print("DFS Traversal:", end="")
visited = set() # Initialize the visited set
dfs (graph, start, visited)
