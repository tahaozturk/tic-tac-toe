import random

class TicTacToe:
    size = 3

    def __init__(self):
        self.board = []

    def greeting(self):
        print("""
        Welcome to the Tic-Tac-Toe Game!

        To make your move, enter the row and column coordinates separated by a comma.
        For example, to place your symbol in the first row and second column, type: 1,2.

        The game continues until a player wins or the board is filled.
        You can exit the game at any time by pressing 'q'.

        Let the games begin!
        """)

    def menu(self):
        while True:
            print("""
            1. Play again
            2. Exit
            """)

            choice = input("Enter choice: ")

            if choice == "1":
                print("\nThe game is starting again...")
                return True
            elif choice == "2":
                print("\nExiting the game...")
                return False
            else:
                print("Wrong choice, please try again.")

    def create_board(self):
        self.board = []
        for i in range(self.size):
            row = ['-'] * self.size
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def row_victory(self, player):
        for i in range(self.size):
            row_win = all(cell == player for cell in self.board[i])
            if row_win:
                return True
        return False

    def column_victory(self, player):
        for i in range(self.size):
            col_win = all(row[i] == player for row in self.board)
            if col_win:
                return True
        return False

    def diagonal_victory(self, player):
        main_diag_win = all(self.board[i][i] == player for i in range(self.size))
        anti_diag_win = all(self.board[i][self.size - 1 - i] == player for i in range(self.size))
        return main_diag_win or anti_diag_win

    def has_player_won(self, player):
        return self.row_victory(player) or self.column_victory(player) or self.diagonal_victory(player)

    def is_board_filled(self):
        return all(cell != '-' for row in self.board for cell in row)

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def user_input(self, player):
        coordinates = input('Enter row & column numbers to fix spot: ').split(",")

        if "q" in coordinates or "Q" in coordinates:
            print(f'Player {player} resigned! Quitting the game...')
            return None

        else:
            return coordinates

    def validate_coordinates(self, row, col):
        if row is None or col is None:
            raise ValueError('Not enough values to unpack (expected 2, got 1)')

        elif row > 3 or row < 1 or col < 1 or col > 3:
            raise ValueError('Out of board range. Please enter numbers between 1-3')

        elif self.board[row - 1][col - 1] != "-":
            raise ValueError('This coordinate is not available! Please choose another space')

        else:
            return True
