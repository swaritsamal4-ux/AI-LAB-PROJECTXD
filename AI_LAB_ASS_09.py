# Converted from AI_LAB_ASS_09.ipynb
# Jupyter Notebook -> Python script

# %% Code Cell 1
def print_board(board):
  for row in board:
    print("|".join(row))
    print("-"*9)

def check_winner(board):
  # Check rows
  for row in board:
    if row[0]==row[1]==row[2] != "":
      return True
  # Check columns
  for col in range(3):
    if board[0][col]==board[1][col]==board[2][col]!="":
      return True
  # Check diagonals
  if board[0][0]==board[1][1]==board[2][2]!="":
    return True
  if board[0][2]==board[1][1]==board[2][0]!="":
    return True
  return False

board=[[""for _ in range(3)]for _ in range(3)]
player="x"
for turn in range(9):
  print("\nCurrent Board:")
  print_board(board)
  print(f"player {player}'s Turn")
  row=int(input("enter row(0-2):"))
  col=int(input("enter col(0-2):"))

  if board[row][col]=="":
    board[row][col]=player
    if check_winner(board):
      print("\nFinal Board:")
      print_board(board)
      print(f"player {player} wins!")
      break
    player="0" if player=="x" else"x"
else:
    print("\nFinal Board:")
    print_board(board)
    print("Game Draw!")
