from consts import SOLDIER, MINE, FLAG,BOARD_ROWS,BOARD_COLUMNS,GROUND

def where_is_soldier(board):
    index_list=[]
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == SOLDIER:
                    index_list.append([row,col])
    return index_list
def can_soldier_move(board,letter):
    index_list=where_is_soldier(board)
    left_foot=index_list[0]
    right_foot=index_list[1]
    if letter=='a':
        if left_foot[1] != 0:
            return True

        return False
    if letter=='d':
        if right_foot[1] != BOARD_COLUMNS-1:
            return True
        return False
    if letter=='w':
        if right_foot[0]>3:
            return True
        return False
    if letter=='s':
        if left_foot[0] != BOARD_ROWS-1:
            return True
        return False

def move_soldier(board,letter):

    pos=where_is_soldier(board)
    left_foot=pos[0]
    right_foot=pos[1]
    possible_moves=[FLAG,SOLDIER,MINE,GROUND]
    if letter=='a':

        if board[left_foot[0]][left_foot[1]-1]==MINE:
            return False
        board[left_foot[0]][left_foot[1]-1]=SOLDIER
        board[right_foot[0]][right_foot[1]]=GROUND


    if letter=='s':

        if board[left_foot[0]+1][left_foot[1]]==FLAG or board[right_foot[0]+1][right_foot[1]]==FLAG:
            return True
        if board[left_foot[0]+1][left_foot[1]]==MINE or board[right_foot[0]+1][right_foot[1]]==MINE:
            return False

        board[left_foot[0]+1][left_foot[1]]=SOLDIER
        board[right_foot[0]+1][right_foot[1]]=SOLDIER
        board[left_foot[0]][left_foot[1]]=GROUND
        board[right_foot[0]][right_foot[1]]=GROUND

    # [3,0]
    # [3,1]
    if letter=='d':
         if board[right_foot[0]][right_foot[1]+1]==FLAG:
            return True

         if right_foot[1]+1!=BOARD_COLUMNS and board[right_foot[0]][right_foot[1]+1]==MINE:
             return False
         board[right_foot[0]][right_foot[1]+1]=SOLDIER
         board[left_foot[0]][left_foot[1]]=GROUND

    if letter=='w':

            if  board[left_foot[0]-1][left_foot[1]]==MINE and board[right_foot[0]-1][right_foot[1]]==MINE:
                return False

            board[left_foot[0]-1][left_foot[1]]=SOLDIER
            board[right_foot[0]-1][right_foot[1]]=SOLDIER
            board[left_foot[0]][left_foot[1]]=GROUND
            board[right_foot[0]][right_foot[1]]=GROUND













