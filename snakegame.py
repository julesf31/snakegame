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
  if ypos == 0:
    return 
  elif ypos == 9:
    return
  elif board[ypos][xpos] == '0':
    fruitypos = random.randint(1, 7)
    fruitxpos = random.randint(1, 7)
    if board[fruitypos][fruitxpos] == 'x':
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

def check_for_collision(ypos, xpos, board):
  global l
  if ypos == 0:
    l = 1
    return l
  elif ypos == 9:
    l += 1
    return l
  elif board[ypos][xpos] == 'x':
    l += 1
    return l
  elif board[ypos][xpos] == '|':
    l += 1
    return l

print_board(board)
lenth = 1
l = 0
while 1:
  move = input('Enter direction (wasd): ')
  if move == 'w':
    board[ypos][xpos] = ' '
    ypos -= 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 's':
    board[ypos][xpos] = ' '
    ypos += 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 'a':
    board[ypos][xpos] = ' '
    xpos -= 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)
  elif move == 'd':
    board[ypos][xpos] = ' '
    xpos += 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board, lenth)
    board[ypos][xpos] = 'x'
    print_board(board)

print('bad')