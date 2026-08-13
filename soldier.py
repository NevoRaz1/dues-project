from consts import SOLDIER, MINE, FLAG,BOARD_ROWS,BOARD_COLUMNS,GROUND
from board import create_board
board = create_board()
def where_is_soldier(board):
    index_list=[]
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == SOLDIER:
                    index_list.append([row,col])
    return index_list
def move_soldier(letter):
    pos=where_is_soldier(board)
    current_index1=pos[0]
    current_index2=pos[1]
    possible_moves=[FLAG,SOLDIER,MINE,GROUND]
    if letter=='a':
        if board[current_index1[1]]!=0 and board[current_index1[0]][current_index1[1]-1]==MINE:
            return False
        if board[current_index1[1]]!=0:
            board[current_index1[0]][current_index1[1]-1]=SOLDIER
            board[current_index2[0]][current_index2[1]]=GROUND

    if letter=='s':
        if current_index1[0] + 1 != BOARD_ROWS:
            if board[current_index1[0]+1][current_index1[1]]==FLAG or board[current_index2[0]+1][current_index2[1]]==FLAG:
                return True
            if board[current_index1[0]][current_index1[1]+1]==MINE or board[current_index2[0]][current_index2[1]+1]==MINE:
                return False

            if current_index1[0]+1!=BOARD_ROWS:
                board[current_index1[0]+1][current_index1[1]]=SOLDIER
                board[current_index2[0]+1][current_index2[1]]=SOLDIER
                board[current_index1[0]][current_index1[1]]=GROUND
                board[current_index2[0]][current_index2[1]]=GROUND





    if letter=='d':
        if board[current_index2[0]][current_index2[1]+1]==FLAG:
            if current_index2[1]+1!=BOARD_COLUMNS and board[current_index2[0]][current_index2[1]+1]==FLAG:
                return True
        if board[current_index2[0]][current_index2[1]+1]==MINE:
            return False
        if current_index2[1]+1!=BOARD_COLUMNS:
            board[current_index2[0]][current_index2[1]+1]=SOLDIER
            board[current_index1[0]][current_index1[1]]=GROUND

    if letter=='w':
        if board[current_index1[0]+1][current_index1[1]]==MINE:
            if current_index1[0]>3 and board[current_index1[0]+1][current_index1[1]]==MINE:
                    return False
        if current_index1[0]>3:
            if board[current_index1[0]-1][current_index1[1]] in possible_moves and board[current_index2[0]-1][current_index2[1]] in possible_moves:
                board[current_index1[0]-1][current_index1[1]]=SOLDIER
                board[current_index2[0]-1][current_index2[1]]=SOLDIER
                board[current_index1[0]][current_index1[1]]=GROUND
                board[current_index2[0]][current_index2[1]]=GROUND










def foot_index(row, column):
    index_list=[]
    index_list.append([row+3,column])
    index_list.append([row+3,column+1])
    return index_list

