from consts import SOLDIER, MINE
from board import board
def where_is_soldier(board):
    index_list=[]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLDIER:
                    index_list.append((row,col))
    return index_list


def player_is_lose():
    foot_list=where_is_soldier(board)
    for foot in foot_list:
        if board[foot[0]][foot[1]]==MINE :
            return True
    return False







def foot_index(row, column):
    index_list=[]
    index_list.append([row+3,column])
    index_list.append([row+3,column+1])
    return index_list
