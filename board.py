import random
from consts import BOARD_ROWS,BOARD_COLUMNS,GROUND,MINE,FLAG
def create_board():
    board=[]
    for row in range(BOARD_ROWS):
        board.append([])
        for column in range(BOARD_COLUMNS):
            board[row].append(GROUND)
    return board

def put_flag(board):
    for row in range(22,BOARD_ROWS):
        for column in range(46,BOARD_COLUMNS):
            board[row][column]=FLAG
def put_mines_in_board(board):
    mines=[]
    row = random.randint(0, BOARD_ROWS)  # roll random number between 0-len-3 because the mine length is 3
    col = random.randint(0, BOARD_COLUMNS - 3)
    mine = [(row, col), (row, col + 1), (row, col + 2)]
    mines.append(mine)
    for i in range(19):#run 20 times for 20 mines
        row=random.randint(0,BOARD_ROWS-1)#roll random number between 0-len-3 because the mine length is 3
        col=random.randint(0,BOARD_COLUMNS-3)
        while (row,col) in mines[i] and (row,col+1) in mines[i] and (row,col+2) in mines[i] and board[row][col]==FLAG and board[row][col+1]==FLAG and board[row][col+2]==FLAG :
            row = random.randint(0, BOARD_ROWS - 3)
            col = random.randint(0, BOARD_COLUMNS - 3)
        mine=[(row,col),(row,col+1),(row,col+2)]
        mines.append(mine)
    #mines=לרשימה שיש בה רשימות[[(),(),()],[(),(),()],[(),(),()],[(),(),()]]
    #mine=[(),(),()]
    #mine_square=()
    for mine in mines:#פה שמים את הפצצות בלוח
        for mine_square in mine:
            board[mine_square[0]][mine_square[1]]=MINE
board=create_board()
put_flag(board)
put_mines_in_board(board)



for i in board:
    print(i)
