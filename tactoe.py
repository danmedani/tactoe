# 3D tic tac toe AI, Dave

import sys
import copy
import random

class Game:
  def __init__(self, p1, p2, lines):
    self.players = (p1, p2)

    self.boardSize = 4
    self.board = [[[None for x in xrange(boardSize)] for y in xrange(boardSize)] for z in xrange(boardSize)]

    self.lines = lines

  def play(self):
    currentPlayer = 0
    if random.random() < 0.5:
      currentPlayer = 1
    
    while True:
      moveRes = self.players[currentPlayer].move(self.board)
      if moveRes[0] == None:
        return self.players[currentPlayer].getName()
      
      print self.players[currentPlayer].getName(), 'moved here:', moveRes[0]
      self.board = moveRes[1]

      if self.isWinner():
        print self.players[currentPlayer].getName() + ' has won!!! Good job!'
        return self.players[currentPlayer].getName()
        break

      currentPlayer = 1 - currentPlayer

  def isWinner(self):
    for line in self.lines:
      # line = [[0,0,0],[0,0,1],[0,0,2],[0,0,3]]
      user = self.board[line[0][0]][line[0][1]][line[0][2]]
      wonLine = False
      if user != None:
        matched = True
        
        for pos in line:
          if self.board[pos[0]][pos[1]][pos[2]] != user:
            matched = False
            break
        
        if matched:
          return True

    return False

class User:
  def __init__(self):
    self.userName = raw_input('Enter Name: ')

  def getName(self):
    return self.userName

  def move(self, board):
    userInput = raw_input('Please enter position (space separated) x y z: ')
    i = [int(a) for a in userInput.split(' ')]
    if (len(i) == 3) and (i[0] >= 0) and (i[0] < boardSize) and (i[1] >= 0) and (i[1] < boardSize) and (i[2] >= 0) and (i[2] < boardSize):
      if board[i[0]][i[1]][i[2]] != None:
        print 'Can not move here bro. ' + board[i[0]][i[1]][i[2]] + ' has a stone here.'
      else:
        # print 'User Moved: ', i
        board[i[0]][i[1]][i[2]] = self.userName
        return (i[0],i[1],i[2]), board

class AI:
  def __init__(self, boardSize, cpuName, opponentName, cpuParams, userParams, lines):
    self.cpuName = cpuName
    self.opponentName = opponentName
    self.cpuParams = cpuParams
    self.userParams = userParams
    self.lines = lines
    
    self.moveList = []
    for a in xrange(boardSize):
      for b in xrange(boardSize):
        for c in xrange(boardSize):
          self.moveList.append([a, b, c])

  def getName(self):
    return self.cpuName

  def move(self, board):
    highestRanked = -1 * (10 ** 90)
    moveToChoose = None
    
    # Are we forced to win?
    for line in self.lines:
      counts = self.getCounts(board, line)

      if (counts[1] == 0) and (counts[0] == 3):        
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:

            # print self.cpuName + ' Moves Here: ', pos[0], pos[1], pos[2]
            board[pos[0]][pos[1]][pos[2]] = self.cpuName
            return pos, board

    # Are we forced to move?
    for line in lines:
      counts = self.getCounts(board, line)
    
      if (counts[0] == 0) and (counts[1] == 3):
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:

            # print cpuName + ' Moves Here: ', pos[0], pos[1], pos[2]
            board[pos[0]][pos[1]][pos[2]] = self.cpuName
            return pos, board

    # No forced moves... Let's look for a good one
    moveFound = False
    for move in self.moveList:
      if board[move[0]][move[1]][move[2]] == None:
        moveFound = True
        tmpBoard = copy.deepcopy(board)
        tmpBoard[move[0]][move[1]][move[2]] = self.cpuName
        # print '     move ', move
        potentialRank = self.getRank(tmpBoard)

        if potentialRank > highestRanked:
          highestRanked = potentialRank
          moveToChoose = move

    if not moveFound:
      print 'Cat Game'
      return None, board
    # print moveToChoose
    # print self.cpuName + ' Moves Here: ', moveToChoose
    board[moveToChoose[0]][moveToChoose[1]][moveToChoose[2]] = self.cpuName
    return moveToChoose, board

  def getNextMove(self, justMoved):
    if justMoved == self.cpuName:
      return self.opponentName
    else:
      return self.cpuName

  def advanceSente(self, board, justMoved):
    global lines

    nextMove = self.getNextMove(justMoved)
   
    if justMoved == self.cpuName:

      # Check to see if cpu won
      for line in lines:
        counts = self.getCounts(board, line)

        if counts[0] == 4:
          return (board, justMoved)
      
      # Check for forcing moves
      for line in lines:
        counts = self.getCounts(board, line)    

        if (counts[0] == 3) and (counts[1] == 0):
          # User is forced
          for pos in line:
            if board[pos[0]][pos[1]][pos[2]] == None:
              tmpBoard = copy.deepcopy(board)
              tmpBoard[pos[0]][pos[1]][pos[2]] = self.opponentName

              return self.advanceSente(tmpBoard, nextMove)
    else:
      # Check to see if user won
      for line in lines:
        counts = self.getCounts(board, line)

        if counts[1] == 4:
          return (board, justMoved)

      # Check for possible winning moves for cpu
      for line in lines:
        counts = self.getCounts(board, line)

        if (counts[0] == 3) and (counts[1] == 0):
          for pos in line:
            if board[pos[0]][pos[1]][pos[2]] == None:
              tmpBoard = copy.deepcopy(board)
              tmpBoard[pos[0]][pos[1]][pos[2]] = self.cpuName

              return (tmpBoard, self.cpuName)
      
      # Check for forcing moves
      for line in lines:
        counts = self.getCounts(board, line)

        if (counts[1] == 3) and (counts[0] == 0):
          # User is forced        
          for pos in line:
            if board[pos[0]][pos[1]][pos[2]] == None:
              tmpBoard = copy.deepcopy(board)
              tmpBoard[pos[0]][pos[1]][pos[2]] = self.cpuName

              return self.advanceSente(tmpBoard, nextMove)

    return (board, justMoved)

  def getCounts(self, board, line):
    userCount = 0
    cpuCount = 0

    for pos in line:
      if board[pos[0]][pos[1]][pos[2]] == self.opponentName:
        userCount = userCount + 1
      elif board[pos[0]][pos[1]][pos[2]] == self.cpuName:
        cpuCount = cpuCount + 1

    return (cpuCount, userCount)

  # Higher rank == better for Dave
  def getRank(self, theBoard):
    # Push game forward to natural state through sente moves.
    newBoardState = self.advanceSente(theBoard, self.cpuName)
    newBoard = newBoardState[0]
    justMoved = newBoardState[1]

    if justMoved == self.cpuName:
      for line in self.lines:
        counts = self.getCounts(newBoard, line)
        if counts[0] == 4:
          # we won
          return 10 ** 40

      # Check to see if there are any spots where if the user moved there, there would be more than 1
      # 3 count for the user (0 cpu). If that spot is there, then this is a losing position.
      for move in self.moveList:
        tmpBoard = copy.deepcopy(newBoard)
        tmpBoard[move[0]][move[1]][move[2]] = self.opponentName

        threeCounts = 0
        for line in self.lines:
          # Check who is on the line
          counts = self.getCounts(tmpBoard, line)

          if (counts[0] == 0) and (counts[1] == 3):
            threeCounts = threeCounts + 1

        if threeCounts > 1:
          # losing strat
          return -1 * (10 ** 40)

    rank = 0
    for line in self.lines:
      # Check who is on the line
      counts = self.getCounts(newBoard, line)

      if counts[0] + counts[1] == 0:
        rank = rank + 0
      elif counts[0] * counts[1] > 0:
        rank = rank + 0
      elif counts[0] > 0:
        rank = rank + self.cpuParams[counts[0]-1]
      elif counts[1] > 0:
        rank = rank - self.userParams[counts[1]-1]

    return rank


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

boardSize = 4

bestParams = [56734, 155558, 305346, 446075]
bestUserParams = [128521, 174904, 225807, 357475]

user = User()
cpu = AI(boardSize, 'Troll', user.getName(), bestParams, bestUserParams, lines)

# game = Game(cpu, user, lines)
game = Game(user, cpu, lines)
print game.play()

# Playing the machines against each other
# while True:
#   bar = random.randint(100, 1000000)
#   champ = AI(boardSize, 'Champ', 'Challenger', bestParams, bestUserParams, lines)
  
#   challengerParams = []
#   lastNum = 1
#   for i in xrange(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerParams.append(newNum)

#     lastNum = newNum

#   challengerUserParams = []
#   lastNum = 1
#   for i in xrange(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerUserParams.append(newNum)

#     lastNum = newNum

#   challenger = AI(boardSize, 'Challenger', 'Champ', challengerParams, challengerUserParams, lines)
  
#   print 'The Champ:', bestParams, bestUserParams
#   print 'The Challenger:', challengerParams, challengerUserParams

#   game = Game(champ, challenger, lines)

#   winner = game.play()

#   print 'Winner: ', winner
#   if winner == 'Challenger':
#     print 'New Champ!', winner
#     bestParams = challengerParams
#     bestUserParams = challengerUserParams

    