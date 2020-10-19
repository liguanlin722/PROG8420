#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_03
#Creation Date: 2020.10.13
#Author: Guanlin Li
#StudentID: 8674601

# creat tic tac toe board
def initBoard():
  global board  # declare a global variable
  board = [None] * 3
  print("Tic Tac Toe：")
  for i in range(len(board)):
    board[i] = ["+ "] * 3


# print board
def printBoard():
  global board
  for i in range(len(board)):
    for j in range(len(board[i])):
      print(board[i][j], end=" ")
    print("")


# start game
def startGame():
  global board
  player = 0
  while isGameContinue():
    if player <= 8:
      if player % 2 == 0:
        # black turn
        print("==>Black Turn")
        if not playChess("x"):
          continue
      else:
        # white turn
        print("==>White Turn")
        if not playChess("○"):
          continue
      player += 1
    else:
      print("Draw")
      break


def playChess(chess):
  # get the position
  x = int(input("==> X=")) - 1
  y = int(input("==> Y=")) - 1
  if board[x][y] == "+ ":
    board[x][y] = chess
    printBoard()
    return True  # the block is available
  else:
    print("==> There is already a piece, please set again.\a")
    printBoard()
    return False  # the block is unavailable


def isGameContinue():
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] != "+ ":
        # check by row
        if j == 0:
          if board[i][j] == board[i][j + 1] == board[i][j + 2]:
            whoWin(i, j)
            return False
        # check by column
        if i == 0:
          if board[i][j] == board[i + 1][j] == board[i + 2][j]:
            whoWin(i, j)
            return False
        # check from left down corner to right up corner
        if i == 0 and j == 0:
          if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]:
            whoWin(i, j)
            return False
        # check from left up corner to right down corner
        if i == 2 and j == 0:
          if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2]:
            whoWin(i, j)
            return False
  return True


def whoWin(i, j):
  if board[i][j] == "x":
    print("Black Win！")
  else:
    print("White Win！")

board = []
initBoard()
printBoard()
startGame()
