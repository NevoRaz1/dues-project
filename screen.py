import time


import pygame
from soldier import where_is_soldier,move_soldier,can_soldier_move
from consts import WIDTH,HIGHT,BOARD_ROWS,BOARD_COLUMNS,MINE
import random
pygame.init()
# מילון למעקב אחר זמני לחיצה על מקשי ספרות
number_and_time = {}
from Database import add_game_to_save
# מיפוי מקשי הספרות (כולל Numpad) לערכים המספריים שלהם
NUMBER_KEYS = {
    pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3,
    pygame.K_4: 4, pygame.K_5: 5, pygame.K_6: 6,
    pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9,
    pygame.K_KP1: 1, pygame.K_KP2: 2, pygame.K_KP3: 3,
    pygame.K_KP4: 4, pygame.K_KP5: 5, pygame.K_KP6: 6,
    pygame.K_KP7: 7, pygame.K_KP8: 8, pygame.K_KP9: 9,
}
game_saves = {}
def save_game(current_board, slot_number,game_saves):
    game_saves[slot_number] = current_board




cell_size=WIDTH//BOARD_COLUMNS
#https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame

screen = pygame.display.set_mode((WIDTH,HIGHT))

from board import create_board
board = create_board()

#soldier image
soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (2*cell_size,4*cell_size))


mine_img = pygame.image.load("mine.png").convert_alpha()
mine_img = pygame.transform.scale(mine_img, (cell_size*3, cell_size))


grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (cell_size, cell_size))


flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (3*cell_size, 4*cell_size))


font = pygame.font.Font(None, 24)

lose_font = pygame.font.Font(None, 200)
lose_text = lose_font.render("You Lose!",True,(255,255,255))
win_text = lose_font.render("You Win!",True,(255,255,255))

def put_background(grass_list,grass_img,flag_img):


    screen.fill((90, 100, 49))
    screen.blit(flag_img, (46*cell_size, 21*cell_size))

    for grass in grass_list:
        screen.blit(grass_img,grass)


def show_xray(board, screen, soldier_img, soldier_x, soldier_y, mine_img, cell_size):
    screen.fill((0, 0, 0))

    for row in range(BOARD_ROWS + 1):
        pygame.draw.line(screen, (0, 100, 0), (0, row * cell_size), (WIDTH, row * cell_size))
    for col in range(BOARD_COLUMNS + 1):
        pygame.draw.line(screen, (0, 100, 0), (col * cell_size, 0), (col * cell_size, HIGHT))

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == MINE:
                if col == 0 or board[row][col -1] != MINE:# אם אנחנו בעמודה ה 0 אז פשוט מציירים ואם אנחנו הגענו לפצצה אז אנחנו בודקים עם היא שמאלית ביותר
                    mine_x = col * cell_size
                    mine_y = row * cell_size
                    screen.blit(mine_img, (mine_x, mine_y))#ומציירים רק את הפצצה השמאלית כי היא באורך של שלוש ולכן צריך רק את השמאלית

    screen.blit(soldier_img, (soldier_x, soldier_y))
    pygame.display.flip()



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

def run_game():
    text_massage=True
    running = True
    while running:

        soldier_x = where_is_soldier(board)[0][1] * cell_size
        soldier_y = (where_is_soldier(board)[0][0] - 3) * cell_size

        put_background(grass_list, grass_img, flag_img)
        screen.blit(soldier_img,(soldier_x,soldier_y))
        if text_massage == True:
            screen.blit(text, (70, 10))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if can_soldier_move(board,"s")==True:
                        do_win=move_soldier(board,"s")#פרמטר שמזיז את השחקן ולאחר מכן מקבל תשובה אם הוא ניצח
                        if do_win == False:
                            screen.blit(lose_text, (200, 200))
                            running = False
                            break
                        elif do_win == True:
                            screen.blit(win_text,(200,200))
                            running=False
                            break



                elif event.key == pygame.K_UP:
                    if can_soldier_move(board, "w") == True:
                        do_win = move_soldier(board, "w")
                        if do_win == False:
                            screen.blit(lose_text, (200, 200))
                            running = False
                            break
                        elif do_win == True:
                            screen.blit(win_text, (200,200))
                            running = False
                            break



                elif event.key == pygame.K_LEFT:
                    if can_soldier_move(board, "a") == True:
                        do_win = move_soldier(board, "a")
                        if do_win == False:
                            screen.blit(lose_text, (200, 200))
                            running = False
                            break
                        elif do_win == True:
                            screen.blit(win_text, (200, 200))
                            running = False
                            break




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



                elif event.key == pygame.K_RETURN:
                    show_xray(board, screen, soldier_img, soldier_x, soldier_y, mine_img, cell_size)
                    time.sleep(1)  # שניה
                    pygame.event.clear()#כל קליטה של כפתורים במהלך השניה ימחקו כי אסור לו לזוז
                text_massage=False

                if event.key in NUMBER_KEYS:  # האם הכפתור שנלחץ הוא מספר
                    number_and_time[event.key] = time.time()  # שמירת המספר והזמן שהוא נלחץ
            elif event.type == pygame.KEYUP:  # בודק האם המקש הורם
                if event.key in number_and_time.keys():
                    press_duration = time.time() - number_and_time[event.key]  # מחסר את הזמן העכשווי לזמן שהוא נלחץ
                    slot_number = list(number_and_time.keys())[0]
                    if press_duration <= 1.0:
                        save_game(board, slot_number,game_saves)
                        add_game_to_save(game_saves,slot_number)
                    number_and_time.clear()


        pygame.display.flip()





    for i in range(3000):
        pygame.display.flip()
