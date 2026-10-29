# Converted from AI_LAB_ASS03.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
def objective_function(x):
  return -((x-8)**2)+45
print(objective_function(8))

# %% Code Cell 2
def objective_function(x):
  return -((x-8)**2)+64
print(objective_function(8))

# %% Code Cell 3
def objective_function(x):
  return -(x-10)**2+100
print(objective_function(10))

# %% Code Cell 4
def objective_function(x):
  return -(x**2)+10

def hill_climbing(start, step_size, max_iterations):
    current=start
    current_value=objective_function(current)


    for i in range(max_iterations):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break

    return current, current_value
start = float(input("Enter the starting point: "))
step_size = float(input("Enter the step size: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

best_point, best_value = hill_climbing(start, step_size, max_iterations)
print("Best point:", best_point)
print("Best value:", best_value)
