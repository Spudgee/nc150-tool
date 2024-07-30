from models import Category
from constants import *

def initialize_categories():
    categories = {}

    # Parental relationships between categories
    arrays_and_hashing = Category(ARRAYS_AND_HASHING)
    two_pointers = Category(TWO_POINTERS, [ARRAYS_AND_HASHING])
    stack = Category(STACK, [ARRAYS_AND_HASHING])
    binary_search = Category(BINARY_SEARCH, [TWO_POINTERS])
    sliding_window = Category(SLIDING_WINDOW, [TWO_POINTERS])
    linked_list = Category(LINKED_LIST, [TWO_POINTERS])
    trees = Category(TREES, [BINARY_SEARCH, LINKED_LIST])
    tries = Category(TRIES, [TREES])
    backtracking = Category(BACKTRACKING, [TREES])
    heap_priority_queue = Category(HEAP_PRIORITY_QUEUE, [TREES])
    graphs = Category(GRAPHS, [BACKTRACKING])
    advanced_graphs = Category(ADVANCED_GRAPHS, [GRAPHS, HEAP_PRIORITY_QUEUE])
    one_d_dp = Category(ONE_D_DP, [BACKTRACKING])
    two_d_dp = Category(TWO_D_DP, [ONE_D_DP, GRAPHS])
    greedy = Category(GREEDY, [HEAP_PRIORITY_QUEUE])
    intervals = Category(INTERVALS, [HEAP_PRIORITY_QUEUE])
    math_and_geometry = Category(MATH_AND_GEOMETRY, [GRAPHS, BIT_MANIPULATION])
    bit_manipulation = Category(BIT_MANIPULATION, [TWO_D_DP])

    # Set children of different categories
    arrays_and_hashing.children = [two_pointers, stack]
    two_pointers.children = [binary_search, sliding_window, linked_list]
    binary_search.children = [trees]
    linked_list.children = [trees]
    trees.children = [tries, heap_priority_queue, backtracking]
    heap_priority_queue.children = [intervals, greedy, advanced_graphs]
    backtracking.children = [graphs, one_d_dp]
    graphs.children = [advanced_graphs, math_and_geometry, two_d_dp]
    one_d_dp.children = [two_d_dp, bit_manipulation]

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