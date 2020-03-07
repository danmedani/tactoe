import random
import copy

class AI:
  def __init__(self, boardSize, cpuName, opponentName, cpuParams, userParams, lines):
    self.cpuName = cpuName
    self.opponentName = opponentName
    self.cpuParams = cpuParams
    self.userParams = userParams
    self.lines = lines
    
    self.moveList = []
    for a in range(boardSize):
      for b in range(boardSize):
        for c in range(boardSize):
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

            board[pos[0]][pos[1]][pos[2]] = self.cpuName
            return pos, board

    # Are we forced to move?
    for line in self.lines:
      counts = self.getCounts(board, line)
    
      if (counts[0] == 0) and (counts[1] == 3):
        for pos in line:
          if board[pos[0]][pos[1]][pos[2]] == None:
            board[pos[0]][pos[1]][pos[2]] = self.cpuName
            return pos, board

    # No forced moves... Let's look for a good one
    moveFound = False
    goodMoves = []
    for move in self.moveList:
      if board[move[0]][move[1]][move[2]] == None:
        moveFound = True
        board[move[0]][move[1]][move[2]] = self.cpuName

        potentialRank = self.getRank(board)

        if potentialRank > highestRanked:
          highestRanked = potentialRank
          goodMoves = [move]
        elif potentialRank == highestRanked:
          goodMoves.append(move)
        
        board[move[0]][move[1]][move[2]] = None

    if not moveFound:
      print('Cat Game')
      return None, board

    moveToChoose = random.choice(goodMoves)
    board[moveToChoose[0]][moveToChoose[1]][moveToChoose[2]] = self.cpuName
    return moveToChoose, board


  def getCounts(self, board, line):
    userCount = 0
    cpuCount = 0

    for pos in line:
      if board[pos[0]][pos[1]][pos[2]] == self.opponentName:
        userCount = userCount + 1
      elif board[pos[0]][pos[1]][pos[2]] == self.cpuName:
        cpuCount = cpuCount + 1

    return (cpuCount, userCount)

  # Higher rank == better for Mongo
  def getRank(self, theBoard):
    rank = 0
    for line in self.lines:
      # Check who is on the line
      counts = self.getCounts(theBoard, line)

      if counts[0] + counts[1] == 0: # nobody here
        rank = rank + 0
      elif counts[0] * counts[1] > 0: # dead line
        rank = rank + 0
      elif counts[0] > 0:
        rank = rank + self.cpuParams[counts[0]-1]
      elif counts[1] > 0:
        rank = rank - self.userParams[counts[1]-1]

    return rank
