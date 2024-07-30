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

    ARRAYS_AND_HASHING = "Arrays and Hashing"
    TWO_POINTERS = "Two Pointers"
    STACK = "Stack"
    BINARY_SEARCH = "Binary Search"
    SLIDING_WINDOW = "Sliding Window"
    LINKED_LIST = "Linked List"
    TREES = "Trees"
    TRIES = "Tries"
    BACKTRACKING = "Backtracking"
    HEAP_PRIORITY_QUEUE = "Heap or Priority Queue"
    GRAPHS = "Graphs"
    ADVANCED_GRAPHS = "Advanced Graphs"
    ONE_D_DP = "1-D Dynamic Programming"
    TWO_D_DP = "2-D Dynamic Programming"
    GREEDY = "Greedy"
    INTERVALS = "Intervals"
    MATH_AND_GEOMETRY = "Math and Geometry"
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
        Problem("Arrays and Hashing", "Easy", "Contains Duplicate", "https://www.youtube.com/watch?v=3OamzN90kPg", "https://leetcode.com/problems/contains-duplicate"),
        Problem("Arrays and Hashing", "Easy", "Valid Anagram", "https://www.youtube.com/watch?v=9UtInBqnCgA", "https://leetcode.com/problems/valid-anagram"),
        Problem("Arrays and Hashing", "Easy", "Two Sum", "https://www.youtube.com/watch?v=KLlXCFG5TnA", "https://leetcode.com/problems/two-sum"),
        Problem("Arrays and Hashing", "Medium", "Group Anagrams", "https://www.youtube.com/watch?v=vzdNOK2oB2E", "https://leetcode.com/problems/group-anagrams"),
        Problem("Arrays and Hashing", "Medium", "Top K Frequent Elements", "https://www.youtube.com/watch?v=YPTqKIgVk-k", "https://leetcode.com/problems/top-k-frequent-elements"),
        Problem("Arrays and Hashing", "Medium", "Product of Array Except Self", "https://www.youtube.com/watch?v=bNvIQI2wAjk", "https://leetcode.com/problems/product-of-array-except-self"),
        Problem("Arrays and Hashing", "Medium", "Valid Sudoku", "https://www.youtube.com/watch?v=TjFXEUCMqI8", "https://leetcode.com/problems/valid-sudoku"),
        Problem("Arrays and Hashing", "Medium", "Encode and Decode Strings", "https://www.youtube.com/watch?v=B1k_sxOSgv8", "https://leetcode.com/problems/encode-and-decode-strings"),
        Problem("Arrays and Hashing", "Medium", "Longest Consecutive Sequence", "https://www.youtube.com/watch?v=P6RZZMu_maU", "https://leetcode.com/problems/longest-consecutive-sequence"),
    ])

    # 2. Two Pointers
    problems.extend([
        Problem("Two Pointers", "Easy", "Valid Palindrome", "https://www.youtube.com/watch?v=jJXJ16kPFWg", "https://leetcode.com/problems/valid-palindrome"),
        Problem("Two Pointers", "Medium", "Two Sum II - Input Array Is Sorted", "https://www.youtube.com/watch?v=cQ1Oz4ckceM", "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted"),
        Problem("Two Pointers", "Medium", "3Sum", "https://www.youtube.com/watch?v=jzZsG8n2R9A", "https://leetcode.com/problems/3sum"),
        Problem("Two Pointers", "Medium", "Container With Most Water", "https://www.youtube.com/watch?v=UuiTKBwPgAo", "https://leetcode.com/problems/container-with-most-water"),
        Problem("Two Pointers", "Hard", "Trapping Rain Water", "https://www.youtube.com/watch?v=ZI2z5pq0TqA", "https://leetcode.com/problems/trapping-rain-water"),
    ])

    # 3. Stack
    problems.extend([
        Problem("Stack", "Easy", "Valid Parentheses", "https://www.youtube.com/watch?v=xbbX7woE5Qg", "https://leetcode.com/problems/valid-parentheses"),
        Problem("Stack", "Medium", "Min Stack", "https://www.youtube.com/watch?v=qkLl7nAwDPoandt=12s", "https://leetcode.com/problems/min-stack"),
        Problem("Stack", "Medium", "Evaluate Reverse Polish Notation", "https://www.youtube.com/watch?v=iu0082c4HDE", "https://leetcode.com/problems/evaluate-reverse-polish-notation"),
        Problem("Stack", "Medium", "Generate Parentheses", "https://www.youtube.com/watch?v=s9fokUqJ76A", "https://leetcode.com/problems/generate-parentheses"),
        Problem("Stack", "Medium", "Daily Temperatures", "https://www.youtube.com/watch?v=cTBiBSnjO3c", "https://leetcode.com/problems/daily-temperatures"),
        Problem("Stack", "Medium", "Car Fleet", "https://www.youtube.com/watch?v=Pr6T-3yB9RM", "https://leetcode.com/problems/car-fleet"),
        Problem("Stack", "Hard", "Largest Rectangle in Histogram", "https://www.youtube.com/watch?v=zx5Sw9130L0", "https://leetcode.com/problems/largest-rectangle-in-histogram"),
    ])

    # 4. Binary Search
    problems.extend([
        Problem("Binary Search", "Easy", "Binary Search", "https://www.youtube.com/watch?v=s4DPM8ct1pI", "https://leetcode.com/problems/binary-search"),
        Problem("Binary Search", "Medium", "Search a 2D Matrix", "https://www.youtube.com/watch?v=Ber2pi2C0j0", "https://leetcode.com/problems/search-a-2d-matrix"),
        Problem("Binary Search", "Medium", "Koko Eating Bananas", "https://www.youtube.com/watch?v=U2SozAs9RzA", "https://leetcode.com/problems/koko-eating-bananas"),
        Problem("Binary Search", "Medium", "Find Minimum in Rotated Sorted Array", "https://www.youtube.com/watch?v=nIVW4P8b1VA", "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array"),
        Problem("Binary Search", "Medium", "Search in Rotated Sorted Array", "https://www.youtube.com/watch?v=U8XENwh8Oy8", "https://leetcode.com/problems/search-in-rotated-sorted-array"),
        Problem("Binary Search", "Medium", "Time Based Key-Value Store", "https://www.youtube.com/watch?v=fu2cD_6E8Hw", "https://leetcode.com/problems/time-based-key-value-store"),
        Problem("Binary Search", "Hard", "Median of Two Sorted Arrays", "https://www.youtube.com/watch?v=q6IEA26hvXc", "https://leetcode.com/problems/median-of-two-sorted-arrays"),
    ])

    # 5. Sliding Window
    problems.extend([
        Problem("Sliding Window", "Easy", "Best Time to Buy and Sell Stock", "https://www.youtube.com/watch?v=1pkOgXD63yU", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock"),
        Problem("Sliding Window", "Medium", "Longest Substring Without Repeating Characters", "https://www.youtube.com/watch?v=wiGpQwVHdE0", "https://leetcode.com/problems/longest-substring-without-repeating-characters"),
        Problem("Sliding Window", "Medium", "Longest Repeating Character Replacement", "https://www.youtube.com/watch?v=gqXU1UyA8pk", "https://leetcode.com/problems/longest-repeating-character-replacement"),
        Problem("Sliding Window", "Medium", "Permutation in String", "https://www.youtube.com/watch?v=UbyhOgBN834", "https://leetcode.com/problems/permutation-in-string"),
        Problem("Sliding Window", "Hard", "Minimum Window Substring", "https://www.youtube.com/watch?v=jSto0O4AJbM", "https://leetcode.com/problems/minimum-window-substring"),
        Problem("Sliding Window", "Hard", "Sliding Window Maximum", "https://www.youtube.com/watch?v=DfljaUwZsOk", "https://leetcode.com/problems/sliding-window-maximum"),
    ])

    # 6. Linked List
    problems.extend([
        Problem("Linked List", "Easy", "Reverse Linked List", "https://www.youtube.com/watch?v=G0_I-ZF0S38", "https://leetcode.com/problems/reverse-linked-list"),
        Problem("Linked List", "Easy", "Merge Two Sorted Lists", "https://www.youtube.com/watch?v=XIdigk956u0", "https://leetcode.com/problems/merge-two-sorted-lists"),
        Problem("Linked List", "Easy", "Linked List Cycle", "https://www.youtube.com/watch?v=gBTe7lFR3vc", "https://leetcode.com/problems/linked-list-cycle"),
        Problem("Linked List", "Medium", "Reorder List", "https://www.youtube.com/watch?v=S5bfdUTrKLM", "https://leetcode.com/problems/reorder-list"),
        Problem("Linked List", "Medium", "Remove Nth Node From End of List", "https://www.youtube.com/watch?v=XVuQxVej6y8", "https://leetcode.com/problems/remove-nth-node-from-end-of-list"),
        Problem("Linked List", "Medium", "Copy List with Random Pointer", "https://www.youtube.com/watch?v=5Y2EiZST97Y", "https://leetcode.com/problems/copy-list-with-random-pointer"),
        Problem("Linked List", "Medium", "Add Two Numbers", "https://www.youtube.com/watch?v=wgFPrzTjm7s", "https://leetcode.com/problems/add-two-numbers"),
        Problem("Linked List", "Medium", "Find the Duplicate Number", "https://www.youtube.com/watch?v=wjYnzkAhcNk", "https://leetcode.com/problems/find-the-duplicate-number"),
        Problem("Linked List", "Medium", "LRU Cache", "https://www.youtube.com/watch?v=7ABFKPK2hD4", "https://leetcode.com/problems/lru-cache"),
        Problem("Linked List", "Hard", "Merge K Sorted Lists", "https://www.youtube.com/watch?v=q5a5OiGbT6Q", "https://leetcode.com/problems/merge-k-sorted-lists"),
        Problem("Linked List", "Hard", "Reverse Nodes in k-Group", "https://www.youtube.com/watch?v=1UOPsfP85V4", "https://leetcode.com/problems/reverse-nodes-in-k-group"),
    ])

    # 7. Trees
    problems.extend([
        Problem("Trees", "Easy", "Invert Binary Tree", "https://www.youtube.com/watch?v=OnSn2XEQ4MY", "https://leetcode.com/problems/invert-binary-tree"),
        Problem("Trees", "Easy", "Maximum Depth of Binary Tree", "https://www.youtube.com/watch?v=hTM3phVI6YQ", "https://leetcode.com/problems/maximum-depth-of-binary-tree"),
        Problem("Trees", "Easy", "Diameter of Binary Tree", "https://www.youtube.com/watch?v=bkxqA8Rfv04", "https://leetcode.com/problems/diameter-of-binary-tree"),
        Problem("Trees", "Easy", "Balanced Binary Tree", "https://www.youtube.com/watch?v=QfJsau0ItOY", "https://leetcode.com/problems/balanced-binary-tree"),
        Problem("Trees", "Easy", "Same Tree", "https://www.youtube.com/watch?v=vRbbcKXCxOw", "https://leetcode.com/problems/same-tree"),
        Problem("Trees", "Easy", "Subtree of Another Tree", "https://www.youtube.com/watch?v=E36O5SWp-LE", "https://leetcode.com/problems/subtree-of-another-tree"),
        Problem("Trees", "Medium", "Lowest Common Ancestor of a Binary Search Tree", "https://www.youtube.com/watch?v=gs2LMfuOR9k", "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree"),
        Problem("Trees", "Medium", "Binary Tree Level Order Traversal", "https://www.youtube.com/watch?v=6ZnyEApgFYg", "https://leetcode.com/problems/binary-tree-level-order-traversal"),
        Problem("Trees", "Medium", "Binary Tree Right Side View", "https://www.youtube.com/watch?v=d4zLyf32e3I", "https://leetcode.com/problems/binary-tree-right-side-view"),
        Problem("Trees", "Medium", "Count Good Nodes in Binary Tree", "https://www.youtube.com/watch?v=7cp5imvDzl4", "https://leetcode.com/problems/count-good-nodes-in-binary-tree"),
        Problem("Trees", "Medium", "Validate Binary Search Tree", "https://www.youtube.com/watch?v=s6ATEkipzow", "https://leetcode.com/problems/validate-binary-search-tree"),
        Problem("Trees", "Medium", "Kth Smallest Element in a BST", "https://www.youtube.com/watch?v=5LUXSvjmGCw", "https://leetcode.com/problems/kth-smallest-element-in-a-bst"),
        Problem("Trees", "Medium", "Construct Binary Tree from Preorder and Inorder Traversal", "https://www.youtube.com/watch?v=ihj4IQGZ2zc", "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal"),
        Problem("Trees", "Hard", "Binary Tree Maximum Path Sum", "https://www.youtube.com/watch?v=Hr5cWUld4vU", "https://leetcode.com/problems/binary-tree-maximum-path-sum"),
        Problem("Trees", "Hard", "Serialize and Deserialize Binary Tree", "https://www.youtube.com/watch?v=u4JAi2JJhI8", "https://leetcode.com/problems/serialize-and-deserialize-binary-tree"),
    ])

    # 8. Tries
    problems.extend([
        Problem("Tries", "Medium", "Implement Trie (Prefix Tree)", "https://www.youtube.com/watch?v=oobqoCJlHA0", "https://leetcode.com/problems/implement-trie-prefix-tree"),
        Problem("Tries", "Medium", "Design Add and Search Words Data Structure", "https://www.youtube.com/watch?v=BTf05gs_8iU", "https://leetcode.com/problems/design-add-and-search-words-data-structure"),
        Problem("Tries", "Hard", "Word Search II", "https://www.youtube.com/watch?v=asbcE9mZz_U", "https://leetcode.com/problems/word-search-ii"),
    ])

    # 9. Backtracking (continued)
    problems.extend([
        Problem("Backtracking", "Medium", "Subsets", "https://www.youtube.com/watch?v=REOH22Xwdkk", "https://leetcode.com/problems/subsets"),
        Problem("Backtracking", "Medium", "Combination Sum", "https://www.youtube.com/watch?v=GBKI9VSKdGg", "https://leetcode.com/problems/combination-sum"),
        Problem("Backtracking", "Medium", "Permutations", "https://www.youtube.com/watch?v=FZe0UqISmUw", "https://leetcode.com/problems/permutations"),
        Problem("Backtracking", "Medium", "Subsets II", "https://www.youtube.com/watch?v=Vn2v6ajA7U0", "https://leetcode.com/problems/subsets-ii"),
        Problem("Backtracking", "Medium", "Combination Sum II", "https://www.youtube.com/watch?v=rSA3t6BDDwg", "https://leetcode.com/problems/combination-sum-ii"),
        Problem("Backtracking", "Medium", "Word Search", "https://www.youtube.com/watch?v=pfiQ_PS1g8E", "https://leetcode.com/problems/word-search"),
        Problem("Backtracking", "Medium", "Palindrome Partitioning", "https://www.youtube.com/watch?v=3jvWodd7ht0", "https://leetcode.com/problems/palindrome-partitioning"),
        Problem("Backtracking", "Medium", "Letter Combinations of a Phone Number", "https://www.youtube.com/watch?v=0snEunUacZY", "https://leetcode.com/problems/letter-combinations-of-a-phone-number"),
        Problem("Backtracking", "Hard", "N-Queens", "https://www.youtube.com/watch?v=Ph95IHmRp5M", "https://leetcode.com/problems/n-queens"),
    ])

    # 10. Heap / Priority Queue
    problems.extend([
        Problem("Heap or Priority Queue", "Easy", "Kth Largest Element in a Stream", "https://www.youtube.com/watch?v=hOjcdrqMoQ8", "https://leetcode.com/problems/kth-largest-element-in-a-stream"),
        Problem("Heap or Priority Queue", "Easy", "Last Stone Weight", "https://www.youtube.com/watch?v=B-QCq79-Vfw", "https://leetcode.com/problems/last-stone-weight"),
        Problem("Heap or Priority Queue", "Medium", "K Closest Points to Origin", "https://www.youtube.com/watch?v=rI2EBUEMfTk", "https://leetcode.com/problems/k-closest-points-to-origin"),
        Problem("Heap or Priority Queue", "Medium", "Kth Largest Element in an Array", "https://www.youtube.com/watch?v=XEmy13g1Qxc", "https://leetcode.com/problems/kth-largest-element-in-an-array"),
        Problem("Heap or Priority Queue", "Medium", "Task Scheduler", "https://www.youtube.com/watch?v=s8p8ukTyA2I", "https://leetcode.com/problems/task-scheduler"),
        Problem("Heap or Priority Queue", "Medium", "Design Twitter", "https://www.youtube.com/watch?v=pNichitDD2E", "https://leetcode.com/problems/design-twitter"),
        Problem("Heap or Priority Queue", "Hard", "Find Median from Data Stream", "https://www.youtube.com/watch?v=itmhHWaHupI", "https://leetcode.com/problems/find-median-from-data-stream"),
    ])

    # 11. Graphs
    problems.extend([
        Problem("Graphs", "Medium", "Number of Islands", "https://www.youtube.com/watch?v=pV2kpPD66nE", "https://leetcode.com/problems/number-of-islands"),
        Problem("Graphs", "Medium", "Clone Graph", "https://www.youtube.com/watch?v=mQeF6bN8hMk", "https://leetcode.com/problems/clone-graph"),
        Problem("Graphs", "Medium", "Max Area of Island", "https://www.youtube.com/watch?v=W8VuDt0eb5c", "https://leetcode.com/problems/max-area-of-island"),
        Problem("Graphs", "Medium", "Pacific Atlantic Water Flow", "https://www.youtube.com/watch?v=s-VkcjHqkGI", "https://leetcode.com/problems/pacific-atlantic-water-flow"),
        Problem("Graphs", "Medium", "Surrounded Regions", "https://www.youtube.com/watch?v=9z2BunfoZ5Y", "https://leetcode.com/problems/surrounded-regions"),
        Problem("Graphs", "Medium", "Rotting Oranges", "https://www.youtube.com/watch?v=y704fEOx0s0", "https://leetcode.com/problems/rotting-oranges"),
        Problem("Graphs", "Medium", "Walls and Gates", "https://www.youtube.com/watch?v=e69C6xhiSQE", "https://leetcode.com/problems/walls-and-gates"),
        Problem("Graphs", "Medium", "Course Schedule", "https://www.youtube.com/watch?v=EgI5nU9etnU", "https://leetcode.com/problems/course-schedule"),
        Problem("Graphs", "Medium", "Course Schedule II", "https://www.youtube.com/watch?v=Akt3glAwyfY", "https://leetcode.com/problems/course-schedule-ii"),
        Problem("Graphs", "Medium", "Redundant Connection", "https://www.youtube.com/watch?v=FXWRE67PLL0", "https://leetcode.com/problems/redundant-connection"),
        Problem("Graphs", "Medium", "Number of Connected Components in an Undirected Graph", "https://www.youtube.com/watch?v=8f1XPm4WOUc", "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph"),
        Problem("Graphs", "Medium", "Graph Valid Tree", "https://www.youtube.com/watch?v=bXsUuownnoQ", "https://leetcode.com/problems/graph-valid-tree"),
        Problem("Graphs", "Hard", "Word Ladder", "https://www.youtube.com/watch?v=h9iTnkgv05E", "https://leetcode.com/problems/word-ladder"),
    ])

    # 12. Advanced Graphs
    problems.extend([
        Problem("Advanced Graphs", "Medium", "Reconstruct Itinerary", "https://www.youtube.com/watch?v=ZyB_gQ8vqGA", "https://leetcode.com/problems/reconstruct-itinerary"),
        Problem("Advanced Graphs", "Medium", "Min Cost to Connect All Points", "https://www.youtube.com/watch?v=f7JOBJIC-NA", "https://leetcode.com/problems/min-cost-to-connect-all-points"),
        Problem("Advanced Graphs", "Medium", "Network Delay Time", "https://www.youtube.com/watch?v=EaphyqKU4PQ", "https://leetcode.com/problems/network-delay-time"),
        Problem("Advanced Graphs", "Hard", "Swim in Rising Water", "https://www.youtube.com/watch?v=amvrKlMLuGY", "https://leetcode.com/problems/swim-in-rising-water"),
        Problem("Advanced Graphs", "Hard", "Alien Dictionary", "https://www.youtube.com/watch?v=6kTZYvNNyps", "https://leetcode.com/problems/alien-dictionary"),
        Problem("Advanced Graphs", "Hard", "Cheapest Flights Within K Stops", "https://www.youtube.com/watch?v=5eIK3zUdYmE", "https://leetcode.com/problems/cheapest-flights-within-k-stops"),
    ])

    # 13. 1-D Dynamic Programming
    problems.extend([
        Problem("1-D Dynamic Programming", "Easy", "Climbing Stairs", "https://www.youtube.com/watch?v=Y0lT9Fck7qI", "https://leetcode.com/problems/climbing-stairs"),
        Problem("1-D Dynamic Programming", "Easy", "Min Cost Climbing Stairs", "https://www.youtube.com/watch?v=ktmzAZWkEZ0", "https://leetcode.com/problems/min-cost-climbing-stairs"),
        Problem("1-D Dynamic Programming", "Medium", "House Robber", "https://www.youtube.com/watch?v=73r3KWiEvyk", "https://leetcode.com/problems/house-robber"),
        Problem("1-D Dynamic Programming", "Medium", "House Robber II", "https://www.youtube.com/watch?v=rWAJCfYYOvM", "https://leetcode.com/problems/house-robber-ii"),
        Problem("1-D Dynamic Programming", "Medium", "Longest Palindromic Substring", "https://www.youtube.com/watch?v=XYQecbcd6_c", "https://leetcode.com/problems/longest-palindromic-substring"),
        Problem("1-D Dynamic Programming", "Medium", "Palindromic Substrings", "https://www.youtube.com/watch?v=4RACzI5-du8", "https://leetcode.com/problems/palindromic-substrings"),
        Problem("1-D Dynamic Programming", "Medium", "Decode Ways", "https://www.youtube.com/watch?v=6aEyTjOwlJU", "https://leetcode.com/problems/decode-ways"),
        Problem("1-D Dynamic Programming", "Medium", "Coin Change", "https://www.youtube.com/watch?v=H9bfqozjoqs", "https://leetcode.com/problems/coin-change"),
        Problem("1-D Dynamic Programming", "Medium", "Maximum Product Subarray", "https://www.youtube.com/watch?v=lXVy6YWFcRM", "https://leetcode.com/problems/maximum-product-subarray"),
        Problem("1-D Dynamic Programming", "Medium", "Word Break", "https://www.youtube.com/watch?v=Sx9NNgInc3A", "https://leetcode.com/problems/word-break"),
        Problem("1-D Dynamic Programming", "Medium", "Longest Increasing Subsequence", "https://www.youtube.com/watch?v=cjWnW0hdF1Y", "https://leetcode.com/problems/longest-increasing-subsequence"),
        Problem("1-D Dynamic Programming", "Medium", "Partition Equal Subset Sum", "https://www.youtube.com/watch?v=IsvocB5BJhw", "https://leetcode.com/problems/partition-equal-subset-sum"),
    ])

    # 14. 2-D Dynamic Programming
    problems.extend([
        Problem("2-D Dynamic Programming", "Medium", "Unique Paths", "https://www.youtube.com/watch?v=IlEsdxuD4lY", "https://leetcode.com/problems/unique-paths"),
        Problem("2-D Dynamic Programming", "Medium", "Longest Common Subsequence", "https://www.youtube.com/watch?v=Ua0GhsJSlWM", "https://leetcode.com/problems/longest-common-subsequence"),
        Problem("2-D Dynamic Programming", "Medium", "Best Time to Buy and Sell Stock With Cooldown", "https://www.youtube.com/watch?v=I7j0F7AHpb8", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown"),
        Problem("2-D Dynamic Programming", "Medium", "Coin Change II", "https://www.youtube.com/watch?v=Mjy4hd2xgrs", "https://leetcode.com/problems/coin-change-ii"),
        Problem("2-D Dynamic Programming", "Medium", "Target Sum", "https://www.youtube.com/watch?v=g0npyaQtAQM", "https://leetcode.com/problems/target-sum"),
        Problem("2-D Dynamic Programming", "Medium", "Interleaving String", "https://www.youtube.com/watch?v=3Rw3p9LrgvE", "https://leetcode.com/problems/interleaving-string"),
        Problem("2-D Dynamic Programming", "Hard", "Longest Increasing Path in a Matrix", "https://www.youtube.com/watch?v=wCc_nd-GiEc", "https://leetcode.com/problems/longest-increasing-path-in-a-matrix"),
        Problem("2-D Dynamic Programming", "Hard", "Distinct Subsequences", "https://www.youtube.com/watch?v=-RDzMJ33nx8", "https://leetcode.com/problems/distinct-subsequences"),
        Problem("2-D Dynamic Programming", "Hard", "Edit Distance", "https://www.youtube.com/watch?v=XYi2-LPrwm4", "https://leetcode.com/problems/edit-distance"),
        Problem("2-D Dynamic Programming", "Hard", "Burst Balloons", "https://www.youtube.com/watch?v=VFskby7lUbw", "https://leetcode.com/problems/burst-balloons"),
        Problem("2-D Dynamic Programming", "Hard", "Regular Expression Matching", "https://www.youtube.com/watch?v=HAA8mgxlov8", "https://leetcode.com/problems/regular-expression-matching"),
    ])

    # 15. Greedy
    problems.extend([
        Problem("Greedy", "Medium", "Maximum Subarray", "https://www.youtube.com/watch?v=5WZl3MMT0Eg", "https://leetcode.com/problems/maximum-subarray"),
        Problem("Greedy", "Medium", "Jump Game", "https://www.youtube.com/watch?v=Yan0cv2cLy8", "https://leetcode.com/problems/jump-game"),
        Problem("Greedy", "Medium", "Jump Game II", "https://www.youtube.com/watch?v=dJ7sWiOoK7g", "https://leetcode.com/problems/jump-game-ii"),
        Problem("Greedy", "Medium", "Gas Station", "https://www.youtube.com/watch?v=lJwbPZGo05A", "https://leetcode.com/problems/gas-station"),
        Problem("Greedy", "Medium", "Hand of Straights", "https://www.youtube.com/watch?v=amnrMCVd2YI", "https://leetcode.com/problems/hand-of-straights"),
        Problem("Greedy", "Medium", "Merge Triplets to Form Target Triplet", "https://www.youtube.com/watch?v=kShkQLQZ9K4", "https://leetcode.com/problems/merge-triplets-to-form-target-triplet"),
        Problem("Greedy", "Medium", "Partition Labels", "https://www.youtube.com/watch?v=B7m8UmZE-vw", "https://leetcode.com/problems/partition-labels"),
        Problem("Greedy", "Medium", "Valid Parenthesis String", "https://www.youtube.com/watch?v=QhPdNS143Qg", "https://leetcode.com/problems/valid-parenthesis-string"),
    ])

    # 16. Intervals (continued)
    problems.extend([
        Problem("Intervals", "Easy", "Meeting Rooms", "https://www.youtube.com/watch?v=PaJxqZVPhbg", "https://leetcode.com/problems/meeting-rooms"),
        Problem("Intervals", "Medium", "Insert Interval", "https://www.youtube.com/watch?v=A8NUOmlwOlM", "https://leetcode.com/problems/insert-interval"),
        Problem("Intervals", "Medium", "Merge Intervals", "https://www.youtube.com/watch?v=44H3cEC2fFM", "https://leetcode.com/problems/merge-intervals"),
        Problem("Intervals", "Medium", "Non-overlapping Intervals", "https://www.youtube.com/watch?v=nONCGxWoUfM", "https://leetcode.com/problems/non-overlapping-intervals"),
        Problem("Intervals", "Medium", "Meeting Rooms II", "https://www.youtube.com/watch?v=FdzJmTCVyJU", "https://leetcode.com/problems/meeting-rooms-ii"),
        Problem("Intervals", "Hard", "Minimum Interval to Include Each Query", "https://www.youtube.com/watch?v=5hQ5WWW5awQ", "https://leetcode.com/problems/minimum-interval-to-include-each-query"),
    ])

    # 17. Math and Geometry
    problems.extend([
        Problem("Math and Geometry", "Easy", "Happy Number", "https://www.youtube.com/watch?v=ljz85bxOYJ0", "https://leetcode.com/problems/happy-number"),
        Problem("Math and Geometry", "Easy", "Plus One", "https://www.youtube.com/watch?v=jIaA8boiG1s", "https://leetcode.com/problems/plus-one"),
        Problem("Math and Geometry", "Medium", "Rotate Image", "https://www.youtube.com/watch?v=fMSJSS7eO1w", "https://leetcode.com/problems/rotate-image"),
        Problem("Math and Geometry", "Medium", "Spiral Matrix", "https://www.youtube.com/watch?v=BJnMZNwUk1M", "https://leetcode.com/problems/spiral-matrix"),
        Problem("Math and Geometry", "Medium", "Set Matrix Zeroes", "https://www.youtube.com/watch?v=T41rL0L3Pnw", "https://leetcode.com/problems/set-matrix-zeroes"),
        Problem("Math and Geometry", "Medium", "Pow(x, n)", "https://www.youtube.com/watch?v=g9YQyYi4IQQ", "https://leetcode.com/problems/powx-n"),
        Problem("Math and Geometry", "Medium", "Multiply Strings", "https://www.youtube.com/watch?v=1vZswirL8Y8", "https://leetcode.com/problems/multiply-strings"),
        Problem("Math and Geometry", "Medium", "Detect Squares", "https://www.youtube.com/watch?v=bahebearrDc", "https://leetcode.com/problems/detect-squares"),
    ])

    # 18. Bit Manipulation
    problems.extend([
        Problem("Bit Manipulation", "Easy", "Single Number", "https://www.youtube.com/watch?v=qMPX1AOa83k", "https://leetcode.com/problems/single-number"),
        Problem("Bit Manipulation", "Easy", "Number of 1 Bits", "https://www.youtube.com/watch?v=5Km3utixwZs", "https://leetcode.com/problems/number-of-1-bits"),
        Problem("Bit Manipulation", "Easy", "Counting Bits", "https://www.youtube.com/watch?v=RyBM56RIWrM", "https://leetcode.com/problems/counting-bits"),
        Problem("Bit Manipulation", "Easy", "Reverse Bits", "https://www.youtube.com/watch?v=UcoN6UjAI64", "https://leetcode.com/problems/reverse-bits"),
        Problem("Bit Manipulation", "Easy", "Missing Number", "https://www.youtube.com/watch?v=WnPLSRLSANE", "https://leetcode.com/problems/missing-number"),
        Problem("Bit Manipulation", "Medium", "Sum of Two Integers", "https://www.youtube.com/watch?v=gVUrDV4tZfY", "https://leetcode.com/problems/sum-of-two-integers"),
        Problem("Bit Manipulation", "Medium", "Reverse Integer", "https://www.youtube.com/watch?v=HAgLH58IgJQ", "https://leetcode.com/problems/reverse-integer"),
    ])

    # Add problems to their respective categories
    for problem in problems:
        categories[problem.category].add_problem(problem)

    return categories
