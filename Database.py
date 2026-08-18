import csv
from pathlib import Path


def load_game(slot):
    filename = f"game_save_{slot}.csv"
    a = Path(filename)

    if a.exists():
        save_board = []
        try:
            with open(filename, "r") as f:
                data = csv.reader(f)
                for row in data:
                    int_row = [int(cell) for cell in row]
                    save_board.append(int_row)

            return save_board

        except (ValueError, IndexError):
            return False
    else:
        return False


def add_game_to_save(game_save):
    # עובר על כל סלוט והלוח שלו ושומר לקובץ נפרד
    for slot, board_to_save in game_save.items():
        filename = f"game_save_{slot}.csv"

        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerows(board_to_save)