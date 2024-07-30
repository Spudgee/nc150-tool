class LeetCodeProblem:
    def __init__(self, problem_name, difficulty, parent_category, category, neetcode_url=None, leetcode_url=None, is_completed=False):
        self.problem_name = problem_name
        self.difficulty = difficulty
        self.parent_category = parent_category
        self.category = category
        self.neetcode_url = neetcode_url
        self.leetcode_url = leetcode_url
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "[x]" if self.is_completed else "[ ]"
        return f" {self.problem_name} {self.difficulty} {self.parent_category} {self.category} {self.neetcode_url} {self.leetcode_url}"

    def get_display(self):
        status = "[x]" if self.is_completed else "[ ]"
        return f" {self.parent_category}-{self.difficulty}-{self.problem_name}"