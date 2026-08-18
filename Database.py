import csv
import pandas as pd
from pathlib import Path

def load_game(slot):
    a = Path(f"game_save_{slot - 48}.csv")

    # Check if the file exists
    if a.exists():

        filename = f"game_save_{slot-48}.csv"

        # opening the file using "with"
        # statement
        save_board={}
        with open(f'game_save_{slot-48}.csv', mode='r') as infile:
            reader = csv.reader(infile)
            with open(f'game_save_{slot-48}.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                save_board = {rows[0]: rows[1] for rows in reader}

        board=save_board.get(slot-48)
        return board
    else:
        return False

def add_game_to_save(game_save,slot):
    # File path


    # File path
    a = Path(f"game_save_{slot-48}.csv")

    # Check if the file exists
    if a.exists():

        with open(f"game_save_{slot-48}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, game_save.keys())
            w.writeheader()
            w.writerow(game_save)



    else:
        df = pd.DataFrame(game_save)

        csv_file_path = f'game_save_{slot-48}.csv'

        df.to_csv(csv_file_path, index=False)

        with open(f"game_save_{slot-48}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, game_save.keys())
            w.writeheader()
            w.writerow(game_save)



