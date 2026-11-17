import json
import os

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "savegame.json")

def save(pets):
    d = [p.to_dict() for p in pets]
    with open(F, "w") as f:
        json.dump(d, f, indent=2)
    print("Game saved!")

def load():
    from tamagotchi import Tamagotchi
    if not os.path.exists(F):
        print("No save file found.")
        return None
    try:
        with open(F, "r") as f:
            d = json.load(f)
        pets = [Tamagotchi.from_dict(x) for x in d]
        print("Game loaded!")
        return pets
    except (json.JSONDecodeError, KeyError):
        print("Save file is corrupted.")
        return None
