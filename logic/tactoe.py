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
bestParams = [375250, 561784, 713811, 954648]
bestUserParams = [322324, 485781, 555105, 783246]

user = User()
cpu = AI(boardSize, CPU_NAME, user.getName(), bestParams, bestUserParams, LINES)
cpu = AIV2()
game = Game(user, cpu)
game.play()

# Playing the machines against each other
# while True:
#   bar = random.randint(100, 1000000)
#   champ = AI(boardSize, 'Champ', 'Challenger', bestParams, bestUserParams, LINES)
  
#   challengerParams = []
#   lastNum = 1
#   for i in range(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerParams.append(newNum)

#     lastNum = newNum

#   challengerUserParams = []
#   lastNum = 1
#   for i in range(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerUserParams.append(newNum)

#     lastNum = newNum

#   challenger = AI(boardSize, 'Challenger', 'Champ', challengerParams, challengerUserParams, LINES)
  
#   # print 'The Champ:', bestParams, bestUserParams
#   # print 'The Challenger:', challengerParams, challengerUserParams

#   game = Game(champ, challenger, LINES)

#   winner, record = game.play()

#   # print 'Winner: ', winner
#   print record
#   if winner == 'Challenger':
#     # print 'New Champ!', winner
#     bestParams = challengerParams
#     bestUserParams = challengerUserParams

#     