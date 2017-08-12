class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def root_to_leaf_path(self, root):
		if root is None:
			return
		if root.left is None and root.right is None:
			return [str(root.val)]
		full_subtree = self.root_to_leaf_path(root.left) + self.root_to_leaf_path(root.right)
		root_tree = []
		for elem in full_subtree:
			root_tree.append(str(root.val) + '->' + elem)
		return root_tree

#Time Complexity: O(n2) where n is number of nodes.	
# tree_obj = Tree()
# tree_obj.root = Node(1)
# tree_obj.root.left = Node(2)
# tree_obj.root.right = Node(3)
# tree_obj.root.left.left = Node(7)
# tree_obj.root.left.right = Node(6)
# tree_obj.root.right.left = Node(5)
# tree_obj.root.right.right = Node(4)
# print tree_obj.root_to_leaf_path(tree_obj.root)
# #['1->2->7', '1->2->6', '1->3->5', '1->3->4']
