from consts import GUARD, GUARD_ROW, BOARD_COLUMNS, GROUND, MINE, SOLDIER


def where_guard_col(board):
    for col in range(len(board[GUARD_ROW])):
        if board[GUARD_ROW][col]==GUARD:
            return col

def move_guard_right(board):
    guard_col=where_guard_col(board)
    if guard_col<BOARD_COLUMNS-1 :
        if board[GUARD_ROW][guard_col+1]==SOLDIER:
            return True

    if guard_col<BOARD_COLUMNS-1 :
        if  board[GUARD_ROW][guard_col+1]==GROUND:
            board[GUARD_ROW][guard_col+1]=GUARD
            board[GUARD_ROW][guard_col]=GROUND
        elif board[GUARD_ROW][guard_col+1]==MINE:
            count=0
            i=0
            while i <=3:
                if count==0:
                    board[GUARD_ROW][guard_col + 1] = GUARD
                    board[GUARD_ROW][guard_col] = GROUND
                elif count==1 or count == 2 :
                    board[GUARD_ROW][guard_col + 1] = GUARD
                    board[GUARD_ROW][guard_col] = MINE

                elif count==3:
                    if board[GUARD_ROW][guard_col+1]==GROUND:
                        board[GUARD_ROW][guard_col+1]=GUARD
                        board[GUARD_ROW][guard_col]=MINE
                    elif board[GUARD_ROW][guard_col+1]==MINE:
                        i=0
                        count=0
                        continue
                i +=1
                count+=1

def move_guard_left(board):
    guard_col = where_guard_col(board)
    if guard_col>0 :
        if board[GUARD_ROW][guard_col-1]==SOLDIER:
            return True

    if guard_col >0:
        if board[GUARD_ROW][guard_col - 1] == GROUND:
            board[GUARD_ROW][guard_col - 1] = GUARD
            board[GUARD_ROW][guard_col] = GROUND
        elif board[GUARD_ROW][guard_col - 1] == MINE:
            count = 0
            i = 0
            while i <= 3:
                if count == 0:
                    board[GUARD_ROW][guard_col -1] = GUARD
                    board[GUARD_ROW][guard_col] = GROUND
                elif count == 1 or count == 2:
                    board[GUARD_ROW][guard_col - 1] = GUARD
                    board[GUARD_ROW][guard_col] = MINE

                elif count == 3:
                    if board[GUARD_ROW][guard_col - 1] == GROUND:
                        board[GUARD_ROW][guard_col - 1] = GUARD
                        board[GUARD_ROW][guard_col] = MINE
                    elif board[GUARD_ROW][guard_col - 1] == MINE:
                        i = 0
                        count = 0
                        continue
                i += 1
                count += 1






