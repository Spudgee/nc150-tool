import sys

# Display main menu options for overall Neetcode manager
def main_menu(categories):
    while True:
        print("\nNeetCode 150 Manager")
        print("1. Download manager")
        print("2. Problem Tracker")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        try:
            choice = int(choice)
            # FIX: Access download menu
            if choice == 1:
                break
            # Access problem tracking menu
            elif choice == 2:
                problem_tracker_menu(categories)
            elif choice == 3:
                # Exit
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display main menu options for overall Neetcode manager
def problem_tracker_menu(categories):
    while True:
        print("\nNeetCode 150 Problem Tracker")
        # Display categories with completion rates
        for i, (category_name, category) in enumerate(categories.items(), 1):
            total = len(category.problems)
            completed = sum(problem.is_completed for problem in category.problems)
            completion_rate = (completed / total) * 100 if total > 0 else 0
            print(f"{i}. {category_name}: {completed}/{total} ({completion_rate:.1f}%)")

        print(f"{len(categories) + 1}. Back")

        choice = input(f"Enter your choice (1-{len(categories) + 1}): ")
        try:
            choice = int(choice)
            # User selected category
            if 1 <= choice <= len(categories):
                category_name = list(categories.keys())[choice - 1]
                display_category_problems(categories[category_name])
            elif choice == len(categories) + 1:
                # Back to main menu
                main_menu(categories)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")