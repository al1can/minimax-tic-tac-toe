import random

class TicTacToe:
    table = []
    human_player = ''
    ai_player = ''
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
        is_won = False
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
    def pick_side(self):
        while True:
            side = input("Pick the side you want to play as. X or O\n")
            if side in ('O', 'X'):
                self.human_player = side
                if side == 'X':
                    self.ai_player = 'O'
                else:
                    self.ai_player = 'X'
                break

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
        if self.is_player_won(table, self.human_player):
            return {'score': -10}
        elif self.is_player_won(table, self.ai_player):
            return {'score': 10}
        elif self.is_table_filled(table):
            return {'score': 0}
        moves = []
        for cell in self.available_cells(table):
            move = {}
            move['index'] = cell
            table[cell[1]][cell[0]] = player
            if player == self.ai_player:
                result = self.minimax(table, self.human_player)
                move['score'] = result['score']
            elif player == self.human_player:
                result = self.minimax(table, self.ai_player)
                move['score'] = result['score']
            table[cell[1]][cell[0]] = '-'
            moves.append(move)
        
        best_move = []
        if player == self.ai_player:
            best_score = -float("Inf")
            for move in moves:
                if move['score'] > best_score:
                    best_score = move['score']
                    best_move = move['index']
        elif player == self.human_player:
            best_score = float("Inf")
            for move in moves:
                if move['score'] < best_score:
                    best_score = move['score']
                    best_move = move['index']
        return {'index': best_move, 'score': best_score};

def main():
    # Create the class instance
    tic_tac_toe = TicTacToe()
    # Make user pick siXde
    tic_tac_toe.pick_side()
    # Game loop
    while True:
        # Print the table
        tic_tac_toe.print_table()
        # Swap players
        # player = tic_tac_toe.player_swap(player)
        # Player makes move
        tic_tac_toe.player_move(tic_tac_toe.human_player)
        # Check if player won
        if tic_tac_toe.is_player_won(tic_tac_toe.table, tic_tac_toe.human_player):
            tic_tac_toe.print_table()
            print(f"player {tic_tac_toe.human_player} is won!")
            break
        # Check if there is empty cells in the table
        if tic_tac_toe.is_table_filled(tic_tac_toe.table):
            tic_tac_toe.print_table()
            print("It is a draw!")
            break
        result = tic_tac_toe.minimax(tic_tac_toe.table, tic_tac_toe.ai_player)
        tic_tac_toe.table[result['index'][1]][result['index'][0]]=tic_tac_toe.ai_player
        # Check if player won
        if tic_tac_toe.is_player_won(tic_tac_toe.table, tic_tac_toe.ai_player):
            tic_tac_toe.print_table()
            print(f"player {tic_tac_toe.ai_player} is won!")
            break
        # Check if there is empty cells in the table
        if tic_tac_toe.is_table_filled(tic_tac_toe.table):
            tic_tac_toe.print_table()
            print("It is a draw!")
            break

if __name__ == '__main__':
    main()