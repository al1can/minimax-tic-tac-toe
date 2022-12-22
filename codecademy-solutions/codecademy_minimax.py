from codecademy_tic_tac_toe import *
from copy import deepcopy

def game_is_over(board):
    return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def evaluate_board(board):
    if has_won(board, "X"):
        return 1
    elif has_won(board, "O"):
        return -1
    else:
        return 0

new_game = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

x_winning = [
	["X", "2", "O"],
	["4", "O", "6"],
	["7", "8", "X"]
]

o_winning = [
	["X", "X", "O"],
	["4", "X", "6"],
	["7", "O", "O"]
]

def minimax(input_board, is_maximizing):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board):
        return [evaluate_board(input_board), ""]
    best_move = ""
    if is_maximizing == True:
        best_value = -float("Inf")
        symbol = "X"
    else:
        best_value = float("Inf")
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        hypothetical_value = minimax(new_board, not is_maximizing)[0]
        if is_maximizing == True and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
        if is_maximizing == False and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
    return [best_value, best_move]

new_game = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

#print(minimax(x_winning, True))
#print(minimax(o_winning, True))
#print(minimax(new_game, False))

while not game_is_over(new_game):
    select_space(new_game, minimax(new_game, True)[1], "X")
    if not game_is_over(new_game):
        select_space(new_game, minimax(new_game, False)[1], "O")
    print_board(new_game)  