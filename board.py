import random
import consts
from consts import BOARD_ROWS,BOARD_COLUMNS,GROUND,MINE
matrix=[]
for row in range(0, 25):
    matrix.append([])
    for column in range(0, 50):
        matrix[row].append(GROUND)
def put_grass_in_board(matrix):#
    grasses=[]
    for i in range(20):
        row = random.randint(0, 24)
        col = random.randint(0, 49)
        while (row,col) in grasses:
            row = random.randint(0, 24)
            col = random.randint(0, 49)
        grasses.append((row,col))

def put_mines_in_board(matrix):
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
            matrix[mine_first_square[0]][mine_first_square[1]]=MINE
put_mines_in_board(matrix)
for i in matrix:
    print(i)

