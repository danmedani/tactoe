# 3D tic tac toe AI, Dave

import sys
import copy
import random
from .game import Game
from .user import User
from .ai import AI
from .gameEssentials import GameEssentials

boardSize = 4
bestParams = [375250, 561784, 713811, 954648]
bestUserParams = [322324, 485781, 555105, 783246]

user = User()
cpu = AI(boardSize, 'Mongo', user.getName(), bestParams, bestUserParams, GameEssentials.lines)

# game = Game(cpu, user, lines)
game = Game(user, cpu, GameEssentials.lines)
print game.play()

# Playing the machines against each other
# while True:
#   bar = random.randint(100, 1000000)
#   champ = AI(boardSize, 'Champ', 'Challenger', bestParams, bestUserParams, lines)
  
#   challengerParams = []
#   lastNum = 1
#   for i in xrange(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerParams.append(newNum)

#     lastNum = newNum

#   challengerUserParams = []
#   lastNum = 1
#   for i in xrange(4):
#     newNum = random.randint(lastNum, lastNum + bar)
#     challengerUserParams.append(newNum)

#     lastNum = newNum

#   challenger = AI(boardSize, 'Challenger', 'Champ', challengerParams, challengerUserParams, lines)
  
#   print 'The Champ:', bestParams, bestUserParams
#   print 'The Challenger:', challengerParams, challengerUserParams

#   game = Game(champ, challenger, lines)

#   winner = game.play()

#   print 'Winner: ', winner
#   if winner == 'Challenger':
#     print 'New Champ!', winner
#     bestParams = challengerParams
#     bestUserParams = challengerUserParams

#     