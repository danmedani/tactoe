import copy

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

  def move(self, board, boardSize):
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
    for line in self.lines:
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
      for line in self.lines:
        counts = self.getCounts(board, line)

        if counts[0] == 4:
          return (board, justMoved)
      
      # Check for forcing moves
      for line in self.lines:
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
      for line in self.lines:
        counts = self.getCounts(board, line)

        if counts[1] == 4:
          return (board, justMoved)

      # Check for possible winning moves for cpu
      for line in self.lines:
        counts = self.getCounts(board, line)

        if (counts[0] == 3) and (counts[1] == 0):
          for pos in line:
            if board[pos[0]][pos[1]][pos[2]] == None:
              tmpBoard = copy.deepcopy(board)
              tmpBoard[pos[0]][pos[1]][pos[2]] = self.cpuName

              return (tmpBoard, self.cpuName)
      
      # Check for forcing moves
      for line in self.lines:
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