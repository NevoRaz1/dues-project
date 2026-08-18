import csv
from pathlib import Path
import pandas as pd


def add_game_to_save(game_save, slot):
    # המרה: אם קיבלנו קוד מקש מ-pygame (49-57), נחסר 48 ונקבל 1-9
    if slot >= 48:
        slot_num = slot - 48
    else:
        slot_num = slot

    # קריטי: המפתח במילון חייב להיות slot_num ולא slot!
    save_dict = {slot_num: game_save}

    file_path = Path(f"game_save_{slot_num}.csv")

    # בדיקה האם הקובץ קיים
    if file_path.exists():
        with open(file_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=save_dict.keys())
            w.writeheader()
            w.writerow(save_dict)
    else:
        df = pd.DataFrame(save_dict)
        df.to_csv(file_path, index=False)

        with open(file_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=save_dict.keys())
            w.writeheader()
            w.writerow(save_dict)

    # הדפסה לבדיקה שמוודאת שהמפתח הוא 1
    print(save_dict)