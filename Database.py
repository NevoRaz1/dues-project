from pathlib import Path
import pandas as pd


def add_game_to_save(game_save, slot):
    # Step 1 / 2: Calculate slot number and file path
    slot_num = slot - 48 if slot >= 48 else slot
    csv_file_path = Path(f"game_save_{slot_num}.csv")

    # Step 3: Check if file exists; if exists delete old file, otherwise prepare to create new
    if csv_file_path.is_file():
        print(f"File '{csv_file_path}' exists. Overwriting...")
        csv_file_path.unlink()
    else:
        print(f"File '{csv_file_path}' does not exist. Creating a new file...")

    # Step 4: Create a DataFrame using DataFrame function
    df = pd.DataFrame(game_save)

    # Step 5: Write the DataFrame to the CSV file
    df.to_csv(csv_file_path, index=False, header=False)

    print(f'CSV file "{csv_file_path}" has been saved successfully.')