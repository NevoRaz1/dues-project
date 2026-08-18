import csv
import pandas as pd
from pathlib import Path


def add_game_to_save(game_save,slot):
    # File path


    # File path
    a = Path(f"game_save_{slot-48}.csv")

    # Check if the file exists
    if a.exists():

        with open(f'game_save_{slot-48}.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=game_save)
            writer.writeheader()
            writer.writerows(game_save)



    else:
        df = pd.DataFrame(game_save)

        csv_file_path = f'game_save_{slot-48}.csv'

        df.to_csv(csv_file_path, index=False)



