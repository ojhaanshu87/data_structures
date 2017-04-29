class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def children_sum (root):
    if (root is not None and root.left is None and root.right is None):
        return 1
    else:
        if (root.left is not None):
            left_sum = root.left.val
        if (root.right is not None):
            right_sum=root.right.val
        if (root.val == (left_sum+right_sum) and children_sum(root.left) and children_sum(root.right)):
            return 1
        else:
            return 0