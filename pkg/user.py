class User:
  def __init__(self):
    self.userName = raw_input('Enter Name: ')

  def getName(self):
    return self.userName

  def move(self, board, boardSize):
    userInput = raw_input('Please enter position (space separated) x y z: ')
    i = [int(a) for a in userInput.split(' ')]
    if (len(i) == 3) and (i[0] >= 0) and (i[0] < boardSize) and (i[1] >= 0) and (i[1] < boardSize) and (i[2] >= 0) and (i[2] < boardSize):
      if board[i[0]][i[1]][i[2]] != None:
        print 'Can not move here bro. ' + board[i[0]][i[1]][i[2]] + ' has a stone here.'
      else:
        # print 'User Moved: ', i
        board[i[0]][i[1]][i[2]] = self.userName
        return (i[0],i[1],i[2]), board