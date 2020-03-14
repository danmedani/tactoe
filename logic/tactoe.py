# 3D tic tac toe AI, Dave

import sys
import copy
import random
from logic.game import Game
from logic.user import User
from logic.ai import AI
from logic.ai_v2 import AIV2
from logic.game_essentials import LINES
from logic.ai_v2 import CPU_NAME

boardSize = 4
# bestParams = [1, 4, 20, 10**10]
# bestUserParams = [1, 4, 20, 10**10]

bestParams = [10, 31, 80, 10**10]
bestUserParams = [10, 31, 80, 10**10]

user = User()
cpu = AI(boardSize, CPU_NAME, user.getName(), bestParams, bestUserParams, LINES)
game = Game(user, cpu)
game.play()

# Playing the machines against each other
# while True:
# #   bar = random.randint(100, 1000000)
#   champ = AI(boardSize, 'Champ', 'Challenger', bestParams, bestUserParams, LINES)
  
#   challengerParams = []
#   lastNum = 1
#   first_param = random.randint(1, 10)
#   second_param = random.randint(first_param, 100)
#   third_param = random.randint(second_param, 1000)

#   challengerUserParams = [first_param, second_param, third_param, 10 ** 10]
# #   print(challengerUserParams)

#   challenger = AI(boardSize, 'Challenger', 'Champ', challengerUserParams, challengerUserParams, LINES)
  
# #   print 'The Champ:', bestParams, bestUserParams
# #   print 'The Challenger:', challengerParams, challengerUserParams

#   game = Game(champ, challenger)

#   winner, record = game.play()

# #   print 'Winner: ', winner
# #   print record
#   if winner == 'Challenger':
#     print('New Champ!', winner, challengerUserParams)
#     bestParams = challengerUserParams
#     bestUserParams = challengerUserParams
    