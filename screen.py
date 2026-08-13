import pygame
import time
from soldier import where_is_soldier,move_soldier

pygame.init()

screen = pygame.display.set_mode((640,640))

from board import create_board
board = create_board()

#soldier image
soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(soldier_img, (64,64))

#put 20 grasses
import random
grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (32,32))
screen.blit(grass_img, (random.randint(0, 100), 30))




font = pygame.font.Font(None, 20)

soldier_x = where_is_soldier(board)[0][0]
soldier_y=30
running=True
while running:

    # time.sleep(0.5)
    screen.fill((90, 100, 49))

    text=font.render("Welcome to The Flag game.\n Have Fun!",True,(255,255,255))
    screen.blit(text,(70,10))


    screen.blit(soldier_img,(soldier_x,soldier_y))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_soldier("s")
                soldier_y+=22.8
            elif event.key == pygame.K_UP:
                move_soldier("w")
                soldier_y-=22.8
            elif event.key == pygame.K_LEFT:
                move_soldier("a")
                soldier_x-=11.4
            elif event.key == pygame.K_RIGHT:
                move_soldier("d")
                soldier_x+=11.4

    pygame.display.flip()


pygame.quit()
