import random
from copy import deepcopy

class TicTacToe:
    table = []
    # Constuctor
    def __init__(self):
        self.create_table()
    # Create the table
    def create_table(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.table.append(row)
    # Check if there any other empty spot on table
    def is_table_filled(self, table):
        is_filled = True
        for row in table:
            for element in row:
                if element=='-':
                    is_filled = False
        return is_filled
    # Check if given player won
    def is_player_won(self, table, player):
        is_won = None
        size = len(table)
        # Checking if all points in horizontal line from same player
        for row in range(size):
            is_won = True
            for element in range(size):
                if table[row][element]!=player:
                    is_won = False
                    break
            if is_won:return is_won
        # Checking if all points in vertical line from same player
        for row in range(size):
            is_won = True
            for element in range(size):
                if table[element][row]!=player:
                    is_won = False
                    break
            if is_won:return is_won
        # Checking if all points in diagonal line to right is from same player
        # As in
        # X _ _
        # _ X _
        # _ _ X
        for element in range(size):
            is_won = True
            if table[element][element]!=player:
                is_won = False
                break
        if is_won:return is_won
        # Checking if all points in diagonal line to right is from same player
        # As in
        # _ _ X
        # _ X _
        # X _ _
        for element in range(size):
            is_won = True
            if table[element][size - 1 - element]!=player:
                is_won = False
                break
        if is_won:return is_won

        return is_won
    # Print the table
    def print_table(self):
        for i, row in enumerate(self.table):
            print(" ", end="")
            print(*row,sep=" | ")
            if i!=2: print('---+---+---') 
    # Pick a random player
    def random_player(self):
        player = random.choice(['X','O'])
        return player
    # Make player move
    def player_move(self,player):
        print(f"Now it is {player}'s turn.")
        # Check if input is acceptable
        while True:
            # Check if enough input is given
            while True:
                try:
                    # First input is x and second is y
                    col,row = list(map(int, input().split()))
                    break
                except ValueError:
                    print("Wrong type of input!\nYou need to enter integer values in the order x and y separated with a single space.")
            # To get inputs between these values so the user doesnt need to enter 0
            if (row in (1, 2, 3)) and (col in (1, 2, 3)):
                # The way matrix works is to keep row lists that keeps x lists
                # Thats way we access the cell as in table[row][col]
                if self.table[row-1][col-1]=='-':
                    self.table[row-1][col-1] = player
                    break
                else:
                    print("This place is not available. Try again different spot!")
            else:
                print("The input needs to be between 1 and 3")
    # Swap the players
    def player_swap(self,player):
        return 'X' if player=='O' else 'O'
    # Return available cells
    def available_cells(self, table):
        available_cells = []
        for y, row in enumerate(table):
            for x, col in enumerate(row):
                if col == '-':
                    available_cells.append([x, y])
        return available_cells

    # Minimax
    def minimax(self, table, player):
        if self.is_player_won(table, 'X'):
            return [10]
        elif self.is_player_won(table, 'O'):
            return [-10]
        elif self.is_table_filled(table):
            return [0]

        human_player = 'O'
        ai_player = 'X'

        if player == ai_player:
            best_value = -float("Inf")
        else:
            best_value = float("Inf")
        for cell in self.available_cells(table):
            new_table = deepcopy(table)
            new_table[cell[1]][cell[0]] = player

            if player == ai_player:                
                score = self.minimax(new_table, human_player)[0]
            elif player == human_player:
                score = self.minimax(new_table, ai_player)[0]

            if player == ai_player and score > best_value:
                best_value = score
                best_move = cell
            elif player == human_player and score < best_value:
                best_value = score
                best_move = cell
        return [best_value, best_move]

def main():
    # Create the class instance
    tic_tac_toe = TicTacToe()
    # Pick a random player
    #player = tic_tac_toe.random_player()
    player = 'X'
    # Game loop
    while True:
        # Print the table
        tic_tac_toe.print_table()
        # Swap players
        # player = tic_tac_toe.player_swap(player)
        # Player makes move
        tic_tac_toe.player_move(player)

        tic_tac_toe.minimax(tic_tac_toe.table)

        # Check if there is a win
        if tic_tac_toe.is_player_won(player, tic_tac_toe.table):
            # Print the final version of table
            tic_tac_toe.print_table()
            print(f"player {player} is won!")
            break
        # Check if there is empty cells in the table
        if tic_tac_toe.is_table_filled(tic_tac_toe.table):
            # Print the final version of table
            tic_tac_toe.print_table()
            print("It is a draw!")
            break

if __name__ == '__main__':
    #main()
    tic_tac_toe = TicTacToe()
    player = 'X'
    x_winning = [
	["X", "-", "O"],
	["-", "O", "-"],
	["-", "-", "X"]
    ]
    o_winning = [
	["X", "X", "O"],
	["-", "X", "-"],
	["-", "O", "O"]
    ]
    result = tic_tac_toe.minimax(x_winning, player)
    print(result)
    result = tic_tac_toe.minimax(o_winning, player)
    print(result)
    #table = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
    #result = tic_tac_toe.is_table_filled(table)
    #print(result)