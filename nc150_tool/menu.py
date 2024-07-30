import sys
import os
import webbrowser
import json
import subprocess
from progress_manager import save_progress, load_progress
from downloader import download_explanations
from util import construct_video_path, open_video, delete_videos, reset_completion_data

# Display set of options and a title with generic function
def display_menu(title, options):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{title}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input(f"\nEnter your choice (1-{len(options)}): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display main menu options for overall Neetcode manager
def main_menu(categories):
    options = ["Download Manager", "Problem Manager", "Settings",  "Exit"]
    while True:
        choice = display_menu("------- NeetCode 150 Manager -------", options)
        if choice == 1:
            download_manager_menu(categories)
        elif choice == 2:
            problem_manager_menu(categories)
        elif choice == 3:
            settings_menu(categories)
        elif choice == 4:
            print("Exiting...")
            sys.exit()

# Display download menu options
def download_manager_menu(categories):
    options = ["Download Neetcode explanations", "Back"]
    while True:
        choice = display_menu("------- NeetCode 150 Download Manager -------", options)
        if choice == 1:
            download_explanations(categories)
            # Pause so that failed downloads can be viewed
            input("Press any button to continue...")
        elif choice == 2:
            return

# Display download menu options
def problem_manager_menu(categories):
    while True:
        options = [f"{category_name}: {sum(p.is_completed for p in category.problems)}/{len(category.problems)} ({(sum(p.is_completed for p in category.problems) / len(category.problems) * 100):.1f}%)" 
                   for category_name, category in categories.items()]
        options.append("Back")
        
        choice = display_menu("------- NeetCode 150 Problem Manager -------", options)
        if choice == len(options):
            return
        else:
            category_name = list(categories.keys())[choice - 1]
            category_menu(categories, categories[category_name])

def settings_menu(categories):
    options = ["Delete all downloaded videos", "Reset completition progress", "Back"]
    while True:
        choice = display_menu("------- NeetCode 150 Download Manager -------", options)
        if choice == 1:
            delete_videos()
        elif choice == 2:
            reset_completion_data(categories)
        elif choice == 3:
            return

def category_menu(categories, category):
    while True:
        options = [f"{'[x]' if problem.is_completed else '[ ]'} {problem.difficulty} - {problem.problem_name}" 
                   for problem in category.problems]
        options.append("Back")
        
        choice = display_menu(f"(------- NeetCode 150 {category.category_name} -------", options)
        if choice == len(options):
            return  # Back to previous menu
        else:
            problem = category.problems[choice - 1]
            problem_menu(categories, problem)

def problem_menu(categories, problem):
    while True:
        options = [
            "Watch explanation",
            "Open LeetCode",
            f"Mark as {'incomplete' if problem.is_completed else 'complete'}",
            "Back"
        ]
        
        choice = display_menu(f"------- NeetCode 150 {problem.problem_name} -------", options)
        print(f"\nDifficulty: {problem.difficulty}")
        print(f"Status: {'Completed' if problem.is_completed else 'Incomplete'}")

        if choice == 1:
            video_path = construct_video_path(problem.category, problem)
            if os.path.exists(video_path):
                open_video(video_path)
            else:
                print(f"Video file not found: {video_path}")
        elif choice == 2:
            if problem.leetcode_url:
                webbrowser.open(problem.leetcode_url)
            else:
                print("No LeetCode URL available.")
        elif choice == 3:
            problem.is_completed = not problem.is_completed
            save_progress(categories)
            print(f"Problem marked as {'incomplete' if not problem.is_completed else 'complete'}.")
        elif choice == 4:
            return