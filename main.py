from menu import main_menu
from problem_tracker import initialize_categories, initialize_problems
from progress_manager import save_progress, load_progress

def main():
    categories = initialize_categories()
    categories = initialize_problems(categories)
    load_progress(categories)
    main_menu(categories)
    save_progress(categories)

if __name__ == "__main__":
    main()
