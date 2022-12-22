from copy import deepcopy

def print_board(board):
    print("|-------------|")
    print("| Tic Tac Toe |")
    print("|-------------|")
    print("|             |")
    print("|    " + board[0][0] + " " + board[0][1] + " " + board[0][2] + "    |")
    print("|    " + board[1][0] + " " + board[1][1] + " " + board[1][2] + "    |")
    print("|    " + board[2][0] + " " + board[2][1] + " " + board[2][2] + "    |")
    print("|             |")
    print("|-------------|")
    print()

def select_space(board, move, turn):
    if move not in range(1,10):
        return False
    row = int((move-1)/3)
    col = (move-1)%3
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        return False

def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves

def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

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

def minimax(input_board, player):
    human_player = 'O'
    ai_player = 'X'
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board):
        return [evaluate_board(input_board), ""]
    best_move = ""
    if player == ai_player:
        best_value = -float("Inf")
    else:
        best_value = float("Inf")
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, player)
        if player == ai_player:
            hypothetical_value = minimax(new_board, human_player)[0]
        else:
            hypothetical_value = minimax(new_board, ai_player)[0]
        if player == ai_player and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
        if player == human_player and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
  #print([best_value, best_move])
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
    move = int(input("move: "))
    select_space(new_game, move, "X")
    #select_space(new_game, minimax(new_game, "X")[1], "X")
    if not game_is_over(new_game):
        select_space(new_game, minimax(new_game, "O")[1], "O")
    print_board(new_game)  