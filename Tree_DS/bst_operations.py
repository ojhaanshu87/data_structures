class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class BST(object):
	def __init__(self):
		self.root =None

	def inorder_traversal(self, root):
		if root:
			self.inorder_traversal(root.left)
			print root.val,
			self.inorder_traversal(root.right)

	def insert_bst(self, root, elem):
		if root is None:
			root = elem
		else:
			if root.val < elem.val:
				if root.right is None:
					root.right = elem
				else:
					self.insert_bst(root.right, elem)
			else:
				if root.left is None:
					root.left = elem
				else:
					self.insert_bst(root.left, elem)


	def search_bst(self,root, elem):
		if root is None:
			return -1
		if root.val == elem:
			return root.val
		if root.val < elem:
		    return self.search_bst(root.right, elem)
		if root.val > elem:
			return self.search_bst(root.left, elem)

	def smallest_in_right(self, root):
		while root.left is not None:
			root = root.left
		return root

	def delete_bst_node(self, root, elem):
		if root is None :
			return root
		if root.val > elem:
			left_rec = self.delete_bst_node(root.left, elem)
		elif root.val < elem:
			right_rec = self.delete_bst_node(root.right, elem)
		else:
			#if root is to be delete with one or no child
			if root.left is None:
				tmp = root.right
				root = None
				return tmp
			if root.right is None:
				tmp = root.left
				root = None
				return tmp
			#if root have two child then get Inorder successor
			tmp = self.smallest_in_right(root.right)
			root.val = tmp.val
			root.right = self.delete_bst_node(root.right, tmp.val)
		return root