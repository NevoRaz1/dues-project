from consts import SOLDIER, MINE, FLAG,BOARD_ROWS,BOARD_COLUMNS,GROUND

def where_is_soldier(board):
    index_list=[]
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == SOLDIER:
                    index_list.append([row,col])
    return index_list
def move_soldier(board,letter):
    pos=where_is_soldier(board)
    left_foot=pos[0]
    right_foot=pos[1]
    possible_moves=[FLAG,SOLDIER,MINE,GROUND]
    if letter=='a':
        if board[left_foot[1]] != 0:
            if board[left_foot[0]][left_foot[1]-1]==MINE:
                return False

            board[left_foot[0]][left_foot[1]-1]=SOLDIER
            board[right_foot[0]][right_foot[1]]=GROUND
        else:
            return 1

    if letter=='s':
        if left_foot[0] + 1 != BOARD_ROWS:
            if left_foot[0] + 1 != BOARD_ROWS:
                if board[left_foot[0]+1][left_foot[1]]==FLAG or board[right_foot[0]+1][right_foot[1]]==FLAG:
                    return True
                if board[left_foot[0]][left_foot[1]+1]==MINE or board[right_foot[0]][right_foot[1]+1]==MINE:
                    return False

                board[left_foot[0]+1][left_foot[1]]=SOLDIER
                board[right_foot[0]+1][right_foot[1]]=SOLDIER
                board[left_foot[0]][left_foot[1]]=GROUND
                board[right_foot[0]][right_foot[1]]=GROUND
            else:
                return 1

    # [3,0]
    # [3,1]
    if letter=='d':
        if right_foot[1] + 1 != BOARD_COLUMNS:
            if right_foot[1]+1!=BOARD_COLUMNS and board[right_foot[0]][right_foot[1]+1]==FLAG:
                return True

            if right_foot[1]+1!=BOARD_COLUMNS and board[right_foot[0]][right_foot[1]+1]==MINE:
                return False
            board[right_foot[0]][right_foot[1]+1]=SOLDIER
            board[left_foot[0]][left_foot[1]]=GROUND
        else:
            return 1#אי אפשר לזוז
    if letter=='w':
        if left_foot[0] > 3:
            if left_foot[0]>3 and board[left_foot[0]+1][left_foot[1]]==MINE and board[right_foot[0]+1][right_foot[1]]==MINE:
                return False
            if board[left_foot[0]-1][left_foot[1]] in possible_moves and board[right_foot[0]-1][right_foot[1]] in possible_moves:
                board[left_foot[0]-1][left_foot[1]]=SOLDIER
                board[right_foot[0]-1][right_foot[1]]=SOLDIER
                board[left_foot[0]][left_foot[1]]=GROUND
                board[right_foot[0]][right_foot[1]]=GROUND
    else:
        return 1











def foot_index(row, column):
    index_list=[]
    index_list.append([row+3,column])
    index_list.append([row+3,column+1])
    return index_list

