# Converted from AI_LAB_ASS_06.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 2
import math
def alpha_beta(nodeIndex, values, height, depth, alpha, beta, maximizingPlayer):
    if depth == height:
       # Adjust nodeIndex to correctly access the values list, which only contains leaf nodes
       # The first leaf node in a 0-indexed complete binary tree at depth `height` is at index 2**height - 1
       leaf_index_offset = (2**height - 1)
       return values[nodeIndex - leaf_index_offset]
    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(nodeIndex * 2 + i + 1, values, height, depth + 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(nodeIndex * 2 + i + 1, values, height, depth + 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = alpha_beta(
    0,
    values,
    height,
    0,
    -math.inf,
    math.inf,
    True
)

print("\nOptimal value:", result)
