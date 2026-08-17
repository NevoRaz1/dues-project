import pandas
import json
from pathlib import Path

def add_game_to_save(game_save,slot):
    # File path

    if slot == 1:
        file = Path("game_save_1.json")
        if file.exists():
            with open("game_save_1.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_1.json', "x")
    elif slot == 2:
        file = Path("game_save_2.json")
        if file.exists():
            with open("game_save_2.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_2.json', "x")
    elif slot == 3:
        file = Path("game_save_3.json")
        if file.exists():
            with open("game_save_3.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_3.json', "x")
    elif slot == 4:
        file = Path("game_save_4.json")
        if file.exists():
            with open("game_save_4.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_4.json', "x")
    elif slot == 5:
        file = Path("game_save_5.json")
        if file.exists():
            with open("game_save_5.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_5.json', "x")
    elif slot == 6:
        file = Path("game_save_6.json")
        if file.exists():
            with open("game_save_6.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_6.json', "x")
    elif slot == 7:
        file = Path("game_save_7.json")
        if file.exists():
            with open("game_save_7.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_7.json', "x")
    elif slot == 8:
        file = Path("game_save_8.json")
        if file.exists():
            with open("game_save_8.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_8.json', "x")
    elif slot == 9:
        file = Path("game_save_9.json")
        if file.exists():
            with open("game_save_9.json", 'w') as f:
                json.dump(game_save, f)
        else:
            f = open('game_save_9.json', "x")