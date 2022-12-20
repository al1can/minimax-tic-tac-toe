import random

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
    def is_table_filled(self):
        is_filled = True
        for row in self.table:
            for element in row:
                if element=='-':
                    is_filled = False
        return is_filled
    # Check if given player won
    def is_player_won(self,player):
        is_won = None
        size = len(self.table)
        # Checking if all points in horizontal line from same player
        for row in range(size):
            is_won = True
            for element in range(size):
                if self.table[row][element]!=player:
                    is_won = False
                    break
            if is_won:return is_won
        # Checking if all points in vertical line from same player
        for row in range(size):
            is_won = True
            for element in range(size):
                if self.table[element][row]!=player:
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
            if self.table[element][element]!=player:
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
            if self.table[element][size - 1 - element]!=player:
                is_won = False
                break
        if is_won:return is_won

        return is_won
    # Print table
    def print_table(self):
        for row in self.table:
            for element in row:
                print(f"{element} ",end="")
            print("\n")
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
    # Return available spots
    def avail_spots(self):
        avail_spots = []
        for row in self.table:
            for col in self.table:
                avail_spots.append([row, col])

def main():
    # Create the class instance
    tic_tac_toe = TicTacToe()
    # Pick a random player
    player = tic_tac_toe.random_player()
    # Game loop
    while True:
        # Print the table
        tic_tac_toe.print_table()
        # Swap players
        player = tic_tac_toe.player_swap(player)
        # Player makes move
        tic_tac_toe.player_move(player)
        # Check if there is a win
        if tic_tac_toe.is_player_won(player):
            print(f"player {player} is won!")
            break
        # Check if there is empty cells in the table
        if tic_tac_toe.is_table_filled():
            print("It is a draw!")
            break
    # Print the table last time to show the completed table
    tic_tac_toe.print_table()

if __name__ == '__main__':
    main()