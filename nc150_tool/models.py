class Category:
    def __init__(self, category_name, parents=[], children=[]):
        self.category_name = category_name
        self.parents = parents
        self.children = children
        self.problems = []
        self.is_completed = False

    def add_problem(self, problem):
        self.problems.append(problem)

    def mark_completed(self):
        self.is_completed = True

    def is_all_completed(self):
        return all(problems.is_completed for problem in self.problems)

class Problem:
    def __init__(self, category, difficulty, problem_name, neetcode_url=None, leetcode_url=None, is_completed=False):
        self.category = category
        self.difficulty = difficulty
        self.problem_name = problem_name
        self.neetcode_url = neetcode_url
        self.leetcode_url = leetcode_url
        self.is_completed = is_completed

    def is_completed(self):
        return self.is_completed

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "[x]" if self.is_completed else "[ ]"
        return f" {self.problem_name} {self.difficulty} {self.parent_category} {self.category} {self.neetcode_url} {self.leetcode_url}"

    def get_display(self):
        status = "[x]" if self.is_completed else "[ ]"
        return f" {self.parent_category}-{self.difficulty}-{self.problem_name}"