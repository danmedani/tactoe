import copy
from logic.ai_v2 import convert_position
from logic.ai_v2 import convert_board
from logic.ai_v2 import is_valid_move
# from logic.ai_v2 import get_best_score
from logic.ai_v2 import get_best_result
from logic.ai_v2 import score_count
from logic.ai_v2 import score_board

MOCK_BOARD = [[[None for x in range(4)] for y in range(4)] for z in range(4)]

def test_convert_position_none():
	assert convert_position(None) is None

def test_convert_position_player():
	assert convert_position('Dan') == 0

def test_convert_position_cpu():
	assert convert_position('Mongo') == 1

def test_convert_board():
	test_board = copy.deepcopy(MOCK_BOARD)
	assert convert_board(test_board) == [[[None for x in range(4)] for y in range(4)] for z in range(4)]

def test_convert_board_2():
	test_board = copy.deepcopy(MOCK_BOARD)
	test_board[0][1][2] = 'Mongo'
	test_board[0][1][3] = 'Dan'
	result = convert_board(test_board)
	assert result[0][1][2] == 1
	assert result[0][1][3] == 0

def test_score_count_same():
	assert score_count((1, 1), 0) == 0

def test_score_count_same_2():
	assert score_count((2, 2), 1) == 0

def test_score_count_cpu_up():
	assert score_count((2, 0), 1) == -4

def test_score_count_cpu_up_two():
	assert score_count((2, 0), 0) == 4

def test_score_count_cpu_up_three():
	assert score_count((3, 0), 0) == 9

def test_score_count_cpu_up_four():
	assert score_count((4, 0), 0) == 10 ** 20

def test_score_count_cpu_up_four_other():
	assert score_count((4, 0), 1) == -10 ** 20

def test_score_board():
	test_board = copy.deepcopy(MOCK_BOARD)
	test_board[0][1][2] = 1
	test_board[0][1][3] = 0
	test_board[0][1][1] = 1
	assert score_board(test_board, 0) == -3


def test_score_board():
	test_board = copy.deepcopy(MOCK_BOARD)
	test_board[0][0][0] = 1
	test_board[3][2][3] = 1
	test_board[1][1][1] = 0
	test_board[1][2][1] = 0
	assert score_board(test_board, 0) == 5

def test_is_valid_move():
	test_board = copy.deepcopy(MOCK_BOARD)
	test_board[0][1][0] = 1
	test_board[3][2][3] = 1
	assert is_valid_move(test_board, [0, 0, 0])
	assert is_valid_move(test_board, [3, 3, 3])
	assert not is_valid_move(test_board, [0, 1, 0])
	assert not is_valid_move(test_board, [3, 2, 3])

# def test_get_best_score_zero():
# 	test_board = copy.deepcopy(MOCK_BOARD)
# 	assert get_best_score(test_board, 0, 0) == 0

# def test_get_best_score_one():
# 	test_board = copy.deepcopy(MOCK_BOARD)
# 	assert get_best_score(test_board, 0, 1) == 7

# def test_get_best_score_one():
# 	test_board = copy.deepcopy(MOCK_BOARD)
# 	assert get_best_score(test_board, 0, 2) == 3

def test_get_best_result():
	assert get_best_result()

