from colorama import Fore, Back, Style
import random

print('     ' + Fore.YELLOW, Back.GREEN + 'Snake!' + Style.RESET_ALL)

boardtop = ['X---------------X']
board = []

board.append(boardtop)
for i in range(8):
  row = []
  row.append('|')
  for j in range(7):
    row.append(' ')
  row.append('|')
  board.append(row)
board.append(boardtop)

def print_board(board):
  for i in board:
    print(*i)

ypos = 1
xpos = 1
board[ypos][xpos] = "x"

def new_fruit_pos(board, lenth):
  if board[ypos][xpos] == '0':
    fruitypos = random.randint(1, 7)
    fruitxpos = random.randint(1, 7)
    board[fruitypos][fruitxpos] = '0'
    lenth += 1
  return lenth

#def draw_lenth(lenth):
#  for i in range(lenth):
    

fruitypos = random.randint(1, 7)
fruitxpos = random.randint(1, 7)
board[fruitypos][fruitxpos] = '0'

print_board(board)
lenth = 1
win = 0
while win != 1:
  move = input('Enter direction (wasd): ')
  if move == 'w':
    board[ypos][xpos] = ' '
    ypos -= 1
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 's':
    board[ypos][xpos] = ' '
    ypos += 1
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 'a':
    board[ypos][xpos] = ' '
    xpos -= 1
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 'd':
    board[ypos][xpos] = ' '
    xpos += 1
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)