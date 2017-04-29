class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def size_tree(root):
    if root is None:
        return 0
    else:
        return (size_tree(root.left) + size_tree(root.right)+1)

def max_depth (root):
    if root is None:
        return 0
    if (root is not None and root.left is None and root.right is None):
        return 1
    else:
        l_depth = max_depth(root.left)
        r_depth = max_depth(root.right)
        if (l_depth > r_depth):
            return l_depth+1
        else:
            return r_depth+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
print max_depth(root)
