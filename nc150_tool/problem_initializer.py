from models import Problem
from constants import *

def initialize_problems(categories):
    problems = []

    # 1. Arrays and Hashing
    problems.extend([
        Problem(ARRAYS_AND_HASHING, "Easy", "Contains Duplicate", "https://www.youtube.com/watch?v=3OamzN90kPg", "https://leetcode.com/problems/contains-duplicate"),
        Problem(ARRAYS_AND_HASHING, "Easy", "Valid Anagram", "https://www.youtube.com/watch?v=9UtInBqnCgA", "https://leetcode.com/problems/valid-anagram"),
        Problem(ARRAYS_AND_HASHING, "Easy", "Two Sum", "https://www.youtube.com/watch?v=KLlXCFG5TnA", "https://leetcode.com/problems/two-sum"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Group Anagrams", "https://www.youtube.com/watch?v=vzdNOK2oB2E", "https://leetcode.com/problems/group-anagrams"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Top K Frequent Elements", "https://www.youtube.com/watch?v=YPTqKIgVk-k", "https://leetcode.com/problems/top-k-frequent-elements"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Product of Array Except Self", "https://www.youtube.com/watch?v=bNvIQI2wAjk", "https://leetcode.com/problems/product-of-array-except-self"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Valid Sudoku", "https://www.youtube.com/watch?v=TjFXEUCMqI8", "https://leetcode.com/problems/valid-sudoku"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Encode and Decode Strings", "https://www.youtube.com/watch?v=B1k_sxOSgv8", "https://leetcode.com/problems/encode-and-decode-strings"),
        Problem(ARRAYS_AND_HASHING, "Medium", "Longest Consecutive Sequence", "https://www.youtube.com/watch?v=P6RZZMu_maU", "https://leetcode.com/problems/longest-consecutive-sequence"),
    ])

    # 2. Two Pointers
    problems.extend([
        Problem(TWO_POINTERS, "Easy", "Valid Palindrome", "https://www.youtube.com/watch?v=jJXJ16kPFWg", "https://leetcode.com/problems/valid-palindrome"),
        Problem(TWO_POINTERS, "Medium", "Two Sum II - Input Array Is Sorted", "https://www.youtube.com/watch?v=cQ1Oz4ckceM", "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted"),
        Problem(TWO_POINTERS, "Medium", "3Sum", "https://www.youtube.com/watch?v=jzZsG8n2R9A", "https://leetcode.com/problems/3sum"),
        Problem(TWO_POINTERS, "Medium", "Container With Most Water", "https://www.youtube.com/watch?v=UuiTKBwPgAo", "https://leetcode.com/problems/container-with-most-water"),
        Problem(TWO_POINTERS, "Hard", "Trapping Rain Water", "https://www.youtube.com/watch?v=ZI2z5pq0TqA", "https://leetcode.com/problems/trapping-rain-water"),
    ])

    # 3. Stack
    problems.extend([
        Problem(STACK, "Easy", "Valid Parentheses", "https://www.youtube.com/watch?v=WTzjTskDFMg&t=9s", "https://leetcode.com/problems/valid-parentheses"),
        Problem(STACK, "Medium", "Min Stack", "https://www.youtube.com/watch?v=qkLl7nAwDPoandt=12s", "https://leetcode.com/problems/min-stack"),
        Problem(STACK, "Medium", "Evaluate Reverse Polish Notation", "https://www.youtube.com/watch?v=iu0082c4HDE", "https://leetcode.com/problems/evaluate-reverse-polish-notation"),
        Problem(STACK, "Medium", "Generate Parentheses", "https://www.youtube.com/watch?v=s9fokUqJ76A", "https://leetcode.com/problems/generate-parentheses"),
        Problem(STACK, "Medium", "Daily Temperatures", "https://www.youtube.com/watch?v=cTBiBSnjO3c", "https://leetcode.com/problems/daily-temperatures"),
        Problem(STACK, "Medium", "Car Fleet", "https://www.youtube.com/watch?v=Pr6T-3yB9RM", "https://leetcode.com/problems/car-fleet"),
        Problem(STACK, "Hard", "Largest Rectangle in Histogram", "https://www.youtube.com/watch?v=zx5Sw9130L0", "https://leetcode.com/problems/largest-rectangle-in-histogram"),
    ])

    # 4. Binary Search
    problems.extend([
        Problem(BINARY_SEARCH, "Easy", "Binary Search", "https://www.youtube.com/watch?v=s4DPM8ct1pI", "https://leetcode.com/problems/binary-search"),
        Problem(BINARY_SEARCH, "Medium", "Search a 2D Matrix", "https://www.youtube.com/watch?v=Ber2pi2C0j0", "https://leetcode.com/problems/search-a-2d-matrix"),
        Problem(BINARY_SEARCH, "Medium", "Koko Eating Bananas", "https://www.youtube.com/watch?v=U2SozAs9RzA", "https://leetcode.com/problems/koko-eating-bananas"),
        Problem(BINARY_SEARCH, "Medium", "Find Minimum in Rotated Sorted Array", "https://www.youtube.com/watch?v=nIVW4P8b1VA", "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array"),
        Problem(BINARY_SEARCH, "Medium", "Search in Rotated Sorted Array", "https://www.youtube.com/watch?v=U8XENwh8Oy8", "https://leetcode.com/problems/search-in-rotated-sorted-array"),
        Problem(BINARY_SEARCH, "Medium", "Time Based Key-Value Store", "https://www.youtube.com/watch?v=fu2cD_6E8Hw", "https://leetcode.com/problems/time-based-key-value-store"),
        Problem(BINARY_SEARCH, "Hard", "Median of Two Sorted Arrays", "https://www.youtube.com/watch?v=q6IEA26hvXc", "https://leetcode.com/problems/median-of-two-sorted-arrays"),
    ])

    # 5. Sliding Window
    problems.extend([
        Problem(SLIDING_WINDOW, "Easy", "Best Time to Buy and Sell Stock", "https://www.youtube.com/watch?v=1pkOgXD63yU", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock"),
        Problem(SLIDING_WINDOW, "Medium", "Longest Substring Without Repeating Characters", "https://www.youtube.com/watch?v=wiGpQwVHdE0", "https://leetcode.com/problems/longest-substring-without-repeating-characters"),
        Problem(SLIDING_WINDOW, "Medium", "Longest Repeating Character Replacement", "https://www.youtube.com/watch?v=gqXU1UyA8pk", "https://leetcode.com/problems/longest-repeating-character-replacement"),
        Problem(SLIDING_WINDOW, "Medium", "Permutation in String", "https://www.youtube.com/watch?v=UbyhOgBN834", "https://leetcode.com/problems/permutation-in-string"),
        Problem(SLIDING_WINDOW, "Hard", "Minimum Window Substring", "https://www.youtube.com/watch?v=jSto0O4AJbM", "https://leetcode.com/problems/minimum-window-substring"),
        Problem(SLIDING_WINDOW, "Hard", "Sliding Window Maximum", "https://www.youtube.com/watch?v=DfljaUwZsOk", "https://leetcode.com/problems/sliding-window-maximum"),
    ])

    # 6. Linked List
    problems.extend([
        Problem(LINKED_LIST, "Easy", "Reverse Linked List", "https://www.youtube.com/watch?v=G0_I-ZF0S38", "https://leetcode.com/problems/reverse-linked-list"),
        Problem(LINKED_LIST, "Easy", "Merge Two Sorted Lists", "https://www.youtube.com/watch?v=XIdigk956u0", "https://leetcode.com/problems/merge-two-sorted-lists"),
        Problem(LINKED_LIST, "Easy", "Linked List Cycle", "https://www.youtube.com/watch?v=gBTe7lFR3vc", "https://leetcode.com/problems/linked-list-cycle"),
        Problem(LINKED_LIST, "Medium", "Reorder List", "https://www.youtube.com/watch?v=S5bfdUTrKLM", "https://leetcode.com/problems/reorder-list"),
        Problem(LINKED_LIST, "Medium", "Remove Nth Node From End of List", "https://www.youtube.com/watch?v=XVuQxVej6y8", "https://leetcode.com/problems/remove-nth-node-from-end-of-list"),
        Problem(LINKED_LIST, "Medium", "Copy List with Random Pointer", "https://www.youtube.com/watch?v=5Y2EiZST97Y", "https://leetcode.com/problems/copy-list-with-random-pointer"),
        Problem(LINKED_LIST, "Medium", "Add Two Numbers", "https://www.youtube.com/watch?v=wgFPrzTjm7s", "https://leetcode.com/problems/add-two-numbers"),
        Problem(LINKED_LIST, "Medium", "Find the Duplicate Number", "https://www.youtube.com/watch?v=wjYnzkAhcNk", "https://leetcode.com/problems/find-the-duplicate-number"),
        Problem(LINKED_LIST, "Medium", "LRU Cache", "https://www.youtube.com/watch?v=7ABFKPK2hD4", "https://leetcode.com/problems/lru-cache"),
        Problem(LINKED_LIST, "Hard", "Merge K Sorted Lists", "https://www.youtube.com/watch?v=q5a5OiGbT6Q", "https://leetcode.com/problems/merge-k-sorted-lists"),
        Problem(LINKED_LIST, "Hard", "Reverse Nodes in k-Group", "https://www.youtube.com/watch?v=1UOPsfP85V4", "https://leetcode.com/problems/reverse-nodes-in-k-group"),
    ])

    # 7. Trees
    problems.extend([
        Problem(TREES, "Easy", "Invert Binary Tree", "https://www.youtube.com/watch?v=OnSn2XEQ4MY", "https://leetcode.com/problems/invert-binary-tree"),
        Problem(TREES, "Easy", "Maximum Depth of Binary Tree", "https://www.youtube.com/watch?v=hTM3phVI6YQ", "https://leetcode.com/problems/maximum-depth-of-binary-tree"),
        Problem(TREES, "Easy", "Diameter of Binary Tree", "https://www.youtube.com/watch?v=bkxqA8Rfv04", "https://leetcode.com/problems/diameter-of-binary-tree"),
        Problem(TREES, "Easy", "Balanced Binary Tree", "https://www.youtube.com/watch?v=QfJsau0ItOY", "https://leetcode.com/problems/balanced-binary-tree"),
        Problem(TREES, "Easy", "Same Tree", "https://www.youtube.com/watch?v=vRbbcKXCxOw", "https://leetcode.com/problems/same-tree"),
        Problem(TREES, "Easy", "Subtree of Another Tree", "https://www.youtube.com/watch?v=E36O5SWp-LE", "https://leetcode.com/problems/subtree-of-another-tree"),
        Problem(TREES, "Medium", "Lowest Common Ancestor of a Binary Search Tree", "https://www.youtube.com/watch?v=gs2LMfuOR9k", "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree"),
        Problem(TREES, "Medium", "Binary Tree Level Order Traversal", "https://www.youtube.com/watch?v=6ZnyEApgFYg", "https://leetcode.com/problems/binary-tree-level-order-traversal"),
        Problem(TREES, "Medium", "Binary Tree Right Side View", "https://www.youtube.com/watch?v=d4zLyf32e3I", "https://leetcode.com/problems/binary-tree-right-side-view"),
        Problem(TREES, "Medium", "Count Good Nodes in Binary Tree", "https://www.youtube.com/watch?v=7cp5imvDzl4", "https://leetcode.com/problems/count-good-nodes-in-binary-tree"),
        Problem(TREES, "Medium", "Validate Binary Search Tree", "https://www.youtube.com/watch?v=s6ATEkipzow", "https://leetcode.com/problems/validate-binary-search-tree"),
        Problem(TREES, "Medium", "Kth Smallest Element in a BST", "https://www.youtube.com/watch?v=5LUXSvjmGCw", "https://leetcode.com/problems/kth-smallest-element-in-a-bst"),
        Problem(TREES, "Medium", "Construct Binary Tree from Preorder and Inorder Traversal", "https://www.youtube.com/watch?v=ihj4IQGZ2zc", "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal"),
        Problem(TREES, "Hard", "Binary Tree Maximum Path Sum", "https://www.youtube.com/watch?v=Hr5cWUld4vU", "https://leetcode.com/problems/binary-tree-maximum-path-sum"),
        Problem(TREES, "Hard", "Serialize and Deserialize Binary Tree", "https://www.youtube.com/watch?v=u4JAi2JJhI8", "https://leetcode.com/problems/serialize-and-deserialize-binary-tree"),
    ])

    # 8. Tries
    problems.extend([
        Problem(TRIES, "Medium", "Implement Trie (Prefix Tree)", "https://www.youtube.com/watch?v=oobqoCJlHA0", "https://leetcode.com/problems/implement-trie-prefix-tree"),
        Problem(TRIES, "Medium", "Design Add and Search Words Data Structure", "https://www.youtube.com/watch?v=BTf05gs_8iU", "https://leetcode.com/problems/design-add-and-search-words-data-structure"),
        Problem(TRIES, "Hard", "Word Search II", "https://www.youtube.com/watch?v=asbcE9mZz_U", "https://leetcode.com/problems/word-search-ii"),
    ])

    # 9. Backtracking (continued)
    problems.extend([
        Problem(BACKTRACKING, "Medium", "Subsets", "https://www.youtube.com/watch?v=REOH22Xwdkk", "https://leetcode.com/problems/subsets"),
        Problem(BACKTRACKING, "Medium", "Combination Sum", "https://www.youtube.com/watch?v=GBKI9VSKdGg", "https://leetcode.com/problems/combination-sum"),
        Problem(BACKTRACKING, "Medium", "Permutations", "https://www.youtube.com/watch?v=FZe0UqISmUw", "https://leetcode.com/problems/permutations"),
        Problem(BACKTRACKING, "Medium", "Subsets II", "https://www.youtube.com/watch?v=Vn2v6ajA7U0", "https://leetcode.com/problems/subsets-ii"),
        Problem(BACKTRACKING, "Medium", "Combination Sum II", "https://www.youtube.com/watch?v=rSA3t6BDDwg", "https://leetcode.com/problems/combination-sum-ii"),
        Problem(BACKTRACKING, "Medium", "Word Search", "https://www.youtube.com/watch?v=pfiQ_PS1g8E", "https://leetcode.com/problems/word-search"),
        Problem(BACKTRACKING, "Medium", "Palindrome Partitioning", "https://www.youtube.com/watch?v=3jvWodd7ht0", "https://leetcode.com/problems/palindrome-partitioning"),
        Problem(BACKTRACKING, "Medium", "Letter Combinations of a Phone Number", "https://www.youtube.com/watch?v=0snEunUacZY", "https://leetcode.com/problems/letter-combinations-of-a-phone-number"),
        Problem(BACKTRACKING, "Hard", "N-Queens", "https://www.youtube.com/watch?v=Ph95IHmRp5M", "https://leetcode.com/problems/n-queens"),
    ])

    # 10. Heap / Priority Queue
    problems.extend([
        Problem(HEAP_PRIORITY_QUEUE, "Easy", "Kth Largest Element in a Stream", "https://www.youtube.com/watch?v=hOjcdrqMoQ8", "https://leetcode.com/problems/kth-largest-element-in-a-stream"),
        Problem(HEAP_PRIORITY_QUEUE, "Easy", "Last Stone Weight", "https://www.youtube.com/watch?v=B-QCq79-Vfw", "https://leetcode.com/problems/last-stone-weight"),
        Problem(HEAP_PRIORITY_QUEUE, "Medium", "K Closest Points to Origin", "https://www.youtube.com/watch?v=rI2EBUEMfTk", "https://leetcode.com/problems/k-closest-points-to-origin"),
        Problem(HEAP_PRIORITY_QUEUE, "Medium", "Kth Largest Element in an Array", "https://www.youtube.com/watch?v=XEmy13g1Qxc", "https://leetcode.com/problems/kth-largest-element-in-an-array"),
        Problem(HEAP_PRIORITY_QUEUE, "Medium", "Task Scheduler", "https://www.youtube.com/watch?v=s8p8ukTyA2I", "https://leetcode.com/problems/task-scheduler"),
        Problem(HEAP_PRIORITY_QUEUE, "Medium", "Design Twitter", "https://www.youtube.com/watch?v=pNichitDD2E", "https://leetcode.com/problems/design-twitter"),
        Problem(HEAP_PRIORITY_QUEUE, "Hard", "Find Median from Data Stream", "https://www.youtube.com/watch?v=itmhHWaHupI", "https://leetcode.com/problems/find-median-from-data-stream"),
    ])

    # 11. Graphs
    problems.extend([
        Problem(GRAPHS, "Medium", "Number of Islands", "https://www.youtube.com/watch?v=pV2kpPD66nE", "https://leetcode.com/problems/number-of-islands"),
        Problem(GRAPHS, "Medium", "Clone Graph", "https://www.youtube.com/watch?v=mQeF6bN8hMk", "https://leetcode.com/problems/clone-graph"),
        Problem(GRAPHS, "Medium", "Max Area of Island", "https://www.youtube.com/watch?v=W8VuDt0eb5c", "https://leetcode.com/problems/max-area-of-island"),
        Problem(GRAPHS, "Medium", "Pacific Atlantic Water Flow", "https://www.youtube.com/watch?v=s-VkcjHqkGI", "https://leetcode.com/problems/pacific-atlantic-water-flow"),
        Problem(GRAPHS, "Medium", "Surrounded Regions", "https://www.youtube.com/watch?v=9z2BunfoZ5Y", "https://leetcode.com/problems/surrounded-regions"),
        Problem(GRAPHS, "Medium", "Rotting Oranges", "https://www.youtube.com/watch?v=y704fEOx0s0", "https://leetcode.com/problems/rotting-oranges"),
        Problem(GRAPHS, "Medium", "Walls and Gates", "https://www.youtube.com/watch?v=e69C6xhiSQE", "https://leetcode.com/problems/walls-and-gates"),
        Problem(GRAPHS, "Medium", "Course Schedule", "https://www.youtube.com/watch?v=EgI5nU9etnU", "https://leetcode.com/problems/course-schedule"),
        Problem(GRAPHS, "Medium", "Course Schedule II", "https://www.youtube.com/watch?v=Akt3glAwyfY", "https://leetcode.com/problems/course-schedule-ii"),
        Problem(GRAPHS, "Medium", "Redundant Connection", "https://www.youtube.com/watch?v=FXWRE67PLL0", "https://leetcode.com/problems/redundant-connection"),
        Problem(GRAPHS, "Medium", "Number of Connected Components in an Undirected Graph", "https://www.youtube.com/watch?v=8f1XPm4WOUc", "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph"),
        Problem(GRAPHS, "Medium", "Graph Valid Tree", "https://www.youtube.com/watch?v=bXsUuownnoQ", "https://leetcode.com/problems/graph-valid-tree"),
        Problem(GRAPHS, "Hard", "Word Ladder", "https://www.youtube.com/watch?v=h9iTnkgv05E", "https://leetcode.com/problems/word-ladder"),
    ])

    # 12. Advanced Graphs
    problems.extend([
        Problem(ADVANCED_GRAPHS, "Medium", "Reconstruct Itinerary", "https://www.youtube.com/watch?v=ZyB_gQ8vqGA", "https://leetcode.com/problems/reconstruct-itinerary"),
        Problem(ADVANCED_GRAPHS, "Medium", "Min Cost to Connect All Points", "https://www.youtube.com/watch?v=f7JOBJIC-NA", "https://leetcode.com/problems/min-cost-to-connect-all-points"),
        Problem(ADVANCED_GRAPHS, "Medium", "Network Delay Time", "https://www.youtube.com/watch?v=EaphyqKU4PQ", "https://leetcode.com/problems/network-delay-time"),
        Problem(ADVANCED_GRAPHS, "Hard", "Swim in Rising Water", "https://www.youtube.com/watch?v=amvrKlMLuGY", "https://leetcode.com/problems/swim-in-rising-water"),
        Problem(ADVANCED_GRAPHS, "Hard", "Alien Dictionary", "https://www.youtube.com/watch?v=6kTZYvNNyps", "https://leetcode.com/problems/alien-dictionary"),
        Problem(ADVANCED_GRAPHS, "Hard", "Cheapest Flights Within K Stops", "https://www.youtube.com/watch?v=5eIK3zUdYmE", "https://leetcode.com/problems/cheapest-flights-within-k-stops"),
    ])

    # 13. 1-D Dynamic Programming
    problems.extend([
        Problem(ONE_D_DP, "Easy", "Climbing Stairs", "https://www.youtube.com/watch?v=Y0lT9Fck7qI", "https://leetcode.com/problems/climbing-stairs"),
        Problem(ONE_D_DP, "Easy", "Min Cost Climbing Stairs", "https://www.youtube.com/watch?v=ktmzAZWkEZ0", "https://leetcode.com/problems/min-cost-climbing-stairs"),
        Problem(ONE_D_DP, "Medium", "House Robber", "https://www.youtube.com/watch?v=73r3KWiEvyk", "https://leetcode.com/problems/house-robber"),
        Problem(ONE_D_DP, "Medium", "House Robber II", "https://www.youtube.com/watch?v=rWAJCfYYOvM", "https://leetcode.com/problems/house-robber-ii"),
        Problem(ONE_D_DP, "Medium", "Longest Palindromic Substring", "https://www.youtube.com/watch?v=XYQecbcd6_c", "https://leetcode.com/problems/longest-palindromic-substring"),
        Problem(ONE_D_DP, "Medium", "Palindromic Substrings", "https://www.youtube.com/watch?v=4RACzI5-du8", "https://leetcode.com/problems/palindromic-substrings"),
        Problem(ONE_D_DP, "Medium", "Decode Ways", "https://www.youtube.com/watch?v=6aEyTjOwlJU", "https://leetcode.com/problems/decode-ways"),
        Problem(ONE_D_DP, "Medium", "Coin Change", "https://www.youtube.com/watch?v=H9bfqozjoqs", "https://leetcode.com/problems/coin-change"),
        Problem(ONE_D_DP, "Medium", "Maximum Product Subarray", "https://www.youtube.com/watch?v=lXVy6YWFcRM", "https://leetcode.com/problems/maximum-product-subarray"),
        Problem(ONE_D_DP, "Medium", "Word Break", "https://www.youtube.com/watch?v=Sx9NNgInc3A", "https://leetcode.com/problems/word-break"),
        Problem(ONE_D_DP, "Medium", "Longest Increasing Subsequence", "https://www.youtube.com/watch?v=cjWnW0hdF1Y", "https://leetcode.com/problems/longest-increasing-subsequence"),
        Problem(ONE_D_DP, "Medium", "Partition Equal Subset Sum", "https://www.youtube.com/watch?v=IsvocB5BJhw", "https://leetcode.com/problems/partition-equal-subset-sum"),
    ])

    # 14. 2-D Dynamic Programming
    problems.extend([
        Problem(TWO_D_DP, "Medium", "Unique Paths", "https://www.youtube.com/watch?v=IlEsdxuD4lY", "https://leetcode.com/problems/unique-paths"),
        Problem(TWO_D_DP, "Medium", "Longest Common Subsequence", "https://www.youtube.com/watch?v=Ua0GhsJSlWM", "https://leetcode.com/problems/longest-common-subsequence"),
        Problem(TWO_D_DP, "Medium", "Best Time to Buy and Sell Stock With Cooldown", "https://www.youtube.com/watch?v=I7j0F7AHpb8", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown"),
        Problem(TWO_D_DP, "Medium", "Coin Change II", "https://www.youtube.com/watch?v=Mjy4hd2xgrs", "https://leetcode.com/problems/coin-change-ii"),
        Problem(TWO_D_DP, "Medium", "Target Sum", "https://www.youtube.com/watch?v=g0npyaQtAQM", "https://leetcode.com/problems/target-sum"),
        Problem(TWO_D_DP, "Medium", "Interleaving String", "https://www.youtube.com/watch?v=3Rw3p9LrgvE", "https://leetcode.com/problems/interleaving-string"),
        Problem(TWO_D_DP, "Hard", "Longest Increasing Path in a Matrix", "https://www.youtube.com/watch?v=wCc_nd-GiEc", "https://leetcode.com/problems/longest-increasing-path-in-a-matrix"),
        Problem(TWO_D_DP, "Hard", "Distinct Subsequences", "https://www.youtube.com/watch?v=-RDzMJ33nx8", "https://leetcode.com/problems/distinct-subsequences"),
        Problem(TWO_D_DP, "Hard", "Edit Distance", "https://www.youtube.com/watch?v=XYi2-LPrwm4", "https://leetcode.com/problems/edit-distance"),
        Problem(TWO_D_DP, "Hard", "Burst Balloons", "https://www.youtube.com/watch?v=VFskby7lUbw", "https://leetcode.com/problems/burst-balloons"),
        Problem(TWO_D_DP, "Hard", "Regular Expression Matching", "https://www.youtube.com/watch?v=HAA8mgxlov8", "https://leetcode.com/problems/regular-expression-matching"),
    ])

    # 15. Greedy
    problems.extend([
        Problem(GREEDY, "Medium", "Maximum Subarray", "https://www.youtube.com/watch?v=5WZl3MMT0Eg", "https://leetcode.com/problems/maximum-subarray"),
        Problem(GREEDY, "Medium", "Jump Game", "https://www.youtube.com/watch?v=Yan0cv2cLy8", "https://leetcode.com/problems/jump-game"),
        Problem(GREEDY, "Medium", "Jump Game II", "https://www.youtube.com/watch?v=dJ7sWiOoK7g", "https://leetcode.com/problems/jump-game-ii"),
        Problem(GREEDY, "Medium", "Gas Station", "https://www.youtube.com/watch?v=lJwbPZGo05A", "https://leetcode.com/problems/gas-station"),
        Problem(GREEDY, "Medium", "Hand of Straights", "https://www.youtube.com/watch?v=amnrMCVd2YI", "https://leetcode.com/problems/hand-of-straights"),
        Problem(GREEDY, "Medium", "Merge Triplets to Form Target Triplet", "https://www.youtube.com/watch?v=kShkQLQZ9K4", "https://leetcode.com/problems/merge-triplets-to-form-target-triplet"),
        Problem(GREEDY, "Medium", "Partition Labels", "https://www.youtube.com/watch?v=B7m8UmZE-vw", "https://leetcode.com/problems/partition-labels"),
        Problem(GREEDY, "Medium", "Valid Parenthesis String", "https://www.youtube.com/watch?v=QhPdNS143Qg", "https://leetcode.com/problems/valid-parenthesis-string"),
    ])

    # 16. Intervals (continued)
    problems.extend([
        Problem(INTERVALS, "Easy", "Meeting Rooms", "https://www.youtube.com/watch?v=PaJxqZVPhbg", "https://leetcode.com/problems/meeting-rooms"),
        Problem(INTERVALS, "Medium", "Insert Interval", "https://www.youtube.com/watch?v=A8NUOmlwOlM", "https://leetcode.com/problems/insert-interval"),
        Problem(INTERVALS, "Medium", "Merge Intervals", "https://www.youtube.com/watch?v=44H3cEC2fFM", "https://leetcode.com/problems/merge-intervals"),
        Problem(INTERVALS, "Medium", "Non-overlapping Intervals", "https://www.youtube.com/watch?v=nONCGxWoUfM", "https://leetcode.com/problems/non-overlapping-intervals"),
        Problem(INTERVALS, "Medium", "Meeting Rooms II", "https://www.youtube.com/watch?v=FdzJmTCVyJU", "https://leetcode.com/problems/meeting-rooms-ii"),
        Problem(INTERVALS, "Hard", "Minimum Interval to Include Each Query", "https://www.youtube.com/watch?v=5hQ5WWW5awQ", "https://leetcode.com/problems/minimum-interval-to-include-each-query"),
    ])

    # 17. Math and Geometry
    problems.extend([
        Problem(MATH_AND_GEOMETRY, "Easy", "Happy Number", "https://www.youtube.com/watch?v=ljz85bxOYJ0", "https://leetcode.com/problems/happy-number"),
        Problem(MATH_AND_GEOMETRY, "Easy", "Plus One", "https://www.youtube.com/watch?v=jIaA8boiG1s", "https://leetcode.com/problems/plus-one"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Rotate Image", "https://www.youtube.com/watch?v=fMSJSS7eO1w", "https://leetcode.com/problems/rotate-image"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Spiral Matrix", "https://www.youtube.com/watch?v=BJnMZNwUk1M", "https://leetcode.com/problems/spiral-matrix"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Set Matrix Zeroes", "https://www.youtube.com/watch?v=T41rL0L3Pnw", "https://leetcode.com/problems/set-matrix-zeroes"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Pow(x, n)", "https://www.youtube.com/watch?v=g9YQyYi4IQQ", "https://leetcode.com/problems/powx-n"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Multiply Strings", "https://www.youtube.com/watch?v=1vZswirL8Y8", "https://leetcode.com/problems/multiply-strings"),
        Problem(MATH_AND_GEOMETRY, "Medium", "Detect Squares", "https://www.youtube.com/watch?v=bahebearrDc", "https://leetcode.com/problems/detect-squares"),
    ])

    # 18. Bit Manipulation
    problems.extend([
        Problem(BIT_MANIPULATION, "Easy", "Single Number", "https://www.youtube.com/watch?v=qMPX1AOa83k", "https://leetcode.com/problems/single-number"),
        Problem(BIT_MANIPULATION, "Easy", "Number of 1 Bits", "https://www.youtube.com/watch?v=5Km3utixwZs", "https://leetcode.com/problems/number-of-1-bits"),
        Problem(BIT_MANIPULATION, "Easy", "Counting Bits", "https://www.youtube.com/watch?v=RyBM56RIWrM", "https://leetcode.com/problems/counting-bits"),
        Problem(BIT_MANIPULATION, "Easy", "Reverse Bits", "https://www.youtube.com/watch?v=UcoN6UjAI64", "https://leetcode.com/problems/reverse-bits"),
        Problem(BIT_MANIPULATION, "Easy", "Missing Number", "https://www.youtube.com/watch?v=WnPLSRLSANE", "https://leetcode.com/problems/missing-number"),
        Problem(BIT_MANIPULATION, "Medium", "Sum of Two Integers", "https://www.youtube.com/watch?v=gVUrDV4tZfY", "https://leetcode.com/problems/sum-of-two-integers"),
        Problem(BIT_MANIPULATION, "Medium", "Reverse Integer", "https://www.youtube.com/watch?v=HAgLH58IgJQ", "https://leetcode.com/problems/reverse-integer"),
    ])

    # Add problems to their respective categories
    for problem in problems:
        categories[problem.category].add_problem(problem)

    return categories
