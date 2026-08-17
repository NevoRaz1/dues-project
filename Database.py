import csv
import pandas as pd
import json
from pathlib import Path

def add_game_to_save(game_save,slot):
    # File path


    # Step 3 Create a DataFrame using DataFrame function
    df = pd.DataFrame(game_save)

    # Step 4 Specify the file path to save data
    csv_file_path = f'game_save_{slot-48}.csv'

    # Step 5 Write the DataFrame to a CSV file using to_csv() function where file path is passed
    df.to_csv(csv_file_path, index=False)

    print(f'CSV file &quot;{csv_file_path}&quot; has been created successfully.')