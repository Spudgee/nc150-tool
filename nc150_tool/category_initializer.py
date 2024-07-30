from models import Category
from constants import *

def initialize_categories():
    categories = {}

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