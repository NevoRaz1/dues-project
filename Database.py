import ast
import csv
from pathlib import Path


def add_game_to_save(game_save, slot):
    slot_num = slot - 48 if slot >= 48 else slot
    file_path = Path(f"game_save_{slot_num}.csv")

    # אם הועבר הלוח ישירות, עוטפים אותו במילון {מספר_סלוט: לוח}
    if not isinstance(game_save, dict):
        save_data = {str(slot_num): game_save}
    else:
        save_data = {str(k): v for k, v in game_save.items()}

    # כתיבה ל-CSV כמילון: השורה הראשונה היא מספר הסלוט, השורה השנייה היא הלוח
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(save_data.keys()))
        writer.writeheader()
        writer.writerow(save_data)

    print(f"Game saved to {file_path}")


def load_game(slot):
    slot_num = slot - 48 if slot >= 48 else slot
    file_path = Path(f"game_save_{slot_num}.csv")

    if file_path.exists():
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # שליפת הערך לפי מפתח הסלוט והמרת מחרוזת הטקסט חזרה למטריצה
                if str(slot_num) in row:
                    return ast.literal_eval(row[str(slot_num)])
    return False