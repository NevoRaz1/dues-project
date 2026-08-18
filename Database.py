import csv
import pandas as pd
from pathlib import Path


def add_game_to_save(game_save,slot):
    # File path

    dict={slot-48:game_save}

    # File path
    a = Path(f"game_save_{slot-48}.csv")

    # Check if the file exists
    if a.exists():

        with open(f"game_save_{slot-48}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, dict.keys())
            w.writeheader()
            w.writerow(dict)



    else:
        df = pd.DataFrame(dict)

        csv_file_path = f'game_save_{slot-48}.csv'

        df.to_csv(csv_file_path, index=False)

        with open(f"game_save_{slot-48}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, dict.keys())
            w.writeheader()
            w.writerow(dict)



