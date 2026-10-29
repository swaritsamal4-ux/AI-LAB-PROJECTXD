# Converted from AI_LAB_ASS_04.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 2
import heapq

def astar(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    pq, (new_f, new_g, neighbor,
                         path + [neighbor])
                )

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'G': []
}

h = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'G': 0
}

path, cost = astar(graph, 'A', 'G', h)

print("Shortest Path:", path)
print("Total Cost:", cost)
