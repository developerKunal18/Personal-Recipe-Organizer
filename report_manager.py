from storage import load_recipes


def show_report():
    recipes = load_recipes()

    total_recipes = len(recipes)

    total_prep_time = sum(
        recipe["prep_time"] for recipe in recipes
    )

    total_cook_time = sum(
        recipe["cook_time"] for recipe in recipes
    )

    categories = {}

    for recipe in recipes:
        category = recipe["category"]

        categories[category] = categories.get(category, 0) + 1

    print("\n========== RECIPE REPORT ==========")

    print(f"Total Recipes       : {total_recipes}")
    print(f"Total Prep Time     : {total_prep_time} minutes")
    print(f"Total Cooking Time  : {total_cook_time} minutes")

    print("\nRecipes by Category:")

    if not categories:
        print("No recipe records available.")
    else:
        for category, count in categories.items():
            print(f"{category:<15}: {count}")

    print("===================================")
