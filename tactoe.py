# 3D tic tac toe AI, Dave

import sys
import copy
import random

cpuName = 'Dave'

lines = []

# Verts
lines.append([[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]])
lines.append([[0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 1, 3]])
lines.append([[0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 2, 3]])
lines.append([[0, 3, 0], [0, 3, 1], [0, 3, 2], [0, 3, 3]])
lines.append([[1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3]])
lines.append([[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3]])
lines.append([[1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3]])
lines.append([[1, 3, 0], [1, 3, 1], [1, 3, 2], [1, 3, 3]])
lines.append([[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 0, 3]])
lines.append([[2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 1, 3]])
lines.append([[2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 3]])
lines.append([[2, 3, 0], [2, 3, 1], [2, 3, 2], [2, 3, 3]])
lines.append([[3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3]])
lines.append([[3, 1, 0], [3, 1, 1], [3, 1, 2], [3, 1, 3]])
lines.append([[3, 2, 0], [3, 2, 1], [3, 2, 2], [3, 2, 3]])
lines.append([[3, 3, 0], [3, 3, 1], [3, 3, 2], [3, 3, 3]])

# Horizontals
lines.append([[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]])
lines.append([[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1]])
lines.append([[0, 0, 2], [0, 1, 2], [0, 2, 2], [0, 3, 2]])
lines.append([[0, 0, 3], [0, 1, 3], [0, 2, 3], [0, 3, 3]])
lines.append([[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 3, 0]])
lines.append([[1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1]])
lines.append([[1, 0, 2], [1, 1, 2], [1, 2, 2], [1, 3, 2]])
lines.append([[1, 0, 3], [1, 1, 3], [1, 2, 3], [1, 3, 3]])
lines.append([[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0]])
lines.append([[2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 3, 1]])
lines.append([[2, 0, 2], [2, 1, 2], [2, 2, 2], [2, 3, 2]])
lines.append([[2, 0, 3], [2, 1, 3], [2, 2, 3], [2, 3, 3]])
lines.append([[3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]])
lines.append([[3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 3, 1]])
lines.append([[3, 0, 2], [3, 1, 2], [3, 2, 2], [3, 3, 2]])
lines.append([[3, 0, 3], [3, 1, 3], [3, 2, 3], [3, 3, 3]])

# Other Horizontals
lines.append([[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]])
lines.append([[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1]])
lines.append([[0, 0, 2], [1, 0, 2], [2, 0, 2], [3, 0, 2]])
lines.append([[0, 0, 3], [1, 0, 3], [2, 0, 3], [3, 0, 3]])
lines.append([[0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0]])
lines.append([[0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1]])
lines.append([[0, 1, 2], [1, 1, 2], [2, 1, 2], [3, 1, 2]])
lines.append([[0, 1, 3], [1, 1, 3], [2, 1, 3], [3, 1, 3]])
lines.append([[0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0]])
lines.append([[0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1]])
lines.append([[0, 2, 2], [1, 2, 2], [2, 2, 2], [3, 2, 2]])
lines.append([[0, 2, 3], [1, 2, 3], [2, 2, 3], [3, 2, 3]])
lines.append([[0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0]])
lines.append([[0, 3, 1], [1, 3, 1], [2, 3, 1], [3, 3, 1]])
lines.append([[0, 3, 2], [1, 3, 2], [2, 3, 2], [3, 3, 2]])
lines.append([[0, 3, 3], [1, 3, 3], [2, 3, 3], [3, 3, 3]])

# Flat Diags
lines.append([[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0]])
lines.append([[3, 0, 0], [2, 1, 0], [1, 2, 0], [0, 3, 0]])
lines.append([[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1]])
lines.append([[3, 0, 1], [2, 1, 1], [1, 2, 1], [0, 3, 1]])
lines.append([[0, 0, 2], [1, 1, 2], [2, 2, 2], [3, 3, 2]])
lines.append([[3, 0, 2], [2, 1, 2], [1, 2, 2], [0, 3, 2]])
lines.append([[0, 0, 3], [1, 1, 3], [2, 2, 3], [3, 3, 3]])
lines.append([[3, 0, 3], [2, 1, 3], [1, 2, 3], [0, 3, 3]])

# Super Cross Diags
lines.append([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
lines.append([[3, 0, 0], [2, 1, 1], [1, 2, 2], [0, 3, 3]])
lines.append([[0, 3, 0], [1, 2, 1], [2, 1, 2], [3, 0, 3]])
lines.append([[3, 3, 0], [2, 2, 1], [1, 1, 2], [0, 0, 3]])

# Normal Diags
lines.append([[0, 0, 0], [0, 1, 1], [0, 2, 2], [0, 3, 3]])
lines.append([[1, 0, 0], [1, 1, 1], [1, 2, 2], [1, 3, 3]])
lines.append([[2, 0, 0], [2, 1, 1], [2, 2, 2], [2, 3, 3]])
lines.append([[3, 0, 0], [3, 1, 1], [3, 2, 2], [3, 3, 3]])
lines.append([[0, 0, 0], [1, 0, 1], [2, 0, 2], [3, 0, 3]])
lines.append([[0, 1, 0], [1, 1, 1], [2, 1, 2], [3, 1, 3]])
lines.append([[0, 2, 0], [1, 2, 1], [2, 2, 2], [3, 2, 3]])
lines.append([[0, 3, 0], [1, 3, 1], [2, 3, 2], [3, 3, 3]])
lines.append([[0, 3, 0], [0, 2, 1], [0, 1, 2], [0, 0, 3]])
lines.append([[1, 3, 0], [1, 2, 1], [1, 1, 2], [1, 0, 3]])
lines.append([[2, 3, 0], [2, 2, 1], [2, 1, 2], [2, 0, 3]])
lines.append([[3, 3, 0], [3, 2, 1], [3, 1, 2], [3, 0, 3]])
lines.append([[3, 0, 0], [2, 0, 1], [1, 0, 2], [0, 0, 3]])
lines.append([[3, 1, 0], [2, 1, 1], [1, 1, 2], [0, 1, 3]])
lines.append([[3, 2, 0], [2, 2, 1], [1, 2, 2], [0, 2, 3]])
lines.append([[3, 3, 0], [2, 3, 1], [1, 3, 2], [0, 3, 3]])

# TODO: Apply ML to these params?
cpuParams = [1, 100, 10000, 10 ** 10]
userParams = [100, 10000, 1000000, 10 ** 10]
bigVal = 10 ** 10

boardSize = 4
board = [[[None for x in xrange(boardSize)] for y in xrange(boardSize)] for z in xrange(boardSize)]

moveList = []
for a in xrange(boardSize):
  for b in xrange(boardSize):
    for c in xrange(boardSize):
      moveList.append([a, b, c])

userName = raw_input('Enter Name: ')
headsTails = raw_input('Heads or Tails? ')

def getNextMove(justMoved):
  if justMoved == cpuName:
    return userName
  else:
    return cpuName

def advanceSente(board, justMoved):
  global lines

  nextMove = getNextMove(justMoved)
 
  if justMoved == cpuName:

    # Check to see if cpu won
    for line in lines:
      counts = getCounts(board, line)

      if counts[0] == 4:
        return (board, justMoved)
    
    # Check for forcing moves
    for line in lines:
      counts = getCounts(board, line)      

      if (counts[0] == 3) and (counts[1] == 0):
        # User is forced
        print 'User will be forced. ', line
        
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:
            tmpBoard = copy.deepcopy(board)
            tmpBoard[pos[0]][pos[1]][pos[2]] = userName

            return advanceSente(tmpBoard, nextMove)
  else:
    # Check to see if user won
    for line in lines:
      counts = getCounts(board, line)

      if counts[1] == 4:
        return (board, justMoved)

    # Check for possible winning moves for cpu
    for line in lines:
      counts = getCounts(board, line)

      if (counts[0] == 3) and (counts[1] == 0):
        print 'CPU forced TO WIN! .', line
        
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:
            tmpBoard = copy.deepcopy(board)
            tmpBoard[pos[0]][pos[1]][pos[2]] = cpuName

            return (tmpBoard, cpuName)
    
    # Check for forcing moves
    for line in lines:
      counts = getCounts(board, line)

      if (counts[1] == 3) and (counts[0] == 0):
        # User is forced
        print 'Cpu will be forced. ', line
        
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:
            tmpBoard = copy.deepcopy(board)
            tmpBoard[pos[0]][pos[1]][pos[2]] = cpuName

            return advanceSente(tmpBoard, nextMove)

  return (board, justMoved)

def getCounts(board, line):
  userCount = 0
  cpuCount = 0

  for pos in line:
    if board[pos[0]][pos[1]][pos[2]] == userName:
      userCount = userCount + 1
    elif board[pos[0]][pos[1]][pos[2]] == cpuName:
      cpuCount = cpuCount + 1

  return (cpuCount, userCount)

# Higher rank == better for Dave
def getRank(theBoard):
  global lines

  # Push game forward to natural state through sente moves.
  sente = advanceSente(theBoard, cpuName)
  
  board = sente[0]

  rank = 0
  for line in lines:
    # Check who is on the line
    counts = getCounts(board, line)

    if counts[0] + counts[1] == 0:
      rank = rank + 0
    elif counts[0] * counts[1] > 0:
      rank = rank + 0
    elif counts[0] > 0:
      rank = rank + cpuParams[counts[0]-1]
    elif counts[1] > 0:
      rank = rank - userParams[counts[1]-1]

  return rank

def isWinner(board):
  global lines

  for line in lines:
    # line = [[0,0,0],[0,0,1],[0,0,2],[0,0,3]]
    user = board[line[0][0]][line[0][1]][line[0][2]]
    wonLine = False
    if user != None:
      matched = True
      
      for pos in line:
        if board[pos[0]][pos[1]][pos[2]] != user:
          matched = False
          break
      
      if matched:
        return True

  return False

def userMove(userName):
  userInput = raw_input('Please enter position (space separated) x y z: ')
  i = [int(a) for a in userInput.split(' ')]
  if (len(i) == 3) and (i[0] >= 0) and (i[0] < boardSize) and (i[1] >= 0) and (i[1] < boardSize) and (i[2] >= 0) and (i[2] < boardSize):
    if board[i[0]][i[1]][i[2]] != None:
      print 'Can not move here bro. ' + board[i[0]][i[1]][i[2]] + ' has a stone here.'
    else:
      print 'User Moved: ', i
      board[i[0]][i[1]][i[2]] = userName

def cpuMove(board):
  global moveList, lines
  
  highestRanked = -1 * (10 ** 10)
  moveToChoose = None
  
  # Are we forced?
  for line in lines:
    counts = getCounts(board, line)
    if (counts[0] == 0) and (counts[1] == 3):
      print 'Cpu is forced. ', line
        
      for pos in line:
        if board[pos[0]][pos[1]][pos[2]] == None:
          # moveToChoose = board[pos[0]][pos[1]][pos[2]]

          print cpuName + ' Moves Here: ', pos[0], pos[1], pos[2]
          board[pos[0]][pos[1]][pos[2]] = cpuName
          return

    if (counts[1] == 0) and (counts[0] == 3):
      print 'Cpu is forced... TO WIN ', line
        
      for pos in line:
        if board[pos[0]][pos[1]][pos[2]] == None:
          # moveToChoose = board[pos[0]][pos[1]][pos[2]]

          print cpuName + ' Moves Here: ', pos[0], pos[1], pos[2]
          board[pos[0]][pos[1]][pos[2]] = cpuName
          return

  for move in moveList:
    if board[move[0]][move[1]][move[2]] == None:
      tmpBoard = copy.deepcopy(board)
      tmpBoard[move[0]][move[1]][move[2]] = cpuName
      # print '     move ', move
      potentialRank = getRank(tmpBoard)

      if potentialRank > highestRanked:
        highestRanked = potentialRank
        moveToChoose = move

  print cpuName + ' Moves Here: ', moveToChoose
  board[moveToChoose[0]][moveToChoose[1]][moveToChoose[2]] = cpuName

if random.random() < 0.5:
  print headsTails + '! ' + userName + ' goes first.'
else:
  print 'Nope! ' + cpuName + ' goes first.'
  cpuMove(board)

while True:
  userMove(userName)
  if isWinner(board):
    print userName + ' has won!!! Good job!'
    break
  cpuMove(board)
  if isWinner(board):
    print cpuName + ' has won!!! You Suck!'
    break


