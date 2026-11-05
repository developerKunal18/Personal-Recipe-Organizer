from storage import initialize_storage

from recipe_manager import (
    add_recipe,
    view_recipes,
    search_recipes,
    filter_by_category,
    update_recipe,
    delete_recipe
)

from report_manager import show_report


def main():
    initialize_storage()

    while True:
        print("\n================================")
        print("     PERSONAL RECIPE ORGANIZER")
        print("================================")

        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipe")
        print("4. Filter by Category")
        print("5. Update Recipe")
        print("6. Delete Recipe")
        print("7. View Reports")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_recipe()

        elif choice == "2":
            view_recipes()

        elif choice == "3":
            search_recipes()

        elif choice == "4":
            filter_by_category()

        elif choice == "5":
            update_recipe()

        elif choice == "6":
            delete_recipe()

        elif choice == "7":
            show_report()

        elif choice == "8":
            print("\nThank you for using Recipe Organizer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
