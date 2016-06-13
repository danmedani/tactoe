class Game:
  def __init__(self, p1, p2, lines):
    self.players = (p1, p2)

    self.boardSize = 4
    self.board = [[[None for x in xrange(self.boardSize)] for y in xrange(self.boardSize)] for z in xrange(self.boardSize)]

    self.lines = lines

    self.gameRecord = []

  def play(self):
    currentPlayer = 0
    # if random.random() < 0.5:
    #   currentPlayer = 1
    
    while True:
      moveRes = self.players[currentPlayer].move(self.board, self.boardSize)
      if moveRes[0] == None:
        self.gameRecord.append(0.5)
        return self.players[currentPlayer].getName(), self.formatGameRecord(-1)
      
      # print self.players[currentPlayer].getName(), 'moved here:', moveRes[0]
      self.board = moveRes[1]
      
      self.gameRecord.append(self.formatBoard())

      if self.isWinner():
        # print self.players[currentPlayer].getName() + ' has won!!! Good job!'
        return self.players[currentPlayer].getName(), self.formatGameRecord(currentPlayer)

      # Switch players
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

  def formatBoard(self):
    retVal = []
    for layer in self.board:
      for row in layer:
        for pos in row:
          if pos == None:
            retVal.append(0)
          elif pos == self.players[0].getName():
            retVal.append(1)
          else:
            retVal.append(-1)
    return retVal

  def formatGameRecord(self, winningPlayer):
    outputs = []
    player = 0
    for gameState in self.gameRecord:
      if winningPlayer == -1:
        outputs.append([0.5])
      elif winningPlayer == player:
        outputs.append([1])
      else:
        outputs.append([0])
      player = 1 - player
    
    return [self.gameRecord, outputs]
