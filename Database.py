import pandas
import json
from pathlib import Path

def add_game_to_save(game_save,slot):
    # File path


    file = Path(f"game_save_{slot}.json")
    if file.exists():
        with open(f"game_save_{slot}.json", 'w') as f:
            json.dump(game_save, f)
    else:
        f = open(f"game_save_{slot}.json", "x")
