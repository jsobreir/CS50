"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

class InvalidMoveError(Exception):
    """Exception raised for an invalid move in the Tic-Tac-Toe game."""
    def __init__(self, message="Invalid move. Please try again."):
        self.message = message
        super().__init__(self.message)

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns the player who has the next turn on the board.
    """
    num_X = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)

    return O if num_X > num_O else X

def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	actions_set = set()
	for i in range(3):
		for j in range(3):
			if board[i][j] == EMPTY:
				actions_set.add((i, j))
	return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise InvalidMoveError
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
			return board[i][0]
		if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
			return board[0][i]
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
		return board[0][2]
	else:
		return None
			


def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	if winner(board) != None:
		return True
	if all(board[i][j] != EMPTY for i in range(len(board)) for j in range(len(board))):
		return True
	return False


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if winner(board) == X:
		return 1
	elif winner(board) == O:
		return -1
	else:
		return 0

def max_value(board):
    if terminal(board):
        return utility(board), None  # Return utility value and no action

    v = -10
    best_action = None
    for action in actions(board):
        min_v, _ = min_value(result(board, action))  # Extract only the value
        if min_v > v:  # Correct comparison
            v = min_v
            best_action = action
    return v, best_action  # Return both value and action

def min_value(board):
    if terminal(board):
        return utility(board), None  # Return utility value and no action

    v = 10
    best_action = None
    for action in actions(board):
        max_v, _ = max_value(result(board, action))  # Extract only the value
        if max_v < v:  # Correct comparison
            v = max_v
            best_action = action
    return v, best_action  # Return both value and action


def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	if terminal(board):
		return None
	if player(board) == X:
		return max_value(board)[1]
	elif player(board) == O:
		return min_value(board)[1]

