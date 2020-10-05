A tree is a hierarchical data structure composed of linked nodes. The highest node is called the root, which has branches that link it to other nodes, which are themselves roots of their respective subtrees. 

In this problem set, we will be using lists to represent trees. Since lists do not have hierarchical information themselves, we will be using sublists to indicate subtrees.

The tree above can be represented as the following list:

example_tree = [[1,3], [[5,7], 10]]

We represent each leaf with the integer value it holds, and non-leaves (root or intermediate nodes) with a list. Note that the recursion property holds: if we consider the right branch, [[5,7], 10], we see that it is also a valid tree.
