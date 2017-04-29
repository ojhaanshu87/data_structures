class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def reverse_traversal_util (root1, root2, set_val):
	if root1 is None or root2 is None:
		return
	if (set_val %2 ==0):
		root1.val, root2.val = root2.val, root1.val
	reverse_traversal_util(root1.left, root2.right, set_val+1)
	reverse_traversal_util(root1.right, root2.left, set_val+1)

def reverse_alternate_node(root):
	reverse_traversal_util(root.left, root.right, 0)

def inorder_traversal (root):
	if root:
		inorder_traversal(root.left)
		print root.val
		inorder_traversal(root.right)