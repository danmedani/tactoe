class User:
  def __init__(self):
    self.userName = input('Enter Name: ')

  def getName(self):
    return self.userName

  def move(self, board):
    move = get_user_move(board)
    print('User Moved: ', move)
    
    board[move[0]][move[1]][move[2]] = self.userName
    return (move[0],move[1],move[2]), board

def get_user_move(board):
  userInput = input('Please enter position (space separated) x y z: ')
  try:
      move = [int(a) for a in userInput.split(' ')]
  except ValueError:
    print('Bad input')
    return get_user_move(board)

  if len(move) != 3:
    print('3 coordinates required')
    return get_user_move(board)

  if len([coord for coord in move if coord < 0 or coord > 3]) > 0:
    print('coords need to be between 0 and 3, inclusive')
    return get_user_move(board)

  if board[move[0]][move[1]][move[2]] != None:
    print(board[move[0]][move[1]][move[2]] + ' already has a stone here. Try again')
    return get_user_move(board)

  return move
