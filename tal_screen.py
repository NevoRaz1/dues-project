import pygame
from soldier import where_is_soldier,move_soldier,can_soldier_move
from consts import WIDTH,HIGHT,BOARD_ROWS,BOARD_COLUMNS,MINE
import random

cell_size=WIDTH//BOARD_COLUMNS

screen = pygame.display.set_mode((WIDTH,HIGHT))

from board import create_board
board = create_board()


show_grid_until = 0
flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (3*cell_size, 4*cell_size))

mine_img = pygame.image.load("mine.png").convert_alpha()

soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (2*cell_size,4*cell_size))

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (cell_size, cell_size))

font = pygame.font.Font(None, 24)

lose_font = pygame.font.Font(None, 200)
lose_text = lose_font.render("You Lose!",True,(255,255,255))
win_text = lose_font.render("You Win!",True,(255,255,255))


def put_background(grass_list,grass_img,flag_img):


    screen.fill((90, 100, 49))
    screen.blit(flag_img, (46*cell_size, 21*cell_size))

    for grass in grass_list:
        screen.blit(grass_img,grass)


def draw_special_board(screen, board, soldier_img, soldier_pos):
    width = screen.get_width()
    height = screen.get_height()


    screen.fill((0, 0, 0))

    # קווי הלוח
    for col in range(BOARD_COLUMNS + 1):
        x = int(col * cell_size)
        pygame.draw.line(screen, (0, 100, 0), (x, 0), (x, height), 3)
        pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, height), 1)

    for row in range(BOARD_ROWS + 1):
        y = int(row * cell_size)
        pygame.draw.line(screen, (0, 100, 0), (0, y), (width, y), 3)
        pygame.draw.line(screen, (0, 255, 0), (0, y), (width, y), 1)

    # מוקשים
    for row in range(BOARD_ROWS):
        col = 0
        while col < BOARD_COLUMNS:
            if board[row][col] == MINE:
                x = int(col * cell_size)
                y = int(row * cell_size)

                target_width = int(cell_size * 3)
                target_height = int(cell_size)

                original_width = mine_img.get_width()
                original_height = mine_img.get_height()

                width_ratio = target_width / original_width
                height_ratio = target_height / original_height
                scale = min(width_ratio, height_ratio)

                mine_width = max(1, int(original_width * scale))
                mine_height = max(1, int(original_height * scale))

                scaled_mine = pygame.transform.scale(mine_img, (mine_width, mine_height))

                mine_x = x + (target_width - mine_width) // 2
                mine_y = y + (target_height - mine_height) // 2

                screen.blit(scaled_mine, (mine_x, mine_y))
                col += 3
            else:
                col += 1

    if soldier_img and soldier_pos:
        screen.blit(soldier_img, soldier_pos)

screen.fill((90, 100, 49))
text=font.render("Welcome to The Flag game.\n Have Fun!",True,(255,255,255))
screen.blit(text,(70,10))
screen.blit(flag_img,(46*cell_size,21*cell_size))
grass_list=[]
for i in range(20):
    x=random.randint(0, WIDTH)
    y=random.randint(0, HIGHT)
    grass_list.append((x,y))
put_background(grass_list,grass_img,flag_img)
soldier_x = where_is_soldier(board)[0][1]*cell_size
soldier_y=(where_is_soldier(board)[0][0]-3)*cell_size

running=True
while running:
    soldier_x = where_is_soldier(board)[0][1] * cell_size
    soldier_y = (where_is_soldier(board)[0][0] - 3) * cell_size

    put_background(grass_list, grass_img, flag_img)
    screen.blit(soldier_img,(soldier_x,soldier_y))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if can_soldier_move(board,"s")==True:
                    do_win=move_soldier(board,"s")
                    if do_win == False:
                        screen.blit(lose_text, (200, 200))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text,(200,200))
                        running=False
                        break
                for i in board:
                    print(i)
                print("\n \n \n \n ")


            elif event.key == pygame.K_UP:
                if can_soldier_move(board, "w") == True:
                    do_win = move_soldier(board, "w")
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (100, 100))
                        running = False
                        break

                for i in board:
                    print(i)
                print("\n \n \n \n ")

            elif event.key == pygame.K_LEFT:
                if can_soldier_move(board, "a") == True:
                    do_win = move_soldier(board, "a")
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (100, 100))
                        running = False
                        break

                for i in board:
                    print(i)
                print("\n \n \n \n ")


            elif event.key == pygame.K_RIGHT:
                if can_soldier_move(board, "d") == True:
                    do_win = move_soldier(board, "d")
                    if do_win == False:
                        screen.blit(lose_text, (200, 200))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (200, 200))
                        running = False
                        break

                for i in board:
                    print(i)
                print("\n \n \n \n ")


    pygame.display.flip()

for i in range(3000):
    pygame.display.flip()