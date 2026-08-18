import random
import time
from consts import BOARD_COLUMNS, BOARD_ROWS, HIGHT, MINE, WIDTH
from Database import add_game_to_save, load_game
import pygame
from soldier import can_soldier_move, move_soldier, where_is_soldier
from teleport import get_teleport_image, get_teleport_list

pygame.init()

number_and_time = {}
NUMBER_KEYS = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_KP1: 1,
    pygame.K_KP2: 2,
    pygame.K_KP3: 3,
    pygame.K_KP4: 4,
    pygame.K_KP5: 5,
    pygame.K_KP6: 6,
    pygame.K_KP7: 7,
    pygame.K_KP8: 8,
    pygame.K_KP9: 9,
}
game_saves = {}


def save_game(current_board, slot_number):
    game_saves[slot_number] = [row[:] for row in current_board]


cell_size = WIDTH // BOARD_COLUMNS
screen = pygame.display.set_mode((WIDTH, HIGHT))

soldier_img = pygame.image.load("soldier.png").convert_alpha()
soldier_img = pygame.transform.scale(
    soldier_img, (2 * cell_size, 4 * cell_size)
)

mine_img = pygame.image.load("mine.png").convert_alpha()
mine_img = pygame.transform.scale(mine_img, (cell_size * 3, cell_size))

grass_img = pygame.image.load("grass.png").convert_alpha()
grass_img = pygame.transform.scale(grass_img, (cell_size, cell_size))

flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (3 * cell_size, 4 * cell_size))

teleport_img = get_teleport_image(cell_size)

font = pygame.font.Font(None, 24)
lose_font = pygame.font.Font(None, 200)
lose_text = lose_font.render("You Lose!", True, (255, 255, 255))
win_text = lose_font.render("You Win!", True, (255, 255, 255))


def put_background(grass_list, grass_img, flag_img, teleport_img):
    screen.fill((90, 100, 49))
    screen.blit(flag_img, (46 * cell_size, 21 * cell_size))

    for grass in grass_list:
        screen.blit(grass_img, grass)

    # ציור יציב ישירות מתוך הרשימה המעודכנת
    for t_row, t_col in get_teleport_list():
        screen.blit(teleport_img, (t_col * cell_size, t_row * cell_size))


def show_xray(
    board, screen, soldier_img, soldier_x, soldier_y, mine_img, cell_size
):
    screen.fill((0, 0, 0))
    for row in range(BOARD_ROWS + 1):
        pygame.draw.line(
            screen, (0, 100, 0), (0, row * cell_size), (WIDTH, row * cell_size)
        )
    for col in range(BOARD_COLUMNS + 1):
        pygame.draw.line(
            screen,
            (0, 100, 0),
            (col * cell_size, 0),
            (col * cell_size, HIGHT),
        )

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == MINE:
                if col == 0 or board[row][col - 1] != MINE:
                    screen.blit(
                        mine_img, (col * cell_size, row * cell_size)
                    )

    screen.blit(soldier_img, (soldier_x, soldier_y))
    pygame.display.flip()


def run_game(board):
    grass_list = []
    for _ in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HIGHT)
        grass_list.append((x, y))

    text = font.render(
        "Welcome to The Flag game.\n Have Fun!", True, (255, 255, 255)
    )
    text_massage = True
    running = True

    while running:
        soldier_positions = where_is_soldier(board)
        soldier_x = soldier_positions[0][1] * cell_size
        soldier_y = (soldier_positions[0][0] - 3) * cell_size

        put_background(grass_list, grass_img, flag_img, teleport_img)
        screen.blit(soldier_img, (soldier_x, soldier_y))

        if text_massage:
            screen.blit(text, (70, 10))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                move_dir = None
                if event.key == pygame.K_DOWN and can_soldier_move(board, "s"):
                    move_dir = "s"
                elif event.key == pygame.K_UP and can_soldier_move(board, "w"):
                    move_dir = "w"
                elif event.key == pygame.K_LEFT and can_soldier_move(
                    board, "a"
                ):
                    move_dir = "a"
                elif event.key == pygame.K_RIGHT and can_soldier_move(
                    board, "d"
                ):
                    move_dir = "d"

                if move_dir:
                    do_win = move_soldier(board, move_dir)
                    if do_win == False:
                        screen.blit(lose_text, (200, 200))
                        running = False
                        break
                    elif do_win == True:
                        screen.blit(win_text, (200, 200))
                        running = False
                        break

                elif event.key == pygame.K_RETURN:
                    show_xray(
                        board,
                        screen,
                        soldier_img,
                        soldier_x,
                        soldier_y,
                        mine_img,
                        cell_size,
                    )
                    time.sleep(1)
                    pygame.event.clear()

                text_massage = False

                if event.key in NUMBER_KEYS:
                    number_and_time[event.key] = time.time()

            elif event.type == pygame.KEYUP:
                if event.key in number_and_time:
                    press_duration = time.time() - number_and_time.pop(
                        event.key
                    )
                    slot_number = NUMBER_KEYS[event.key]

                    if press_duration <= 1.0:
                        save_game(board, slot_number)
                        add_game_to_save({slot_number: game_saves[slot_number]})
                    elif press_duration > 1.0:
                        new_board = load_game(slot_number)
                        if new_board == False:
                            print("There is no valid save in this slot.")
                        else:
                            board = new_board

        pygame.display.flip()

    for _ in range(3000):
        pygame.display.flip()