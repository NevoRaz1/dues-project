import pygame
import time
import random
from soldier import where_is_soldier, move_soldier, can_soldier_move
from board import create_board
from consts import MINE, WIDTH, HIGHT, BOARD_ROWS, BOARD_COLUMNS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HIGHT))
board = create_board()

ROWS = BOARD_ROWS
COLS = BOARD_COLUMNS

# חישוב גודל משבצת מדויק לפי הגדרות המסך והלוח
CELL_WIDTH = WIDTH / COLS
CELL_HEIGHT = HIGHT / ROWS

# מידות החייל במשבצות: 2 לרוחב (רגליים), 4 לגובה (גוף וראש)
SOLDIER_COLS = 2
SOLDIER_ROWS = 4

show_grid_until = 0

# טעינת תמונות
mine_img = pygame.image.load("mine.png").convert_alpha()

# טעינת החייל וחיתוך שוליים שקופים לנעלת מיקום מדויקת
raw_soldier_img = pygame.image.load("soldier.png").convert_alpha()
bounding_rect = raw_soldier_img.get_bounding_rect()
cropped_soldier_img = raw_soldier_img.subsurface(bounding_rect)

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (int(CELL_WIDTH), int(CELL_HEIGHT)))

flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (int(3 * CELL_WIDTH), int(4 * CELL_HEIGHT)))

# גופנים וטקסטים
font = pygame.font.Font(None, 24)
lose_font = pygame.font.Font(None, 100)
lose_text = lose_font.render("You Lose!", True, (255, 255, 255))
win_text = lose_font.render("You Win!", True, (255, 255, 255))

# יצירת מיקומים רנדומליים לעשב
grass_list = []
for _ in range(20):
    x = random.randint(0, int(WIDTH - CELL_WIDTH))
    y = random.randint(0, int(HIGHT - CELL_HEIGHT))
    grass_list.append((x, y))


def get_soldier_draw_data(board):
    """חישוב מיקום החייל על גבי הגריד לפי המשבצות."""
    soldier_pos = where_is_soldier(board)
    if not soldier_pos:
        return None, (0, 0)

    feet_row = soldier_pos[0][0]
    left_col = min(p[1] for p in soldier_pos)

    top_row = feet_row - (SOLDIER_ROWS - 1)

    x1 = int(left_col * CELL_WIDTH)
    y1 = int(top_row * CELL_HEIGHT)
    x2 = int((left_col + SOLDIER_COLS) * CELL_WIDTH)
    y2 = int((feet_row + 1) * CELL_HEIGHT)

    width = x2 - x1
    height = y2 - y1

    scaled_img = pygame.transform.smoothscale(cropped_soldier_img, (width, height))
    return scaled_img, (x1, y1)


def put_background(screen, grass_list, grass_img, flag_img):
    """ציור רקע המשחק הרגיל (דשא, עשבים ודגל)."""
    screen.fill((90, 100, 49))
    screen.blit(flag_img, (int(46 * CELL_WIDTH), int(21 * CELL_HEIGHT)))
    for grass in grass_list:
        screen.blit(grass_img, grass)


def draw_special_board(screen, board, soldier_img, soldier_pos):
    """ציור הלוח המיוחד עם הגריד והמוקשים (בעת לחיצה על ENTER)."""
    screen.fill((0, 0, 0))

    # קווי הלוח
    for col in range(COLS + 1):
        x = int(col * CELL_WIDTH)
        pygame.draw.line(screen, (0, 100, 0), (x, 0), (x, HIGHT), 3)
        pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, HIGHT), 1)

    for row in range(ROWS + 1):
        y = int(row * CELL_HEIGHT)
        pygame.draw.line(screen, (0, 100, 0), (0, y), (WIDTH, y), 3)
        pygame.draw.line(screen, (0, 255, 0), (0, y), (WIDTH, y), 1)

    # מוקשים
    for row in range(ROWS):
        col = 0
        while col < COLS:
            if board[row][col] == MINE:
                x = int(col * CELL_WIDTH)
                y = int(row * CELL_HEIGHT)

                target_width = int(CELL_WIDTH * 3)
                target_height = int(CELL_HEIGHT)

                original_width = mine_img.get_width()
                original_height = mine_img.get_height()

                scale = min(target_width / original_width, target_height / original_height)
                mine_w = max(1, int(original_width * scale))
                mine_h = max(1, int(original_height * scale))

                scaled_mine = pygame.transform.scale(mine_img, (mine_w, mine_h))
                mine_x = x + (target_width - mine_w) // 2
                mine_y = y + (target_height - mine_h) // 2

                screen.blit(scaled_mine, (mine_x, mine_y))
                col += 3
            else:
                col += 1

    if soldier_img and soldier_pos:
        screen.blit(soldier_img, soldier_pos)


running = True
game_over_surface = None

while running:
    current_soldier_img, soldier_pixel_pos = get_soldier_draw_data(board)

    # בדיקה אם להציג את לוח הגריד או את הרקע הרגיל
    if time.time() < show_grid_until:
        draw_special_board(screen, board, current_soldier_img, soldier_pixel_pos)
    else:
        put_background(screen, grass_list, grass_img, flag_img)
        if current_soldier_img:
            screen.blit(current_soldier_img, soldier_pixel_pos)

    text = font.render("Welcome to The Flag game.\n Have Fun!", True, (255, 255, 255))
    screen.blit(text, (70, 10))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                show_grid_until = time.time() + 1

            move_key = None
            if event.key == pygame.K_DOWN:
                move_key = "s"
            elif event.key == pygame.K_UP:
                move_key = "w"
            elif event.key == pygame.K_LEFT:
                move_key = "a"
            elif event.key == pygame.K_RIGHT:
                move_key = "d"

            if move_key and can_soldier_move(board, move_key):
                do_win = move_soldier(board, move_key)
                if do_win is False:
                    game_over_surface = lose_text
                    running = False
                elif do_win is True:
                    game_over_surface = win_text
                    running = False

                for row in board:
                    print(row)
                print("\n\n\n\n")

    pygame.display.flip()

# הצגת מסך סיום (הפסד/נצחון) לפני סגירה
if game_over_surface:
    screen.blit(game_over_surface, (100, 100))
    pygame.display.flip()
    pygame.time.delay(3000)

pygame.quit()