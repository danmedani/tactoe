import time
import copy
from logic.game_essentials import LINES
from logic.ai_v2 import CPU_NAME
from logic.ai import AI

MOCK_BOARD = [[[None for x in range(4)] for y in range(4)] for z in range(4)]

def test_find_best_moves():
    boardSize = 4
    bestParams = [1, 4, 20, 10**10]
    bestUserParams = [1, 4, 20, 10**10]

    cpu = AI(boardSize, CPU_NAME, 'Dave', bestParams, bestUserParams, LINES)

    test_board = copy.deepcopy(MOCK_BOARD)
    test_board[0][0][0] = 'Dave'
    test_board[0][0][1] = 'Mongo'
    test_board[0][0][2] = 'Dave'
    test_board[0][0][3] = 'Mongo'
    test_board[0][1][0] = 'Dave'
    test_board[0][1][1] = 'Mongo'
    test_board[0][1][2] = 'Dave'
    test_board[0][1][3] = 'Mongo'
    test_board[0][2][0] = 'Dave'
    test_board[0][2][1] = 'Mongo'
    test_board[0][2][2] = 'Dave'
    test_board[0][2][3] = 'Mongo'
    test_board[0][3][0] = 'Mongo'
    test_board[0][3][1] = 'Dave'
    test_board[0][3][2] = 'Mongo'
    test_board[0][3][3] = 'Dave'

    test_board[1][0][0] = 'Dave'
    test_board[1][0][1] = 'Mongo'
    test_board[1][0][2] = 'Dave'
    test_board[1][0][3] = 'Mongo'
    test_board[1][1][0] = 'Dave'
    test_board[1][1][1] = 'Mongo'
    test_board[1][1][2] = 'Dave'
    test_board[1][1][3] = 'Mongo'
    test_board[1][2][0] = 'Dave'
    test_board[1][2][1] = 'Mongo'
    test_board[1][2][2] = 'Dave'
    test_board[1][2][3] = 'Mongo'
    test_board[1][3][0] = 'Mongo'
    test_board[1][3][1] = 'Dave'
    test_board[1][3][2] = 'Mongo'
    test_board[1][3][3] = 'Dave'

    test_board[2][0][0] = 'Dave'
    test_board[2][0][1] = 'Mongo'
    test_board[2][0][2] = 'Dave'
    test_board[2][0][3] = 'Mongo'
    test_board[2][1][0] = 'Dave'
    test_board[2][1][1] = 'Mongo'
    test_board[2][1][2] = 'Dave'
    test_board[2][1][3] = 'Mongo'
    test_board[2][2][0] = 'Dave'
    test_board[2][2][1] = 'Mongo'
    test_board[2][2][2] = 'Dave'
    test_board[2][2][3] = 'Mongo'
    test_board[2][3][0] = 'Mongo'
    test_board[2][3][1] = 'Dave'
    test_board[2][3][2] = 'Mongo'
    test_board[2][3][3] = 'Dave'
    start_time = time.time()
    cpu.find_best_moves(
        test_board,
        5,
        CPU_NAME
    )
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    assert elapsed_time == 30
    