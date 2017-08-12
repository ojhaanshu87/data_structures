class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def size_tree(self, root):
		if root is None:
			return
		if root is not None and root.left is None and root.right is None:
			return 1
		else:
			return 1 + self.size_tree(root.left) + self.size_tree(root.right)

	def depth_tree(self, root):
		if root is None:
			return
		if root is not None and root.left is None and root.right is None:
			return 1
		else:
			return 1 + max(self.depth_tree(root.left), self.depth_tree(root.right))
