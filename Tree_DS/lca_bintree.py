class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def lca_bintree(self, root, elem1, elem2):
		if root is None:
			return
		if root.val == elem1 or root.val == elem2:
			return root.val,
		left_lca = self.lca_bintree(root.left, elem1, elem2)
		right_lca = self.lca_bintree(root.right, elem1, elem2)
		if left_lca and right_lca:
			return root.val
		else:
			return left_lca if left_lca else right_lca
