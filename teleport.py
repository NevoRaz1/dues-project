from pathlib import Path
import random
from consts import BOARD_COLUMNS, GROUND, TELEPORT
import pygame

# רשימת המיקומים של הטלפורטים
_teleport_list = []


def get_teleport_list():
    """מחזיר את רשימת הטלפורטים המעודכנת תמיד."""
    return _teleport_list


def get_teleport_image(cell_size):
    img = pygame.image.load("teleport.png").convert_alpha()
    return pygame.transform.scale(img, (3 * cell_size, cell_size))


def create_teleport(board):
    """יוצר 5 טלפורטים בשורות 4-20 במטריצה ושומר ברשימה."""
    _teleport_list.clear()
    teleports_placed = 0

    while teleports_placed < 5:
        row = random.randint(4, 20)
        col = random.randint(0, BOARD_COLUMNS - 3)

        if ( board[row][col] == GROUND and board[row][col + 1] == GROUND and board[row][col + 2] == GROUND):
            board[row][col] = TELEPORT
            board[row][col + 1] = TELEPORT
            board[row][col + 2] = TELEPORT

            _teleport_list.append((row, col))
            teleports_placed += 1


def is_on_teleport(bottom_row, left_col):
    """בדיקה האם רגלי החייל נוגעות באחת מ-3 המשבצות של טלפורט."""
    right_col = left_col + 1
    for t_row, t_col in _teleport_list:
        if bottom_row == t_row:
            teleport_cols = [t_col, t_col + 1, t_col + 2]
            if left_col in teleport_cols or right_col in teleport_cols:
                return (t_row, t_col)
    return None


def where_send(current_teleport):

    target = random.choice(_teleport_list)

    while target == current_teleport:
        target = random.choice(_teleport_list)

    return (target[0] - 1, target[1])