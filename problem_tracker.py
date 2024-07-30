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

def initialize_problems(categories):
    problems = []

    # 1. Arrays and Hashing
    problems.extend([
        Problem("Arrays & Hashing", "Easy", "Contains Duplicate", "https://www.youtube.com/watch?v=3OamzN90kPg"),
        Problem("Arrays & Hashing", "Easy", "Valid Anagram", "https://www.youtube.com/watch?v=9UtInBqnCgA"),
        Problem("Arrays & Hashing", "Easy", "Two Sum", "https://www.youtube.com/watch?v=KLlXCFG5TnA"),
        Problem("Arrays & Hashing", "Medium", "Group Anagrams", "https://www.youtube.com/watch?v=vzdNOK2oB2E"),
        Problem("Arrays & Hashing", "Medium", "Top K Frequent Elements", "https://www.youtube.com/watch?v=YPTqKIgVk-k"),
        Problem("Arrays & Hashing", "Medium", "Product of Array Except Self", "https://www.youtube.com/watch?v=bNvIQI2wAjk"),
        Problem("Arrays & Hashing", "Medium", "Valid Sudoku", "https://www.youtube.com/watch?v=TjFXEUCMqI8"),
        Problem("Arrays & Hashing", "Medium", "Encode and Decode Strings", "https://www.youtube.com/watch?v=B1k_sxOSgv8"),
        Problem("Arrays & Hashing", "Medium", "Longest Consecutive Sequence", "https://www.youtube.com/watch?v=P6RZZMu_maU"),
    ])

    # 2. Two Pointers
    problems.extend([
        Problem("Two Pointers", "Easy", "Valid Palindrome", "https://www.youtube.com/watch?v=jJXJ16kPFWg"),
        Problem("Two Pointers", "Medium", "Two Sum II - Input Array Is Sorted", "https://www.youtube.com/watch?v=cQ1Oz4ckceM"),
        Problem("Two Pointers", "Medium", "3Sum", "https://www.youtube.com/watch?v=jzZsG8n2R9A"),
        Problem("Two Pointers", "Medium", "Container With Most Water", "https://www.youtube.com/watch?v=UuiTKBwPgAo"),
        Problem("Two Pointers", "Hard", "Trapping Rain Water", "https://www.youtube.com/watch?v=ZI2z5pq0TqA"),
    ])

    # 3. Stack
    problems.extend([
        Problem("Stack", "Easy", "Valid Parentheses", "https://www.youtube.com/watch?v=xbbX7woE5Qg"),
        Problem("Stack", "Medium", "Min Stack", "https://www.youtube.com/watch?v=qkLl7nAwDPo&t=12s"),
        Problem("Stack", "Medium", "Evaluate Reverse Polish Notation", "https://www.youtube.com/watch?v=iu0082c4HDE"),
        Problem("Stack", "Medium", "Generate Parentheses", "https://www.youtube.com/watch?v=s9fokUqJ76A"),
        Problem("Stack", "Medium", "Daily Temperatures", "https://www.youtube.com/watch?v=cTBiBSnjO3c"),
        Problem("Stack", "Medium", "Car Fleet", "https://www.youtube.com/watch?v=Pr6T-3yB9RM"),
        Problem("Stack", "Hard", "Largest Rectangle in Histogram", "https://www.youtube.com/watch?v=zx5Sw9130L0"),
    ])

    # 4. Binary Search
    problems.extend([
        Problem("Binary Search", "Easy", "Binary Search", "https://www.youtube.com/watch?v=s4DPM8ct1pI"),
        Problem("Binary Search", "Medium", "Search a 2D Matrix", "https://www.youtube.com/watch?v=Ber2pi2C0j0"),
        Problem("Binary Search", "Medium", "Koko Eating Bananas", "https://www.youtube.com/watch?v=U2SozAs9RzA"),
        Problem("Binary Search", "Medium", "Find Minimum in Rotated Sorted Array", "https://www.youtube.com/watch?v=nIVW4P8b1VA"),
        Problem("Binary Search", "Medium", "Search in Rotated Sorted Array", "https://www.youtube.com/watch?v=U8XENwh8Oy8"),
        Problem("Binary Search", "Medium", "Time Based Key-Value Store", "https://www.youtube.com/watch?v=fu2cD_6E8Hw"),
        Problem("Binary Search", "Hard", "Median of Two Sorted Arrays", "https://www.youtube.com/watch?v=q6IEA26hvXc"),
    ])

    # 5. Sliding Window
    problems.extend([
        Problem("Sliding Window", "Easy", "Best Time to Buy and Sell Stock", "https://www.youtube.com/watch?v=1pkOgXD63yU"),
        Problem("Sliding Window", "Medium", "Longest Substring Without Repeating Characters", "https://www.youtube.com/watch?v=wiGpQwVHdE0"),
        Problem("Sliding Window", "Medium", "Longest Repeating Character Replacement", "https://www.youtube.com/watch?v=gqXU1UyA8pk"),
        Problem("Sliding Window", "Medium", "Permutation in String", "https://www.youtube.com/watch?v=UbyhOgBN834"),
        Problem("Sliding Window", "Hard", "Minimum Window Substring", "https://www.youtube.com/watch?v=jSto0O4AJbM"),
        Problem("Sliding Window", "Hard", "Sliding Window Maximum", "https://www.youtube.com/watch?v=DfljaUwZsOk"),
    ])

    # 6. Linked List
    problems.extend([
        Problem("Linked List", "Easy", "Reverse Linked List", "https://www.youtube.com/watch?v=G0_I-ZF0S38"),
        Problem("Linked List", "Easy", "Merge Two Sorted Lists", "https://www.youtube.com/watch?v=XIdigk956u0"),
        Problem("Linked List", "Easy", "Linked List Cycle", "https://www.youtube.com/watch?v=gBTe7lFR3vc"),
        Problem("Linked List", "Medium", "Reorder List", "https://www.youtube.com/watch?v=S5bfdUTrKLM"),
        Problem("Linked List", "Medium", "Remove Nth Node From End of List", "https://www.youtube.com/watch?v=XVuQxVej6y8"),
        Problem("Linked List", "Medium", "Copy List with Random Pointer", "https://www.youtube.com/watch?v=5Y2EiZST97Y"),
        Problem("Linked List", "Medium", "Add Two Numbers", "https://www.youtube.com/watch?v=wgFPrzTjm7s"),
        Problem("Linked List", "Medium", "Find the Duplicate Number", "https://www.youtube.com/watch?v=wjYnzkAhcNk"),
        Problem("Linked List", "Medium", "LRU Cache", "https://www.youtube.com/watch?v=7ABFKPK2hD4"),
        Problem("Linked List", "Hard", "Merge K Sorted Lists", "https://www.youtube.com/watch?v=q5a5OiGbT6Q"),
        Problem("Linked List", "Hard", "Reverse Nodes in k-Group", "https://www.youtube.com/watch?v=1UOPsfP85V4"),
    ])

    # 7. Trees
    problems.extend([
        Problem("Trees", "Easy", "Invert Binary Tree", "https://www.youtube.com/watch?v=OnSn2XEQ4MY"),
        Problem("Trees", "Easy", "Maximum Depth of Binary Tree", "https://www.youtube.com/watch?v=hTM3phVI6YQ"),
        Problem("Trees", "Easy", "Diameter of Binary Tree", "https://www.youtube.com/watch?v=bkxqA8Rfv04"),
        Problem("Trees", "Easy", "Balanced Binary Tree", "https://www.youtube.com/watch?v=QfJsau0ItOY"),
        Problem("Trees", "Easy", "Same Tree", "https://www.youtube.com/watch?v=vRbbcKXCxOw"),
        Problem("Trees", "Easy", "Subtree of Another Tree", "https://www.youtube.com/watch?v=E36O5SWp-LE"),
        Problem("Trees", "Medium", "Lowest Common Ancestor of a Binary Search Tree", "https://www.youtube.com/watch?v=gs2LMfuOR9k"),
        Problem("Trees", "Medium", "Binary Tree Level Order Traversal", "https://www.youtube.com/watch?v=6ZnyEApgFYg"),
        Problem("Trees", "Medium", "Binary Tree Right Side View", "https://www.youtube.com/watch?v=d4zLyf32e3I"),
        Problem("Trees", "Medium", "Count Good Nodes in Binary Tree", "https://www.youtube.com/watch?v=7cp5imvDzl4"),
        Problem("Trees", "Medium", "Validate Binary Search Tree", "https://www.youtube.com/watch?v=s6ATEkipzow"),
        Problem("Trees", "Medium", "Kth Smallest Element in a BST", "https://www.youtube.com/watch?v=5LUXSvjmGCw"),
        Problem("Trees", "Medium", "Construct Binary Tree from Preorder and Inorder Traversal", "https://www.youtube.com/watch?v=ihj4IQGZ2zc"),
        Problem("Trees", "Hard", "Binary Tree Maximum Path Sum", "https://www.youtube.com/watch?v=Hr5cWUld4vU"),
        Problem("Trees", "Hard", "Serialize and Deserialize Binary Tree", "https://www.youtube.com/watch?v=u4JAi2JJhI8"),
    ])

    # 8. Tries
    problems.extend([
        Problem("Tries", "Medium", "Implement Trie (Prefix Tree)", "https://www.youtube.com/watch?v=oobqoCJlHA0"),
        Problem("Tries", "Medium", "Design Add and Search Words Data Structure", "https://www.youtube.com/watch?v=BTf05gs_8iU"),
        Problem("Tries", "Hard", "Word Search II", "https://www.youtube.com/watch?v=asbcE9mZz_U"),
    ])

    # 9. Backtracking
    problems.extend([
        Problem("Backtracking", "Medium", "Subsets", "https://www.youtube.com/watch?v=REOH22Xwdkk"),
        Problem("Backtracking", "Medium", "Combination Sum", "https://www.youtube.com/watch?v=GBKI9VSKdGg"),
        Problem("Backtracking", "Medium", "Permutations", "https://www.youtube.com/watch?v=FZe0UqISmUw"),
        Problem("Backtracking", "Medium", "Subsets II", "https://www.youtube.com/watch?v=Vn2v6ajA7U0"),
        Problem("Backtracking", "Medium", "Combination Sum II", "https://www.youtube.com/watch?v=rSA3t6BDDwg"),
        Problem("Backtracking", "Medium", "Word Search", "https://www.youtube.com/watch?v=pfiQ_PS1g8E"),
        Problem("Backtracking", "Medium", "Palindrome Partitioning", "https://www.youtube.com/watch?v=3jvWodd7ht0"),
        Problem("Backtracking", "Medium", "Letter Combinations of a Phone Number", "https://www.youtube.com/watch?v=0snEunUacZY"),
        Problem("Backtracking", "Hard", "N-Queens", "https://www.youtube.com/watch?v=Ph95IHmRp5M"),
    ])

    # 10. Heap / Priority Queue
    problems.extend([
        Problem("Heap / Priority Queue", "Easy", "Kth Largest Element in a Stream", "https://www.youtube.com/watch?v=hOjcdrqMoQ8"),
        Problem("Heap / Priority Queue", "Easy", "Last Stone Weight", "https://www.youtube.com/watch?v=B-QCq79-Vfw"),
        Problem("Heap / Priority Queue", "Medium", "K Closest Points to Origin", "https://www.youtube.com/watch?v=rI2EBUEMfTk"),
        Problem("Heap / Priority Queue", "Medium", "Kth Largest Element in an Array", "https://www.youtube.com/watch?v=XEmy13g1Qxc"),
        Problem("Heap / Priority Queue", "Medium", "Task Scheduler", "https://www.youtube.com/watch?v=s8p8ukTyA2I"),
        Problem("Heap / Priority Queue", "Medium", "Design Twitter", "https://www.youtube.com/watch?v=pNichitDD2E"),
        Problem("Heap / Priority Queue", "Hard", "Find Median from Data Stream", "https://www.youtube.com/watch?v=itmhHWaHupI"),
    ])

    # 11. Graphs
    problems.extend([
        Problem("Graphs", "Medium", "Number of Islands", "https://www.youtube.com/watch?v=pV2kpPD66nE"),
        Problem("Graphs", "Medium", "Clone Graph", "https://www.youtube.com/watch?v=mQeF6bN8hMk"),
        Problem("Graphs", "Medium", "Max Area of Island", "https://www.youtube.com/watch?v=W8VuDt0eb5c"),
        Problem("Graphs", "Medium", "Pacific Atlantic Water Flow", "https://www.youtube.com/watch?v=s-VkcjHqkGI"),
        Problem("Graphs", "Medium", "Surrounded Regions", "https://www.youtube.com/watch?v=9z2BunfoZ5Y"),
        Problem("Graphs", "Medium", "Rotting Oranges", "https://www.youtube.com/watch?v=y704fEOx0s0"),
        Problem("Graphs", "Medium", "Walls and Gates", "https://www.youtube.com/watch?v=e69C6xhiSQE"),
        Problem("Graphs", "Medium", "Course Schedule", "https://www.youtube.com/watch?v=EgI5nU9etnU"),
        Problem("Graphs", "Medium", "Course Schedule II", "https://www.youtube.com/watch?v=Akt3glAwyfY"),
        Problem("Graphs", "Medium", "Redundant Connection", "https://www.youtube.com/watch?v=FXWRE67PLL0"),
        Problem("Graphs", "Medium", "Number of Connected Components in an Undirected Graph", "https://www.youtube.com/watch?v=8f1XPm4WOUc"),
        Problem("Graphs", "Medium", "Graph Valid Tree", "https://www.youtube.com/watch?v=bXsUuownnoQ"),
        Problem("Graphs", "Hard", "Word Ladder", "https://www.youtube.com/watch?v=h9iTnkgv05E"),
    ])

    # 12. Advanced Graphs
    problems.extend([
        Problem("Advanced Graphs", "Medium", "Reconstruct Itinerary", "https://www.youtube.com/watch?v=ZyB_gQ8vqGA"),
        Problem("Advanced Graphs", "Medium", "Min Cost to Connect All Points", "https://www.youtube.com/watch?v=f7JOBJIC-NA"),
        Problem("Advanced Graphs", "Medium", "Network Delay Time", "https://www.youtube.com/watch?v=EaphyqKU4PQ"),
        Problem("Advanced Graphs", "Medium", "Swim in Rising Water", "https://www.youtube.com/watch?v=amvrKlMLuGY"),
        Problem("Advanced Graphs", "Hard", "Alien Dictionary", "https://www.youtube.com/watch?v=6kTZYvNNyps"),
        Problem("Advanced Graphs", "Hard", "Cheapest Flights Within K Stops", "https://www.youtube.com/watch?v=5eIK3zUdYmE"),
    ])

    # 13. 1-D Dynamic Programming
    problems.extend([
        Problem("1-D Dynamic Programming", "Easy", "Climbing Stairs", "https://www.youtube.com/watch?v=Y0lT9Fck7qI"),
        Problem("1-D Dynamic Programming", "Easy", "Min Cost Climbing Stairs", "https://www.youtube.com/watch?v=ktmzAZWkEZ0"),
        Problem("1-D Dynamic Programming", "Medium", "House Robber", "https://www.youtube.com/watch?v=73r3KWiEvyk"),
        Problem("1-D Dynamic Programming", "Medium", "House Robber II", "https://www.youtube.com/watch?v=rWAJCfYYOvM"),
        Problem("1-D Dynamic Programming", "Medium", "Longest Palindromic Substring", "https://www.youtube.com/watch?v=XYQecbcd6_c"),
        Problem("1-D Dynamic Programming", "Medium", "Palindromic Substrings", "https://www.youtube.com/watch?v=4RACzI5-du8"),
        Problem("1-D Dynamic Programming", "Medium", "Decode Ways", "https://www.youtube.com/watch?v=6aEyTjOwlJU"),
        Problem("1-D Dynamic Programming", "Medium", "Coin Change", "https://www.youtube.com/watch?v=H9bfqozjoqs"),
        Problem("1-D Dynamic Programming", "Medium", "Maximum Product Subarray", "https://www.youtube.com/watch?v=lXVy6YWFcRM"),
        Problem("1-D Dynamic Programming", "Medium", "Word Break", "https://www.youtube.com/watch?v=Sx9NNgInc3A"),
        Problem("1-D Dynamic Programming", "Medium", "Longest Increasing Subsequence", "https://www.youtube.com/watch?v=cjWnW0hdF1Y"),
        Problem("1-D Dynamic Programming", "Medium", "Partition Equal Subset Sum", "https://www.youtube.com/watch?v=IsvocB5BJhw"),
    ])

    # 14. 2-D Dynamic Programming
    problems.extend([
        Problem("2-D Dynamic Programming", "Medium", "Unique Paths", "https://www.youtube.com/watch?v=IlEsdxuD4lY"),
        Problem("2-D Dynamic Programming", "Medium", "Longest Common Subsequence", "https://www.youtube.com/watch?v=Ua0GhsJSlWM"),
        Problem("2-D Dynamic Programming", "Medium", "Best Time to Buy and Sell Stock With Cooldown", "https://www.youtube.com/watch?v=I7j0F7AHpb8"),
        Problem("2-D Dynamic Programming", "Medium", "Coin Change II", "https://www.youtube.com/watch?v=Mjy4hd2xgrs"),
        Problem("2-D Dynamic Programming", "Medium", "Target Sum", "https://www.youtube.com/watch?v=g0npyaQtAQM"),
        Problem("2-D Dynamic Programming", "Medium", "Interleaving String", "https://www.youtube.com/watch?v=3Rw3p9LrgvE"),
        Problem("2-D Dynamic Programming", "Hard", "Longest Increasing Path in a Matrix", "https://www.youtube.com/watch?v=wCc_nd-GiEc"),
        Problem("2-D Dynamic Programming", "Hard", "Distinct Subsequences", "https://www.youtube.com/watch?v=-RDzMJ33nx8"),
        Problem("2-D Dynamic Programming", "Hard", "Edit Distance", "https://www.youtube.com/watch?v=XYi2-LPrwm4"),
        Problem("2-D Dynamic Programming", "Hard", "Burst Balloons", "https://www.youtube.com/watch?v=VFskby7lUbw"),
        Problem("2-D Dynamic Programming", "Hard", "Regular Expression Matching", "https://www.youtube.com/watch?v=HAA8mgxlov8"),
    ])

    # 15. Greedy
    problems.extend([
        Problem("Greedy", "Medium", "Maximum Subarray", "https://www.youtube.com/watch?v=5WZl3MMT0Eg"),
        Problem("Greedy", "Medium", "Jump Game", "https://www.youtube.com/watch?v=Yan0cv2cLy8"),
        Problem("Greedy", "Medium", "Jump Game II", "https://www.youtube.com/watch?v=dJ7sWiOoK7g"),
        Problem("Greedy", "Medium", "Gas Station", "https://www.youtube.com/watch?v=lJwbPZGo05A"),
        Problem("Greedy", "Medium", "Hand of Straights", "https://www.youtube.com/watch?v=amnrMCVd2YI"),
        Problem("Greedy", "Medium", "Merge Triplets to Form Target Triplet", "https://www.youtube.com/watch?v=kShkQLQZ9K4"),
        Problem("Greedy", "Medium", "Partition Labels", "https://www.youtube.com/watch?v=B7m8UmZE-vw"),
        Problem("Greedy", "Medium", "Valid Parenthesis String", "https://www.youtube.com/watch?v=QhPdNS143Qg"),
    ])

    # 16. Intervals
    problems.extend([
        Problem("Intervals", "Easy", "Meeting Rooms", "https://www.youtube.com/watch?v=PaJxqZVPhbg"),
        Problem("Intervals", "Medium", "Insert Interval", "https://www.youtube.com/watch?v=A8NUOmlwOlM"),
        Problem("Intervals", "Medium", "Merge Intervals", "https://www.youtube.com/watch?v=44H3cEC2fFM"),
        Problem("Intervals", "Medium", "Non-overlapping Intervals", "https://www.youtube.com/watch?v=nONCGxWoUfM"),
        Problem("Intervals", "Medium", "Meeting Rooms II", "https://www.youtube.com/watch?v=FdzJmTCVyJU"),
        Problem("Intervals", "Hard", "Minimum Interval to Include Each Query", "https://www.youtube.com/watch?v=5hQ5WWW5awQ"),
    ])

    # 17. Math & Geometry
    problems.extend([
        Problem("Math & Geometry", "Easy", "Happy Number", "https://www.youtube.com/watch?v=ljz85bxOYJ0"),
        Problem("Math & Geometry", "Easy", "Plus One", "https://www.youtube.com/watch?v=jIaA8boiG1s"),
        Problem("Math & Geometry", "Medium", "Rotate Image", "https://www.youtube.com/watch?v=fMSJSS7eO1w"),
        Problem("Math & Geometry", "Medium", "Spiral Matrix", "https://www.youtube.com/watch?v=BJnMZNwUk1M"),
        Problem("Math & Geometry", "Medium", "Set Matrix Zeroes", "https://www.youtube.com/watch?v=T41rL0L3Pnw"),
        Problem("Math & Geometry", "Medium", "Pow(x, n)", "https://www.youtube.com/watch?v=g9YQyYi4IQQ"),
        Problem("Math & Geometry", "Medium", "Multiply Strings", "https://www.youtube.com/watch?v=1vZswirL8Y8"),
        Problem("Math & Geometry", "Medium", "Detect Squares", "https://www.youtube.com/watch?v=bahebearrDc"),
    ])

    # 18. Bit Manipulation
    problems.extend([
        Problem("Bit Manipulation", "Easy", "Single Number", "https://www.youtube.com/watch?v=qMPX1AOa83k"),
        Problem("Bit Manipulation", "Easy", "Number of 1 Bits", "https://www.youtube.com/watch?v=5Km3utixwZs"),
        Problem("Bit Manipulation", "Easy", "Counting Bits", "https://www.youtube.com/watch?v=RyBM56RIWrM"),
        Problem("Bit Manipulation", "Easy", "Reverse Bits", "https://www.youtube.com/watch?v=UcoN6UjAI64"),
        Problem("Bit Manipulation", "Easy", "Missing Number", "https://www.youtube.com/watch?v=WnPLSRLSANE"),
        Problem("Bit Manipulation", "Medium", "Sum of Two Integers", "https://www.youtube.com/watch?v=gVUrDV4tZfY"),
        Problem("Bit Manipulation", "Medium", "Reverse Integer", "https://www.youtube.com/watch?v=HAgLH58IgJQ"),
    ])

    # Add problems to their respective categories
    for problem in problems:
        categories[problem.category].add_problem(problem)

    # FIX: return categories? or problems
    return categories
