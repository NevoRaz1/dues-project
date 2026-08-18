import csv
from pathlib import Path

def load_game(slot):
    filename = Path(f"game_save_{slot}.csv")

    if filename.exists():
        save_board = []
        try:
            with open(filename, "r") as f:
                data = csv.reader(f)
                for row in data:

                    int_row = [int(cell.strip()) for cell in row if cell.strip() != ""]
                    if int_row:
                        save_board.append(int_row)

            print(save_board)
            return save_board
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return False
    else:
        return False

def add_game_to_save(game_save):
    for slot in game_save.keys():
        filename = f"game_save_{slot}.csv"
        board_to_save = game_save[slot]

        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerows(board_to_save)