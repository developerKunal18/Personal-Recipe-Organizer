import json
import os

from config import DATA_DIR, RECIPES_FILE


def initialize_storage():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, "w") as file:
            json.dump([], file, indent=4)


def load_recipes():
    initialize_storage()

    try:
        with open(RECIPES_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_recipes(recipes):
    initialize_storage()

    with open(RECIPES_FILE, "w") as file:
        json.dump(recipes, file, indent=4)
