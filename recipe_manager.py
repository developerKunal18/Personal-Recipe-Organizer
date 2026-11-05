from config import CATEGORIES
from storage import load_recipes, save_recipes

from utils import (
    get_next_id,
    input_required,
    input_integer,
    input_multiline,
    display_recipe
)


def select_category():
    print("\n--- RECIPE CATEGORIES ---")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    try:
        choice = int(input("Select category: "))
    except ValueError:
        print("Enter a valid category number.")
        return None

    if choice < 1 or choice > len(CATEGORIES):
        print("Invalid category.")
        return None

    return CATEGORIES[choice - 1]


def add_recipe():
    recipes = load_recipes()

    print("\n--- ADD RECIPE ---")

    name = input_required("Enter recipe name: ")

    category = select_category()

    if category is None:
        return

    servings = input_integer("Enter number of servings: ", minimum=1)
    prep_time = input_integer("Preparation time in minutes: ")
    cook_time = input_integer("Cooking time in minutes: ")

    ingredients = input_multiline(
        "\nEnter ingredients:"
    )

    if not ingredients:
        print("At least one ingredient is required.")
        return

    steps = input_multiline(
        "\nEnter preparation steps:"
    )

    if not steps:
        print("At least one preparation step is required.")
        return

    notes = input("Enter additional notes: ").strip()

    recipe = {
        "id": get_next_id(recipes),
        "name": name,
        "category": category,
        "servings": servings,
        "prep_time": prep_time,
        "cook_time": cook_time,
        "ingredients": ingredients,
        "steps": steps,
        "notes": notes
    }

    recipes.append(recipe)
    save_recipes(recipes)

    print("\nRecipe added successfully!")


def view_recipes():
    recipes = load_recipes()

    if not recipes:
        print("\nNo recipes available.")
        return

    print("\n--- ALL RECIPES ---")

    for recipe in recipes:
        display_recipe(recipe)


def search_recipes():
    recipes = load_recipes()

    keyword = input_required(
        "Enter recipe name or ingredient: "
    ).lower()

    results = []

    for recipe in recipes:
        name_match = keyword in recipe["name"].lower()

        ingredient_match = any(
            keyword in ingredient.lower()
            for ingredient in recipe["ingredients"]
        )

        if name_match or ingredient_match:
            results.append(recipe)

    if not results:
        print("\nNo matching recipes found.")
        return

    print("\n--- SEARCH RESULTS ---")

    for recipe in results:
        display_recipe(recipe)


def filter_by_category():
    recipes = load_recipes()

    category = select_category()

    if category is None:
        return

    results = [
        recipe for recipe in recipes
        if recipe["category"] == category
    ]

    if not results:
        print(f"\nNo recipes found in {category}.")
        return

    print(f"\n--- {category.upper()} RECIPES ---")

    for recipe in results:
        display_recipe(recipe)


def update_recipe():
    recipes = load_recipes()

    try:
        recipe_id = int(input("Enter recipe ID to update: "))
    except ValueError:
        print("Enter a valid recipe ID.")
        return

    recipe = next(
        (item for item in recipes if item["id"] == recipe_id),
        None
    )

    if not recipe:
        print("Recipe not found.")
        return

    print("\nLeave a field blank to keep its existing value.")

    name = input("Recipe name: ").strip()

    if name:
        recipe["name"] = name

    print("\nUpdate category?")

    change_category = input("Enter y or n: ").strip().lower()

    if change_category == "y":
        category = select_category()

        if category is not None:
            recipe["category"] = category

    servings = input("Servings: ").strip()

    if servings:
        try:
            servings = int(servings)

            if servings < 1:
                print("Servings must be at least 1.")
                return

            recipe["servings"] = servings

        except ValueError:
            print("Invalid servings.")
            return

    prep_time = input("Preparation time: ").strip()

    if prep_time:
        try:
            prep_time = int(prep_time)

            if prep_time < 0:
                print("Preparation time cannot be negative.")
                return

            recipe["prep_time"] = prep_time

        except ValueError:
            print("Invalid preparation time.")
            return

    cook_time = input("Cooking time: ").strip()

    if cook_time:
        try:
            cook_time = int(cook_time)

            if cook_time < 0:
                print("Cooking time cannot be negative.")
                return

            recipe["cook_time"] = cook_time

        except ValueError:
            print("Invalid cooking time.")
            return

    print("\nUpdate ingredients?")

    if input("Enter y or n: ").strip().lower() == "y":
        ingredients = input_multiline(
            "Enter updated ingredients:"
        )

        if ingredients:
            recipe["ingredients"] = ingredients

    print("\nUpdate preparation steps?")

    if input("Enter y or n: ").strip().lower() == "y":
        steps = input_multiline(
            "Enter updated preparation steps:"
        )

        if steps:
            recipe["steps"] = steps

    notes = input("Additional notes: ").strip()

    if notes:
        recipe["notes"] = notes

    save_recipes(recipes)

    print("\nRecipe updated successfully!")


def delete_recipe():
    recipes = load_recipes()

    try:
        recipe_id = int(input("Enter recipe ID to delete: "))
    except ValueError:
        print("Enter a valid recipe ID.")
        return

    updated_recipes = [
        recipe for recipe in recipes
        if recipe["id"] != recipe_id
    ]

    if len(updated_recipes) == len(recipes):
        print("Recipe not found.")
        return

    save_recipes(updated_recipes)

    print("Recipe deleted successfully!")
