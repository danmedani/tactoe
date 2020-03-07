from logic.game_essentials import MOVE_LIST
from logic.game_essentials import LINES

CPU_NAME = 'Mongo'
MAX_SCORE = 10 ** 20

def convert_position(position):
  return None if position is None else (
    1 if position == CPU_NAME else 0
  )

def convert_board(board):
  """
  n  n  0  1
  1  0  n  1
  n  n  n  n
  1  n  0  0
  """
  return [[[convert_position(board[x][y][z]) for z in range(4)] for y in range(4)] for x in range(4)]

def getCounts(board, line, turn):
    my_turn_count = 0
    their_turn_count = 0

    for pos in line:
      if board[pos[0]][pos[1]][pos[2]] == turn:
        my_turn_count = my_turn_count + 1
      elif board[pos[0]][pos[1]][pos[2]] == 1 - turn:
        their_turn_count = their_turn_count + 1

    return (my_turn_count, their_turn_count)

def score_count(counts, turn):
  if counts[turn] > 0 and counts[1 - turn] > 0:
    # moot line
    return 0
  
  if counts[turn] == 4:
    # turn won
    return MAX_SCORE
  
  if counts[1 - turn] == 4:
    # turn lost
    return -1 * MAX_SCORE
  
  return (counts[turn] ** 2) - (counts[1 - turn] ** 2)

def is_valid_move(board, move):
  return board[move[0]][move[1]][move[2]] is None

def score_board(board, turn):
  score = 0
  for line in LINES:
    score += score_count(
      getCounts(board, line, turn), 
      turn
    )
  return score


# def get_best_score(
#   board,
#   turn,
#   depth
# ):
#   current_score = score_board(board, turn)
#   if current_score > 10 ** 10:
#     return current_score

#   if current_score > 10 ** 10:
#     return current_score
#   if depth == 0:
#     return current_score
  
#   max_score = -1 * MAX_SCORE
#   valid_moves = [move for move in MOVE_LIST if is_valid_move(board, move)]
#   for move in valid_moves:
#     board[move[0]][move[1]][move[2]] = turn
#     score = get_best_score(
#       board,
#       1 - turn,
#       depth - 1
#     )
#     if score > max_score:
#       max_score = score
    
#     board[move[0]][move[1]][move[2]] = None
  
#   return max_score

# def best_move(board, turn, depth):
#   best_move = None
#   best_score = -1 * MAX_SCORE
  
#   valid_moves = [move for move in MOVE_LIST if is_valid_move(converted_board, move)]
#   for move in valid_moves:
#     board[move[0]][move[1]][move[2]] = turn

#     board[move[0]][move[1]][move[2]] = None

def get_best_result(board, turn, depth):
  score = score_board(board, turn)
  # if we won, or are tired looking...
  if depth == 0 or score > 10 ** 10:
    return score
  
  best_result = -1 * MAX_SCORE
  for move in [move for move in MOVE_LIST if is_valid_move(board, move)]:
    # move here
    board[move[0]][move[1]][move[2]] = turn

    opponent_best_outcome = get_best_result(board, 1 - turn, depth - 1)
    best_outcome = opponent_best_outcome * -1

    if best_outcome > best_result:
      best_result = best_outcome
    
    # unmove
    board[move[0]][move[1]][move[2]] = None

  return best_result

def move(board):
  converted_board = convert_board(board)
  best_move = None
  best_score = -10 * MAX_SCORE

  for move in [move for move in MOVE_LIST if is_valid_move(converted_board, move)]:
    # cpu moves here
    converted_board[move[0]][move[1]][move[2]] = 1
    opponent_best_outcome = get_best_result(converted_board, 0, 2)
    best_outcome = opponent_best_outcome * -1

    if best_outcome > best_score:
      best_score = best_outcome
      best_move = move
    
    converted_board[move[0]][move[1]][move[2]] = None
  
  board[best_move[0]][best_move[1]][best_move[2]] = CPU_NAME
  return best_move, board

class AIV2:
  def getName(self):
    return CPU_NAME

  def move(self, board):
    return move(board)
