class Game:
  def __init__(self, p1, p2, lines):
    self.players = (p1, p2)

    self.boardSize = 4
    self.board = [[[None for x in xrange(self.boardSize)] for y in xrange(self.boardSize)] for z in xrange(self.boardSize)]

    self.lines = lines

  def play(self):
    currentPlayer = 0
    # if random.random() < 0.5:
    #   currentPlayer = 1
    
    while True:
      moveRes = self.players[currentPlayer].move(self.board, self.boardSize)
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