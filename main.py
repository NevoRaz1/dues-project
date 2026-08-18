from board import create_board
from screen import run_game
from teleport import create_teleport

board = create_board()

create_teleport(board)

run_game(board)