from consts import SOLDIER, MINE, FLAG, BOARD_ROWS, BOARD_COLUMNS, GROUND

def where_is_soldier(board):
    """מחזיר את רשימת המשבצות [row, col] שבהן ממוקם החייל"""
    index_list = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == SOLDIER:
                index_list.append([row, col])
    return index_list

def can_soldier_move(board, letter):
    """בודק אם החייל יכול לזוז מבחינת גבולות הלוח"""
    pos = where_is_soldier(board)
    if len(pos) < 2:
        return False

    left_foot = pos[0]
    right_foot = pos[1]

    if letter == 'a':
        return left_foot[1] > 0
    elif letter == 'd':
        return right_foot[1] < BOARD_COLUMNS - 1
    elif letter == 'w':
        return left_foot[0] > 0
    elif letter == 's':
        return left_foot[0] < BOARD_ROWS - 1

    return False

def is_mine(board, row, col):
    """
    בודק בדק דיוק אם המשבצת הספציפית [row, col] היא חלק ממוקש.
    מונע פסילה שגויה במדרכה נקייה ליד מוקש.
    """
    if row < 0 or row >= BOARD_ROWS or col < 0 or col >= BOARD_COLUMNS:
        return False

    # 1. בדיקה ישירה אם המשבצת עצמה מוגדרת כמוקש
    if board[row][col] == MINE:
        return True

    # 2. בדיקה אם המשבצת משמאל היא תחילתו של מוקש (משבצת 2 של מוקש רחב)
    if col - 1 >= 0 and board[row][col - 1] == MINE:
        if col - 2 < 0 or board[row][col - 2] != MINE:
            return True

    # 3. בדיקה אם המשבצת שתי משבצות משמאל היא תחילתו של מוקש (משבצת 3 של מוקש רחב)
    if col - 2 >= 0 and board[row][col - 2] == MINE:
        if col - 3 < 0 or board[row][col - 3] != MINE:
            return True

    return False

def move_soldier(board, letter):
    """
    מזיז את החייל במטריצה.
    מחזיר False רק אם החייל באמת דרך על מוקש, אחרת True.
    """
    pos = where_is_soldier(board)
    if len(pos) < 2:
        return True

    left_foot = pos[0]   # [row, col_left]
    right_foot = pos[1]  # [row, col_right]

    row = left_foot[0]
    c_left = left_foot[1]
    c_right = right_foot[1]

    if letter == 'a':
        new_col = c_left - 1
        if is_mine(board, row, new_col):
            return False

        board[row][new_col] = SOLDIER
        board[row][c_right] = GROUND

    elif letter == 'd':
        new_col = c_right + 1
        if is_mine(board, row, new_col):
            return False

        board[row][new_col] = SOLDIER
        board[row][c_left] = GROUND

    elif letter == 'w':
        new_row = row - 1
        if is_mine(board, new_row, c_left) or is_mine(board, new_row, c_right):
            return False

        board[new_row][c_left] = SOLDIER
        board[new_row][c_right] = SOLDIER
        board[row][c_left] = GROUND
        board[row][c_right] = GROUND

    elif letter == 's':
        new_row = row + 1
        if is_mine(board, new_row, c_left) or is_mine(board, new_row, c_right):
            return False

        board[new_row][c_left] = SOLDIER
        board[new_row][c_right] = SOLDIER
        board[row][c_left] = GROUND
        board[row][c_right] = GROUND

    return True