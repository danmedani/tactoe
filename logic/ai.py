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

    possible_move_length = len(
      [
        move 
        for move in self.moveList 
        if board[move[0]][move[1]][move[2]] == None
      ]
    )
    depth_search = 2 \
      if possible_move_length > 61 else 3 if possible_move_length > 24 else 4 \
      if possible_move_length > 15 else 5 if possible_move_length > 8 else 6
    bestMoves, best_moves_rank = self.find_best_moves(
      board,
      depth_search,
      self.cpuName
    )
    print(bestMoves, best_moves_rank)

    if not bestMoves:
      print('Cat Game')
      return None, board
    moveToChoose = random.choice(bestMoves)
    board[moveToChoose[0]][moveToChoose[1]][moveToChoose[2]] = self.cpuName
    return moveToChoose, board

  def next_mover(self, current_mover):
    return self.cpuName if current_mover == self.opponentName else self.opponentName

  def find_best_moves(
    self,
    board,
    depth,
    mover
  ):
    if depth == 1:
      # find best ranking of possible moves
      best_move_rank = -1 * (10 ** 90)
      best_moves = []
      for move in self.moveList:
        if board[move[0]][move[1]][move[2]] == None:
          board[move[0]][move[1]][move[2]] = mover
          rank = self.getRank(board, mover)
          if rank == best_move_rank:
            best_moves.append(move)
          elif rank > best_move_rank:
            best_move_rank = rank
            best_moves = [move]
          board[move[0]][move[1]][move[2]] = None
      return best_moves, best_move_rank
    
    # find (wise) opponent's worst move
    worst_opponents_move_rank = 10 ** 90
    best_moves = []
    for move in self.moveList:
      if board[move[0]][move[1]][move[2]] == None:
        board[move[0]][move[1]][move[2]] = mover

        _, best_move_rank_for_opponent_after_this_move = self.find_best_moves(
          board,
          depth - 1,
          self.next_mover(mover)
        )
        if best_move_rank_for_opponent_after_this_move == worst_opponents_move_rank:
          best_moves.append(move)
        elif best_move_rank_for_opponent_after_this_move < worst_opponents_move_rank:
          worst_opponents_move_rank = best_move_rank_for_opponent_after_this_move
          best_moves = [move]
        board[move[0]][move[1]][move[2]] = None

    # print(best_moves, worst_opponents_move_rank)
    return best_moves, worst_opponents_move_rank


  def getCounts(self, board, line):
    userCount = 0
    cpuCount = 0

    for pos in line:
      if board[pos[0]][pos[1]][pos[2]] == self.opponentName:
        userCount = userCount + 1
      elif board[pos[0]][pos[1]][pos[2]] == self.cpuName:
        cpuCount = cpuCount + 1

    return (cpuCount, userCount)

  def getRank(self, theBoard, mover):
    rank = 0
    for line in self.lines:
      # Check who is on the line
      counts = self.getCounts(theBoard, line)

      if counts[0] + counts[1] == 0: # nobody here
        rank = rank + 0
      elif counts[0] * counts[1] > 0: # dead line
        rank = rank + 0
      else:
        if mover == 'Mongo':
          if counts[0] > 0:
            rank = rank + self.cpuParams[counts[0]-1]
          elif counts[1] > 0:
            rank = rank - self.userParams[counts[1]-1]
        else:
          if counts[1] > 0:
            rank = rank + self.cpuParams[counts[1]-1]
          elif counts[0] > 0:
            rank = rank - self.userParams[counts[0]-1]

    return rank
