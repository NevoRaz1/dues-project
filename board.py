import random
from consts import BOARD_ROWS, BOARD_COLUMNS, GROUND, MINE, FLAG, SOLDIER


def create_board():
    board = []
    for row in range(BOARD_ROWS):
        board.append([])
        for column in range(BOARD_COLUMNS):
            board[row].append(GROUND)
    add_soldier(board)
    put_flag(board)
    put_mines_in_board(board)
    while not is_board_ok(board):
        board = create_board()
        add_soldier(board)
        put_flag(board)
        put_mines_in_board(board)
    return board


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
    row = random.randint(0, BOARD_ROWS - 1)  # roll random number between 0-len-3 because the mine length is 3
    col = random.randint(0, BOARD_COLUMNS - 3)
    while board[row][col] == SOLDIER or board[row][col + 1] == SOLDIER or board[row][col + 2] == SOLDIER or board[row][
        col] == FLAG or board[row][col + 1] == FLAG or board[row][col + 2] == FLAG:
        row = random.randint(0, BOARD_ROWS - 3)
        col = random.randint(0, BOARD_COLUMNS - 3)
    mine = [(row, col), (row, col + 1), (row, col + 2)]
    mines.append(mine)
    for i in range(19):  # run 20 times for 20 mines
        row = random.randint(0, BOARD_ROWS - 1)  # roll random number between 0-len-3 because the mine length is 3
        col = random.randint(0, BOARD_COLUMNS - 3)
        # checks edge cases
        while is_mine_exist(mines, row, col) or board[row][col] == SOLDIER or board[row][col + 1] == SOLDIER or \
                board[row][col + 2] == SOLDIER or board[row][col] == FLAG or board[row][col + 1] == FLAG or board[row][
            col + 2] == FLAG:
            row = random.randint(0, BOARD_ROWS - 3)
            col = random.randint(0, BOARD_COLUMNS - 3)
        mine = [(row, col), (row, col + 1), (row, col + 2)]
        mines.append(mine)
        # mines=לרשימה שיש בה רשימות[[(),(),()],[(),(),()],[(),(),()],[(),(),()]]
    # mine=[(),(),()]
    # mine_square=()
    for mine in mines:  # פה שמים את הפצצות בלוח
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





# ===== תוספת בלבד =====
import pygame


def draw_board_image(board):
    pygame.init()

    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("The Flag Game")

    cell_width = 640 / BOARD_COLUMNS
    cell_height = 640 / BOARD_ROWS

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for row in range(BOARD_ROWS):
            for column in range(BOARD_COLUMNS):

                x = int(column * cell_width)
                y = int(row * cell_height)

                if board[row][column] == MINE:
                    pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        (x + 2, y + 2, int(cell_width) - 4, int(cell_height) - 4)
                    )

        for column in range(BOARD_COLUMNS + 1):
            x = int(column * cell_width)

            pygame.draw.line(
                screen,
                (0, 100, 0),
                (x, 0),
                (x, 640),
                3
            )

            pygame.draw.line(
                screen,
                (0, 255, 0),
                (x, 0),
                (x, 640),
                1
            )

        for row in range(BOARD_ROWS + 1):
            y = int(row * cell_height)

            pygame.draw.line(
                screen,
                (0, 100, 0),
                (0, y),
                (640, y),
                3
            )

            pygame.draw.line(
                screen,
                (0, 255, 0),
                (0, y),
                (640, y),
                1
            )

        pygame.display.flip()

    pygame.quit()

# ===== סוף התוספת =====