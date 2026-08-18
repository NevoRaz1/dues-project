from consts import (
    BOARD_COLUMNS,
    BOARD_ROWS,
    FLAG,
    GROUND,
    MINE,
    SOLDIER,
    TELEPORT,
)
from teleport import get_teleport_list, is_on_teleport, where_send


def where_is_soldier(board):
    for row in range(BOARD_ROWS - 1, -1, -1):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == SOLDIER:
                return [(row, col), (row, col + 1)]
    return [(3, 0), (3, 1)]


def can_soldier_move(board, direction):
    legs = where_is_soldier(board)
    bottom_row, left_col = legs[0]
    top_row = bottom_row - 3
    right_col = legs[1][1]

    if direction == "w" and top_row > 0:
        return True
    if direction == "s" and bottom_row < BOARD_ROWS - 1:
        return True
    if direction == "a" and left_col > 0:
        return True
    if direction == "d" and right_col < BOARD_COLUMNS - 1:
        return True
    return False


def set_soldier_position(board, bottom_row, left_col):
    for r in range(bottom_row - 3, bottom_row + 1):
        board[r][left_col] = SOLDIER
        board[r][left_col + 1] = SOLDIER


def clear_soldier(board):
    """מוחק את החייל ומחזיר טלפורטים אם החייל עמד עליהם."""
    teleport_cells = set()
    for t_row, t_col in get_teleport_list():
        teleport_cells.add((t_row, t_col))
        teleport_cells.add((t_row, t_col + 1))
        teleport_cells.add((t_row, t_col + 2))

    for r in range(BOARD_ROWS):
        for c in range(BOARD_COLUMNS):
            if board[r][c] == SOLDIER:
                if (r, c) in teleport_cells:
                    board[r][c] = TELEPORT
                else:
                    board[r][c] = GROUND


def move_soldier(board, direction):
    legs = where_is_soldier(board)
    bottom_row, left_col = legs[0]

    next_bottom = bottom_row
    next_left = left_col

    if direction == "w":
        next_bottom -= 1
    elif direction == "s":
        next_bottom += 1
    elif direction == "a":
        next_left -= 1
    elif direction == "d":
        next_left += 1

    next_right = next_left + 1

    # 1. בדיקת מוקש
    if (
        board[next_bottom][next_left] == MINE
        or board[next_bottom][next_right] == MINE
    ):
        clear_soldier(board)
        set_soldier_position(board, next_bottom, next_left)
        return False

    # 2. בדיקת דגל
    if (
        board[next_bottom][next_left] == FLAG
        or board[next_bottom][next_right] == FLAG
    ):
        clear_soldier(board)
        set_soldier_position(board, next_bottom, next_left)
        return True

    # 3. בדיקת דריכה על טלפורט
    current_teleport = is_on_teleport(next_bottom, next_left)
    if current_teleport is not None:
        dest = where_send(current_teleport)
        if dest is not None:
            landing_row, landing_col = dest
            clear_soldier(board)
            set_soldier_position(board, landing_row, landing_col)
            return None

    # 4. תנועה רגילה
    clear_soldier(board)
    set_soldier_position(board, next_bottom, next_left)
    return None