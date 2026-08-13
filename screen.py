import pygame

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


running=True
from soldier import where_is_soldier,move_soldier

while running:
    screen.fill((90, 100, 49))

    soldier_location = where_is_soldier(board)

    screen.blit(soldier_img,(soldier_location[0][0],30))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            move_soldier("s")
        if event.type == pygame.K_RIGHT:
            move_soldier("d")
        if event.type == pygame.K_LEFT:
            move_soldier("a")
        if event.type == pygame.K_UP:
            move_soldier("w")
        pygame.display.flip()
pygame.quit()