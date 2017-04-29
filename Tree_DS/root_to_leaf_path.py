class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def root_to_leaf_path(root):
    if root is None: 
        return []
    if (root.left == None and root.right == None):
        return [str(root.val)]

    left_subtree = root_to_leaf_path(root.left)  
    right_subtree = root_to_leaf_path(root.right)
    full_subtree = left_subtree + right_subtree

    root_tree = []
    for leaf in full_subtree:  # middle part of the comprehension
        root_tree.append(str(root.val) + '->'+ leaf)

    return root_tree
