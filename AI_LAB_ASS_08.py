# Converted from AI_LAB_ASS_08.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
from collections import deque
def water_jug(capacity1, capacity2, target):
  visited = set()
  queue = deque()
  queue.append((0, 0, []))

  while queue:
    jug1, jug2, path = queue.popleft()

    if (jug1, jug2) in visited:
      continue
    visited.add((jug1, jug2))

    current_path = path + [(jug1, jug2)]
    if jug1 == target or jug2 == target:
      return current_path

    next_states = [
        (capacity1, jug2, current_path.copy()),
        (jug1, capacity2, current_path.copy()),
        (0, jug2, current_path.copy()),
        (jug1, 0, current_path.copy()),
        (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2), current_path.copy()),
        (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1), current_path.copy())
    ]

    for next_jug1, next_jug2, next_path in next_states:
        if (next_jug1, next_jug2) not in visited:
            queue.append((next_jug1, next_jug2, next_path))

  return None

jug1 = int(input("Enter capacity of jug1: "))
jug2 = int(input("Enter capacity of jug2: "))
target = int(input("Enter target capacity: "))

solution = water_jug(jug1, jug2, target)

if solution:
  print("Solution path:")
  for state in solution:
    print(state)
else:
  print("Solution not found")
