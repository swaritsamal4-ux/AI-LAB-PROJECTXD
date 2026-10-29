# Converted from AI_LAB_07.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
def print_board(board):
  for row in board:
    print("".join(row))

def is_safe(board,row,col):
  n = len(board) # Get board size dynamically
  for i in range(row):
    if board[i][col]=='Q':
      return False

  i = row-1
  j = col-1
  while i>= 0 and j>= 0:
    if board[i][j]=='Q':
      return False
    i -= 1
    j -= 1

  i = row-1
  j = col+1
  while i >=0 and j < n: # Use n for board size
    if board[i][j]=='Q':
      return False

    i-=1
    j+=1

  return True

def solved(board,row):
  n = len(board) # Get board size dynamically
  if row == n: # Base case depends on n
    return True

  for col in range(n): # Loop depends on n
    if is_safe(board,row,col):
      board[row][col]='Q'

      if solved(board, row+1):
        return True

      board[row][col]='.'
  return False

# Initialize a 4x4 board
board=[['.' for _ in range(4)] for _ in range(4)]

if solved(board,0):
  print("\nSolution for 4-queen problem:\n")
  print_board(board)
else:

  print("No Solution Exists.")

# %% Code Cell 2
def print_board(board):
  for row in board:
    print("".join(row))

def is_safe(board,row,col):
  n = len(board)
  for i in range(row):
    if board[i][col]=='Q':
      return False

  i = row-1
  j = col-1
  while i>= 0 and j>= 0:
    if board[i][j]=='Q':
      return False
    i -= 1
    j -= 1

  i = row-1
  j = col+1
  while i >=0 and j < n:
    if board[i][j]=='Q':
      return False

    i-=1
    j+=1

  return True

def solved(board,row):
  n = len(board)
  if row == n:
    return True

  for col in range(n):
    if is_safe(board,row,col):
      board[row][col]='Q'

      if solved(board, row+1):
        return True

      board[row][col]='.'
  return False

# Initialize an 8x8 board
board=[['.' for _ in range(8)] for _ in range(8)]

if solved(board,0):
  print("\nSolution for 8-queen problem:\n")
  print_board(board)
else:

  print("No Solution Exists.")
