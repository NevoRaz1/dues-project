import random
from consts import BOARD_ROWS, BOARD_COLUMNS, GROUND, MINE, FLAG, SOLDIER, GUARD_ROW, GUARD, TELEPORT
from teleport import create_teleport


def create_board():
    board = []
    for row in range(BOARD_ROWS):
        board.append([])
        for column in range(BOARD_COLUMNS):
            board[row].append(GROUND)

    add_guard(board)
    add_soldier(board)
    put_flag(board)
    create_teleport(board)
    put_mines_in_board(board)

    while not is_board_ok(board):
        board = []
        for row in range(BOARD_ROWS):
            board.append([])
            for column in range(BOARD_COLUMNS):
                board[row].append(GROUND)
        add_guard(board)
        add_soldier(board)
        put_flag(board)
        create_teleport(board)
        put_mines_in_board(board)
    return board


def add_guard(board):
    board[GUARD_ROW][0] = GUARD


def add_soldier(board):
    board[3][1], board[3][0] = SOLDIER, SOLDIER


def put_flag(board):
    for row in range(22, BOARD_ROWS):
        for column in range(46, BOARD_COLUMNS):
            board[row][column] = FLAG


def is_mine_exist(mines, row, col):
    for mine in range(len(mines)):
        if mines[mine][0] == (row, col) or (row, col) == mines[mine][1] or (row, col) == mines[mine][2]:
            return True
    return False


def put_mines_in_board(board):
    mines = []
    for i in range(20):
        row = random.randint(0, BOARD_ROWS - 1)
        col = random.randint(0, BOARD_COLUMNS - 3)

        while (board[row][col] in [SOLDIER, GUARD, FLAG, TELEPORT] or
               board[row][col + 1] in [SOLDIER, FLAG, TELEPORT] or
               board[row][col + 2] in [SOLDIER, FLAG, TELEPORT] or
               is_mine_exist(mines, row, col)):
            row = random.randint(0, BOARD_ROWS - 3)
            col = random.randint(0, BOARD_COLUMNS - 3)

        mine = [(row, col), (row, col + 1), (row, col + 2)]
        mines.append(mine)

    for mine in mines:
        for mine_square in mine:
            board[mine_square[0]][mine_square[1]] = MINE


def is_board_ok(board, row=2, col=0):
    if board[row][col] == FLAG or board[row][col + 1] == FLAG:
        return True
    if col + 2 < BOARD_COLUMNS and board[row][col + 2] != MINE:
        if is_board_ok(board, row, col + 1):
            return True
    if row + 1 < BOARD_ROWS and board[row + 1][col] != MINE and board[row + 1][col + 1] != MINE:
        if is_board_ok(board, row + 1, col):
            return True
    return False