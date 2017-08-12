class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def lca_bin_search(self, root, elem1, elem2):
		if root is None:
			return
		#if root is less than both elem then lca occour in right subtree 
		if root.val < elem1 and root.val < elem2:
			return self.lca_bin_search(root.right, elem1, elem2)
		#if root is greater than both elem then lca occour in left subtree 
		elif root.val > elem1 and root.val > elem2:
			return self.lca_bin_search(root.left, elem1, elem2)
		#if one key is in left subtree and other in right subtree then root is lca
		else:
			return root.val