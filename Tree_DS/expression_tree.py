class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def evaluate_exp_tree (root):
    # leaf node
    if root.left is None and root.right is None:
        return int(root.val)

    left_tree = evaluate_exp_tree(root.left)
    right_tree = evaluate_exp_tree(root.right)
    if root.val == '+':
        return left_tree+right_tree
    if root.val == '-':
        return left_tree-right_tree
    if root.val =='*':
        return left_tree*right_tree
    else:
        return left_tree / right_tree

if __name__=='__main__':
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('20')
    #print evaluate_exp_tree(root)
