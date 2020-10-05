# Problem Set 4A
# Name: Yi Xie
# Collaborators:
# Time Spent: 1.5 hours
# Late Days Used: x

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
treeA = [[14,19],[[3,5],0]] 
treeB = [[9,3],6] 
treeC = [[7], [16, 4, 2], [8]] 


# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """
    result = 0

    if tree == []: #base case
        return 0
    
    for ele in tree:
        
        if isinstance(ele, int):
            result += ele
    
        elif isinstance(ele, list):
            result += add_tree(ele) 
        
    
    return result


# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """
    result = base_case
    
    if tree == []:
        return base_case

    for ele in tree:
        
        if isinstance(ele, int):
            result = op(ele,result)
    
        elif isinstance(ele, list):
            result = op(op_tree(ele, op, base_case), result)
        
    
    return result


# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """
    #both int
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool):
        return a > 10 or b > 10
    
    #both bool
    if isinstance(a, bool) and isinstance(b, bool):
        return a or b 
    
    #a is int b is bool
    if isinstance(a, int) and not isinstance(a, bool) and isinstance(b, bool):
        return a > 10 or b 
    
    #a is bool b is int
    if isinstance(b, int) and not isinstance(b, bool) and isinstance(a, bool):
        return a or b > 10 
    

# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    op = max
    base_case = 0
    print (op_tree(treeA, op, base_case)) #should return 19
    print (op_tree(treeB, op, base_case)) #should return 9
    print (op_tree(treeC, op, base_case)) #should return 16
