# run.py

from tic_tac_toe import TicTacToe

def main():
    tic_tac_toe = TicTacToe()

    while True:
        tic_tac_toe.greeting()
        tic_tac_toe.create_board()

        player = 'X' if tic_tac_toe.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                tic_tac_toe.show_board()
                print(f'\nPlayer {player} turn')

                coordinates = tic_tac_toe.user_input(player)

                if coordinates is None:
                    game_over = True
                    break

                row, col = map(int, coordinates)
                print()

                tic_tac_toe.validate_coordinates(row, col)

                tic_tac_toe.fix_spot(row - 1, col - 1, player)

                if tic_tac_toe.has_player_won(player):
                    game_over = True
                    print(f'Player {player} wins the game!')
                elif tic_tac_toe.is_board_filled():
                    game_over = True
                    print('Match Draw!')
                else:
                    player = tic_tac_toe.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        tic_tac_toe.show_board()

        # Add this line to display the menu after the game is over
        if not tic_tac_toe.menu():
            break  # Exit the outer loop if the player chooses to exit

if __name__ == '__main__':
    main()
