from consts import SOLDIER, BOARD_ROWS, MINE
from board import board
def where_is_soldier(board):
    index_list=[]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLDIER:
                    index_list.append([row,col])
    return index_list




def create_soldier():
    new_player=[]
    for row in range(4):
        new_player.append([])
        for column in range(2):
            new_player[row].append(SOLDIER)

def player_is_lose():
    foot_list=[]
    index_list=where_is_soldier(board)
    row=index_list[0][0]
    column=index_list[0][1]
    foot_list=foot_index(row,column)
    row1=foot_list[0][0]
    column1=foot_list[0][1]
    row2=foot_list[1][0]
    column2=foot_list[1][1]
    if board[row1][column1]==MINE or board[row2][column2]==MINE:
        return True
    return False







def foot_index(row, column):
    index_list=[]
    index_list.append([row+3,column])
    index_list.append([row+3,column+1])
    return index_list
