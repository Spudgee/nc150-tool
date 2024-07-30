import json
import os

PROGRESS_FILE = 'progress.json'

# Save completed problems within dictionary of progress
def save_progress(categories):
    progress = {}
    for category_name, category in categories.items():
        progress[category_name] = {
            problem.problem_name: problem.is_completed
            for problem in category.problems
        }
    
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)

# Load progress if it exists
def load_progress(categories):
    if not os.path.exists(PROGRESS_FILE):
        print("No saved progress found. Starting fresh.")
        return
    try:
        with open(PROGRESS_FILE, 'r') as f:
            progress = json.load(f)
        
        # Load dictionary from JSON and set appropriate problems to completed
        for category_name, category in categories.items():
            if category_name in progress:
                for problem in category.problems:
                    if problem.problem_name in progress[category_name]:
                        problem.is_completed = progress[category_name][problem.problem_name]
        print("Progress loaded successfully.")
    except json.JSONDecodeError:
        print("Error reading progress file. Starting fresh.")
    except Exception as e:
        print(f"An error occurred while loading progress: {str(e)}. Starting fresh.")