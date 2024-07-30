import sys
import os
import webbrowser
import json
import subprocess
from progress_manager import save_progress, load_progress
from download_manager import download_explanations
from util import construct_video_path, open_video

# Display set of options and a title with generic function
def display_menu(title, options):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{title}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input(f"Enter your choice (1-{len(options)}): ")
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
    options = ["Download Manager", "Problem Manager", "Exit"]
    while True:
        choice = display_menu("------- NeetCode 150 Manager -------", options)
        if choice == 1:
            download_manager_menu(categories)
        elif choice == 2:
            problem_tracker_menu(categories)
        elif choice == 3:
            print("Exiting...")
            sys.exit()

def download_manager_menu(categories):
    options = ["Download Neetcode explanations", "Back"]
    while True:
        choice = display_menu("------- NeetCode 150 Download Manager -------", options)
        if choice == 1:
            download_explanations(categories)
        elif choice == 2:
            return  # Back to main menu

def problem_tracker_menu(categories):
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
        
        print(f"\nDifficulty: {problem.difficulty}")
        print(f"Status: {'Completed' if problem.is_completed else 'Incomplete'}")
        
        choice = display_menu(f"------- NeetCode 150 {problem.problem_name} -------", options)
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