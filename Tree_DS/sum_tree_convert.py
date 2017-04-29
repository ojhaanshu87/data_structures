class root:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def convert_to_sum_tree(root):
    if root is None:
        return 0
    else:
        old_val = root.val
        root.val = convert_to_sum_tree(root.left) + convert_to_sum_tree(root.right)
    return root.val + old_val

#for check before and after traversal
def preorder_traversal(root):
    if root:
        print root.val
        preorder_traversal(root.left)
        preorder_traversal(root.right)

