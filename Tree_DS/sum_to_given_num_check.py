class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def sum_to_given_num (root, target):
    if root is None:
        return (target ==0)
    else:
        ans = 0
        sub_sum = target-root.val
        if (sub_sum==0 and root.left is None and root.right is None):
            return 1
        if (root.left <> None):
            ans = ans or sum_to_given_num(root.left, sub_sum)
        if (root.right <> None):
            ans = ans or sum_to_given_num(root.right, sub_sum)
        return ans