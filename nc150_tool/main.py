from menu import main_menu
from progress_manager import save_progress, load_progress
from category_initializer import initialize_categories
from problem_initializer import initialize_problems

def main():
    # Initialize category data
    categories = initialize_categories()
    # Initialize problems within each category
    categories = initialize_problems(categories)
    # Load progress stored in JSON
    load_progress(categories)
    # Start main menu sequence
    main_menu(categories)
    # Save progress in JSON
    save_progress(categories)

if __name__ == "__main__":
    main()
