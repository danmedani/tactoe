from logic.game_essentials import MOVE_LIST
from logic.game_essentials import LINES

CPU_NAME = 'Mongo'
MAX_SCORE = 10 ** 20

def move(board):
  converted_board = convert_board(board)
  best_move = None
  best_score = -10 * MAX_SCORE


class AIV2:
  def getName(self):
    return CPU_NAME

  def move(self, board):
    return move(board)
