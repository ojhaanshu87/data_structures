class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def mirror_tree (root):
    if root is None:
        return 0
    else:
         mirror_tree(root.left)
         mirror_tree(root.right)
         root.left, root.right = root.right, root.left

#for check before and after traversal
def preorder_traversal(root):
	if root:
		print root.val
		preorder_traversal(root.left)
		preorder_traversal(root.right)
