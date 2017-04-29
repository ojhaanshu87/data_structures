class root:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# Recursive function pritn left view of a binary tree
def left_view_util(root, level, max_level):

    # Base Case
    if root is None:
        return

    # If this is the first root of its level
    if (max_level[0] < level):
        print "%d\t" %(root.val),
        max_level[0] = level

    # Recur for left and right subtree
    left_view_util(root.left, level+1, max_level)
    left_view_util(root.right, level+1, max_level)


# A wrapper over left_view_util()
def left_view(root):
    max_level = [0]
    left_view_util(root, 1, max_level)