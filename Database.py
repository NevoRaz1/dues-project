import os
import pandas as pd


def add_game_to_save(game_save, slot):
    # Step 1 / 2: Calculate slot number and file path
    slot_num = slot - 48 if slot >= 48 else slot
    csv_file_path = f"game_save_{slot_num}.csv"

    # Step 3: Check if file exists, delete if true, otherwise notify creation
    if os.path.exists(csv_file_path):
        print(f"הקובץ '{csv_file_path}' קיים. מוחק את הקובץ הנוכחי...")
        os.remove(csv_file_path)
    else:
        print(f"הקובץ '{csv_file_path}' לא קיים. יוצר קובץ חדש...")

    # Step 4: Create a DataFrame using DataFrame function
    df = pd.DataFrame(game_save)

    # Step 5: Write the DataFrame to a CSV file using to_csv() function where file path is passed
    df.to_csv(csv_file_path, index=False, header=False)

    print(f'CSV file "{csv_file_path}" has been created successfully.')