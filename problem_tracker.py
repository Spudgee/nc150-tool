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

def initialize_categories():
    categories = {}

    ARRAYS_AND_HASHING = "Arrays & Hashing"
    TWO_POINTERS = "Two Pointers"
    STACK = "Stack"
    BINARY_SEARCH = "Binary Search"
    SLIDING_WINDOW = "Sliding Window"
    LINKED_LIST = "Linked List"
    TREES = "Trees"
    TRIES = "Tries"
    BACKTRACKING = "Backtracking"
    HEAP_PRIORITY_QUEUE = "Heap / Priority Queue"
    GRAPHS = "Graphs"
    ADVANCED_GRAPHS = "Advanced Graphs"
    ONE_D_DP = "1-D Dynamic Programming"
    TWO_D_DP = "2-D Dynamic Programming"
    GREEDY = "Greedy"
    INTERVALS = "Intervals"
    MATH_AND_GEOMETRY = "Math & Geometry"
    BIT_MANIPULATION = "Bit Manipulation"

    arrays_and_hashing = Category(ARRAYS_AND_HASHING)
    two_pointers = Category(TWO_POINTERS, [ARRAYS_AND_HASHING])
    stack = Category(STACK, [ARRAYS_AND_HASHING])
    binary_search = Category(BINARY_SEARCH, [ARRAYS_AND_HASHING])
    sliding_window = Category(SLIDING_WINDOW, [ARRAYS_AND_HASHING])
    linked_list = Category(LINKED_LIST)
    trees = Category(TREES)
    tries = Category(TRIES, [TREES])
    backtracking = Category(BACKTRACKING)
    heap_priority_queue = Category(HEAP_PRIORITY_QUEUE, [BACKTRACKING])
    graphs = Category(GRAPHS)
    advanced_graphs = Category(ADVANCED_GRAPHS, [GRAPHS])
    one_d_dp = Category(ONE_D_DP)
    two_d_dp = Category(TWO_D_DP, [ONE_D_DP])
    greedy = Category(GREEDY)
    intervals = Category(INTERVALS)
    math_and_geometry = Category(MATH_AND_GEOMETRY)
    bit_manipulation = Category(BIT_MANIPULATION, [TWO_D_DP])

    # Establish parent-child relationships
    arrays_and_hashing.children = [two_pointers, stack, binary_search, sliding_window]
    two_pointers.parents = [arrays_and_hashing]
    stack.parents = [arrays_and_hashing]
    binary_search.parents = [arrays_and_hashing]
    sliding_window.parents = [arrays_and_hashing]
    trees.children = [tries]
    tries.parents = [trees]
    backtracking.children = [heap_priority_queue]
    heap_priority_queue.parents = [backtracking]
    graphs.children = [advanced_graphs]
    advanced_graphs.parents = [graphs]
    one_d_dp.children = [two_d_dp]
    two_d_dp.parents = [one_d_dp]
    two_d_dp.children = [bit_manipulation]
    bit_manipulation.parents = [two_d_dp]

    # Add categories to the dictionary
    categories[ARRAYS_AND_HASHING] = arrays_and_hashing
    categories[TWO_POINTERS] = two_pointers
    categories[STACK] = stack
    categories[BINARY_SEARCH] = binary_search
    categories[SLIDING_WINDOW] = sliding_window
    categories[LINKED_LIST] = linked_list
    categories[TREES] = trees
    categories[TRIES] = tries
    categories[BACKTRACKING] = backtracking
    categories[HEAP_PRIORITY_QUEUE] = heap_priority_queue
    categories[GRAPHS] = graphs
    categories[ADVANCED_GRAPHS] = advanced_graphs
    categories[ONE_D_DP] = one_d_dp
    categories[TWO_D_DP] = two_d_dp
    categories[GREEDY] = greedy
    categories[INTERVALS] = intervals
    categories[MATH_AND_GEOMETRY] = math_and_geometry
    categories[BIT_MANIPULATION] = bit_manipulation

    # Return dictionary of Category objects containing relationships
    return categories
