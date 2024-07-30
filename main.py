from menu import main_menu
from problem_tracker import initialize_categories, initialize_problems

def main():
    categories = initialize_categories()
    categories = initialize_problems(categories)
    main_menu(categories)

if __name__ == "__main__":
    main()
