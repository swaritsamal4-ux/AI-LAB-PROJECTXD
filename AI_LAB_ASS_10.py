# Converted from AI_LAB_ASS_10.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
from itertools import permutations

def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for perm in permutations(cities):
        current_path = [start]
        current_cost = 0

        for city in perm:
            current_path.append(city)
            current_cost += graph[current_path[-2]][current_path[-1]]

        current_cost += graph[current_path[-1]][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost


n = int(input("Enter the number of cities: "))

graph = []

print("Enter the distance matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input(f"Enter the starting city (0 to {n - 1}): "))

best_path, min_cost = travelling_salesman(graph, start)

print("Best path:", " -> ".join(map(str, best_path)))
print("Minimum cost:", min_cost)
