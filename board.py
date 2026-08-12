import random
from consts import BOARD_ROWS,BOARD_COLUMNS,GROUND,MINE,FLAG
board=[]
for row in range(0,BOARD_ROWS-1):
    board.append([])
    for column in range(0,BOARD_COLUMNS-1):
        board[row].append(GROUND)

def put_mines_in_board(board):
    mines=[]
    for i in range(20):#run 20 times for 20 mines
        row=random.randint(0,BOARD_ROWS-3)#roll random number between 0-len-3 because the mine length is 3
        col=random.randint(0,BOARD_COLUMNS-3)
        while (row,col) in mines and (row,col+1) in mines and (row,col+2) in mines:
            row = random.randint(0, BOARD_ROWS - 3)
            col = random.randint(0, BOARD_COLUMNS - 3)
        mine=[(row,col),(row,col+1),(row,col+2)]
        mines.append(mine)

    for mine in mines:#פה שמים את הפצצות בלוח
        for mine_first_square in mine:
            board[mine_first_square[0]][mine_first_square[1]]=MINE
put_mines_in_board(board)


def put_flag(board):
    for row in range(21,BOARD_ROWS-1):
        for column in range(45,BOARD_COLUMNS-1):
            board[row][column]=FLAG
put_flag(board)
for i in board:
    print(i)
