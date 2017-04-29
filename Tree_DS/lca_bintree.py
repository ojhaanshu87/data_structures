class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def lca_binary_tree(root, elem1, elem2):
    if root is None:
        return 0
    if root.val==elem1 or root.val==elem2:
        return root.val
    left_lca = lca_binary_tree(root.left, elem1, elem2)
    right_lca = lca_binary_tree(root.right, elem1, elem2)
    if left_lca and right_lca:
        return root.val
    else:
        return left_lca if left_lca else right_lca