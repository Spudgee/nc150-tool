import sys
import os
import webbrowser
import json
import subprocess
from download_manager import download_explanations

# Display main menu options for overall Neetcode manager
def main_menu(categories):
    while True:
        # Clear for both Windows and Mac
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNeetCode 150 Manager")
        print("1. Download manager")
        print("2. Problem Tracker")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        try:
            choice = int(choice)
            # FIX: Access download menu
            if choice == 1:
                download_manager_menu(categories)
            # Access problem tracking menu
            elif choice == 2:
                problem_tracker_menu(categories)
            elif choice == 3:
                # Exit program
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display main menu options for download manager
def download_manager_menu(categories):
    while True:
        # Clear for both Windows and Mac
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNeetCode 150 Download Manager")
        # Display categories with completion rates
        print(f"1. Download Neetcode explanations")
        print(f"2. Back")

        choice = input(f"Enter your choice (1-2): ")
        try:
            choice = int(choice)
            # User selected category
            if choice == 1:
                download_explanations(categories)
            elif choice == 2:
                # Back to main menu
                main_menu(categories)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display problem tracking menu with completion rates/progress
def problem_tracker_menu(categories):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
            if 1 <= choice <= len(categories):
                category_name = list(categories.keys())[choice - 1]
                category_menu(categories, categories[category_name])  # This is correct
            elif choice == len(categories) + 1:
                return  # This will go back to the main menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display problems within a category
def category_menu(categories, category):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nNeetCode 150 {category.category_name}")
        
        problems = category.problems
        for i, problem in enumerate(problems, 1):
            checkbox = "[x]" if problem.is_completed else "[ ]"
            print(f"{i}. {checkbox} {problem.difficulty} - {problem.problem_name}")
        
        print(f"{len(problems) + 1}. Back")
        
        choice = input(f"Enter your choice (1-{len(problems) + 1}): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(problems):
                problem = problems[choice - 1]
                problem_menu(categories, problem)
            elif choice == len(problems) + 1:
                return  # This will go back to the previous menu
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display specific problem menu
def problem_menu(categories, problem):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nNeetCode 150 {problem.problem_name}")
        print(f"Difficulty: {problem.difficulty}")
        print(f"Status: {'Completed' if problem.is_completed else 'Not Completed'}")
        print(f"1. Watch explanation")
        print(f"2. Open LeetCode")
        print(f"3. Mark completed")
        print(f"4. Back")
        
        choice = input("Enter your choice (1-4): ")
        try:
            choice = int(choice)
            # Open local video file
            if choice == 1:
                video_path = construct_video_path(problem.category, problem)
                if os.path.exists(video_path):
                    open_video(video_path)
                else:
                    print(f"Video file not found: {video_path}")
            # Open LeetCode URL for problem
            elif choice == 2:
                if problem.leetcode_url:
                    webbrowser.open(problem.leetcode_url)
                else:
                    print("No LeetCode URL available.")
            # Mark problem as completed and save progress
            elif choice == 3:
                problem.is_completed = not problem.is_completed
                save_progress()
                print(f"Problem marked as completed.")
            # Go back
            elif choice == 4:
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Open video file at video_path
def open_video(video_path):
    if os.name == 'nt':  # For Windows
        os.startfile(video_path)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.call(('open', video_path))
    else:
        print(f"Unsupported operating system. Please open the video manually: {video_path}")