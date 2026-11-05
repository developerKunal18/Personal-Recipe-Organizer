def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def input_required(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(message, minimum=0):
    while True:
        try:
            value = int(input(message))

            if value < minimum:
                print(
                    f"Enter a number greater than or equal to {minimum}."
                )
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_multiline(message):
    print(message)
    print("Enter one item per line.")
    print("Type 'done' when finished.")

    values = []

    while True:
        value = input("> ").strip()

        if value.lower() == "done":
            break

        if value:
            values.append(value)

    return values


def display_recipe(recipe):
    print("-" * 65)
    print(f"Recipe ID       : {recipe['id']}")
    print(f"Recipe Name     : {recipe['name']}")
    print(f"Category        : {recipe['category']}")
    print(f"Servings        : {recipe['servings']}")
    print(f"Preparation     : {recipe['prep_time']} minutes")
    print(f"Cooking Time    : {recipe['cook_time']} minutes")

    print("\nIngredients:")

    for ingredient in recipe["ingredients"]:
        print(f"  - {ingredient}")

    print("\nPreparation Steps:")

    for index, step in enumerate(recipe["steps"], start=1):
        print(f"  {index}. {step}")

    print(f"\nNotes           : {recipe['notes']}")
