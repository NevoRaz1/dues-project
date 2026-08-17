import pygame
from soldier import where_is_soldier, move_soldier, can_soldier_move
import time
import random
from board import create_board
from consts import MINE,WIDTH,HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


board = create_board()

ROWS = 25
COLS = 50

# גודל משבצת בפיקסלים
CELL_WIDTH = 640 / COLS   # 12.8
CELL_HEIGHT = 640 / ROWS  # 25.6

# מידות החייל במשבצות: 2 לרוחב (רגליים), 4 לגובה (גוף וראש)
SOLDIER_COLS = 2
SOLDIER_ROWS = 4

show_grid_until = 0

mine_img = pygame.image.load("mine.png").convert_alpha()

# טעינת התמונה וחיתוך שוליים שקופים למניעת חריגה מחוץ לגבולות המשבצת
raw_soldier_img = pygame.image.load("soldier.png").convert_alpha()
bounding_rect = raw_soldier_img.get_bounding_rect()
cropped_soldier_img = raw_soldier_img.subsurface(bounding_rect)

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (32, 32))

font = pygame.font.Font(None, 20)
lose_font = pygame.font.Font(None, 100)
lose_text = lose_font.render("You Lose!", True, (255, 255, 255))
win_text = lose_font.render("You Win!", True, (255, 255, 255))


def get_soldier_draw_data(board):
    """
    מחשבת את המיקום והגודל המדויק בפיקסלים שננעלים על קווי המשבצות של הגריד.
    """
    soldier_pos = where_is_soldier(board)
    if not soldier_pos:
        return None, (0, 0)

    feet_row = soldier_pos[0][0]
    left_col = min(p[1] for p in soldier_pos)

    # השורה העליונה שבה מתחילה תמונת החייל
    top_row = feet_row - (SOLDIER_ROWS - 1)

    # חישוב נקודות הקצה המדויקות לפי קווי הרשת
    x1 = int(left_col * CELL_WIDTH)
    y1 = int(top_row * CELL_HEIGHT)
    x2 = int((left_col + SOLDIER_COLS) * CELL_WIDTH)
    y2 = int((feet_row + 1) * CELL_HEIGHT)

    width = x2 - x1
    height = y2 - y1

    # התאמת התמונה בדיוק לגודל המשבצות
    scaled_img = pygame.transform.smoothscale(cropped_soldier_img, (width, height))
    return scaled_img, (x1, y1)


def draw_special_board(screen, board, soldier_img, soldier_pos):
    width = screen.get_width()
    height = screen.get_height()

    cell_width = width / COLS
    cell_height = height / ROWS

    screen.fill((0, 0, 0))

    # קווי הלוח
    for col in range(COLS + 1):
        x = int(col * cell_width)
        pygame.draw.line(screen, (0, 100, 0), (x, 0), (x, height), 3)
        pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, height), 1)

    for row in range(ROWS + 1):
        y = int(row * cell_height)
        pygame.draw.line(screen, (0, 100, 0), (0, y), (width, y), 3)
        pygame.draw.line(screen, (0, 255, 0), (0, y), (width, y), 1)

    # מוקשים
    for row in range(ROWS):
        col = 0
        while col < COLS:
            if board[row][col] == MINE:
                x = int(col * cell_width)
                y = int(row * cell_height)

                target_width = int(cell_width * 3)
                target_height = int(cell_height)

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


running = True

while running:

    # קבלת התמונה המותאמת והמיקום שננעל על הרשת
    current_soldier_img, soldier_pixel_pos = get_soldier_draw_data(board)

    if time.time() < show_grid_until:
        draw_special_board(screen, board, current_soldier_img, soldier_pixel_pos)
    else:
        screen.fill((90, 100, 49))
        if current_soldier_img:
            screen.blit(current_soldier_img, soldier_pixel_pos)

    text = font.render("Welcome to The Flag game.\n Have Fun!", True, (255, 255, 255))
    screen.blit(text, (70, 10))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                show_grid_until = time.time() + 1

            if event.key == pygame.K_DOWN:
                if can_soldier_move(board, "s") == True:
                    if move_soldier(board, "s") == False:
                        screen.blit(lose_text, (100, 100))
                        running = False

            elif event.key == pygame.K_UP:
                if can_soldier_move(board, "w") == True:
                    if move_soldier(board, "w") == False:
                        screen.blit(lose_text, (100, 100))
                        running = False

            elif event.key == pygame.K_LEFT:
                if can_soldier_move(board, "a") == True:
                    if move_soldier(board, "a") == False:
                        screen.blit(lose_text, (100, 100))
                        running = False

            elif event.key == pygame.K_RIGHT:
                if can_soldier_move(board, "d") == True:
                    if move_soldier(board, "d") == False:
                        screen.blit(lose_text, (100, 100))
                        running = False

    pygame.display.flip()

for i in range(1000):
    pygame.display.flip()

from colorama import Fore, Back, Style, init