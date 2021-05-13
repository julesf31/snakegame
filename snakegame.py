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

fyp = random.randint(1, 7)
fxp = random.randint(1, 7)
board[fyp][fxp] = '0'

snake = [[1, 1]]
for i in snake:
  syp = i[0]
  sxp = i[1]
  board[syp][sxp] = 'x'

for k in board:
  print(*k)

def movement(move):
  global snake
  global direction
  global board

  for i in snake:
    syp = i[0]
    sxp = i[1]
    board[syp][sxp] = ' '

  if move == 'w':
    if direction == 'down':
      return
    for i in snake:
      i[0] -= 1
    direction == 'up'

  if move == 's':
    if direction == 'up':
      return
    for i in snake:
      i[0] += 1
    direction == 'down'

  if move == 'a':
    if direction == 'right':
      return
    for i in snake:
      i[1] -= 1
    direction == 'left'

  if move == 'd':
    if direction == 'left':
      return
    for i in snake:
      i[1] += 1
    direction == 'right'

  for i in snake:
    syp = i[0]
    sxp = i[1]
    board[syp][sxp] = 'x'
  for k in board:
    print(*k)


direction = 'down'
while True:
  move = input('Enter Direction: ')
  movement(move)























'''def print_board(board):
  for i in board:
    print(*i)

ypos = 1
xpos = 1
board[ypos][xpos] = "x"

def new_fruit_pos(board):
  if ypos == 0:
    return 
  elif ypos == 9:
    return
  global lenth
  if board[ypos][xpos] == '0':
    fruitypos = random.randint(1, 7)
    fruitxpos = random.randint(1, 7)
    if board[fruitypos][fruitxpos] == 'x':
      fruitypos = random.randint(1, 7)
      fruitxpos = random.randint(1, 7)
    board[fruitypos][fruitxpos] = '0'
    lenth += 1
  return lenth

def draw_lenth(board, snake, xpos, ypos):
  #snake.append(str(ypos) + ' ' + str(xpos))
  print(snake)
  for i in snake:
    throwaway = i.split(' ')
    ypos, xpos = throwaway[0], throwaway[1]
    board[int(ypos)][int(xpos)] = 'x'
  del snake[-1]
  for i in board:
    print(*i)

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
snake = []
while 1:
  move = input('Enter direction (wasd): ')
  if move == 'w':
    print('')
    board[ypos][xpos] = ' '
    ypos -= 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board)
    board[ypos][xpos] = 'x'
    print_board(board)
    print('Lenth = ' + str(lenth))
  #-----------------------------------------------
  elif move == 's':
    print('')
    board[ypos][xpos] = ' '
    snake.append(str(ypos) + ' ' + str(xpos))
    ypos += 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board)
    board[ypos][xpos] = 'x'
    draw_lenth(board, snake, xpos, ypos)
    #print_board(board) - likely doesn't need to be here
    print('Lenth = ' + str(lenth))
  #-----------------------------------------------
  elif move == 'a':
    print('')
    board[ypos][xpos] = ' '
    xpos -= 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board)
    board[ypos][xpos] = 'x'
    print_board(board)
    print('Lenth = ' + str(lenth))
  #-----------------------------------------------
  elif move == 'd':
    print('')
    board[ypos][xpos] = ' '
    xpos += 1
    check_for_collision(ypos, xpos, board)
    if l == 1:
      break
    new_fruit_pos(board)
    board[ypos][xpos] = 'x'
    print_board(board)
    print('Lenth = ' + str(lenth))

print('bad')'''