import random
from consts import BOARD_ROWS,BOARD_COLUMNS,GROUND,MINE,FLAG
board=[]
for row in range(BOARD_ROWS):
    board.append([])
    for column in range(BOARD_COLUMNS):
        board[row].append(GROUND)
print(len(board))

def put_mines_in_board(board):
    mines=[]
    for i in range(20):#run 20 times for 20 mines
        row=random.randint(0,BOARD_ROWS-3)#roll random number between 0-len-3 because the mine length is 3
        col=random.randint(0,BOARD_COLUMNS-3)
        while (row,col) in mines and (row,col+1) in mines and (row,col+2) in mines and board[row][col]==FLAG and board[row][col+1]==FLAG and board[row][col+2]==FLAG :
            row = random.randint(0, BOARD_ROWS - 3)
            col = random.randint(0, BOARD_COLUMNS - 3)
        mine=[(row,col),(row,col+1),(row,col+2)]
        mines.append(mine)

    for mine in mines:#פה שמים את הפצצות בלוח
        for mine_first_square in mine:
            board[mine_first_square[0]][mine_first_square[1]]=MINE
put_mines_in_board(board)
for i in board:
    print(i)

