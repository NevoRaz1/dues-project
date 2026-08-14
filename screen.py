import pygame
from soldier import where_is_soldier,move_soldier,can_soldier_move
import random
from board import create_board
from consts import WINDOW_HEIGHT,WINDOW_WIDTH,WHITE,BLACK
board = create_board()


https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame

def xrray(board):


xrray(board)





pygame.init()

screen = pygame.display.set_mode((640,640))



#soldier image
soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (64,64))

#put 20 grasses


grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (32, 32))


flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (50, 50))


font = pygame.font.Font(None, 20)

lose_font = pygame.font.Font(None, 100)
lose_text = lose_font.render("You Lose!",True,(255,255,255))
win_text = lose_font.render("You Win!",True,(255,255,255))

def put_background(grass_list,grass_img,flag_img):


    screen.fill((90, 100, 49))
    screen.blit(flag_img, (525, 525))

    for grass in grass_list:
        screen.blit(grass_img,grass)





screen.fill((90, 100, 49))
text=font.render("Welcome to The Flag game.\n Have Fun!",True,(255,255,255))
screen.blit(text,(70,10))
screen.blit(flag_img,(575,575))
grass_list=[]
for i in range(20):
    x=random.randint(0, 575)
    y=random.randint(0, 575)
    grass_list.append((x,y))
put_background(grass_list,grass_img,flag_img)
soldier_x = where_is_soldier(board)[0][0]
soldier_y=30
running=True
while running:

    # time.sleep(0.5)




    screen.blit(soldier_img,(soldier_x,soldier_y))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if can_soldier_move(board,"s")==True:
                    do_win = move_soldier(board, 's')  # עבור שני בדיקות אם ניצחון או הפסד מבלי להזיז פעמיים
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (100, 100))
                        running = False
                        break
                    soldier_y+=22.8
                for i in board:
                    print(i)
                print("\n \n \n \n ")
                put_background(grass_list,grass_img,flag_img)


            elif event.key == pygame.K_UP:
                if can_soldier_move(board, "w") == True:
                    do_win = move_soldier(board, 'w')  # עבור שני בדיקות אם ניצחון או הפסד מבלי להזיז פעמיים
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (100, 100))
                        running = False
                        break
                    soldier_y-=22.8
                for i in board:
                    print(i)
                print("\n \n \n \n ")
                put_background(grass_list,grass_img,flag_img)

            elif event.key == pygame.K_LEFT:
                if can_soldier_move(board, "a") == True:
                    do_win = move_soldier(board, 'a')  # עבור שני בדיקות אם ניצחון או הפסד מבלי להזיז פעמיים
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (100, 100))
                        running = False
                        break
                    soldier_x-=11.4
                for i in board:
                    print(i)
                print("\n \n \n \n ")
                put_background(grass_list,grass_img,flag_img)


            elif event.key == pygame.K_RIGHT:
                if can_soldier_move(board, "d") == True:
                    do_win =move_soldier(board,'d')#עבור שני בדיקות אם ניצחון או הפסד מבלי להזיז פעמיים
                    if do_win == False:
                        screen.blit(lose_text, (100, 100))
                        running = False
                        break
                    elif do_win ==True:
                        screen.blit(win_text,(100,100))
                        running = False
                        break
                    soldier_x+=11.4
                for i in board:
                    print(i)
                print("\n \n \n \n ")
                put_background(grass_list,grass_img,flag_img)


    pygame.display.flip()





for i in range(1000):
    pygame.display.flip()






