class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def k_distance_down_from_root(self, root, k):
		if root == None:
			return
		if k ==0:
			print root.val,
		self.k_distance_down_from_root(root.left, k-1)
		self.k_distance_down_from_root(root.right, k-1)

	def k_distance_from_given_node(self, root, k, given_node):
		if root is None:
			return
		if root == given_node:
			self.k_distance_down_from_root(root, k)
			return 0
		#recur for left subtree
		left_recur = self.k_distance_from_given_node(root.left, k, given_node)
		#CHECK IF GIVEn node found in left subtree
		if left_recur != -1:
			#if root is distance from given node, print root
			#left recur is distanc of root's left child of target
			if left_recur+1 == k:
				print root.val,
			else:
				self.k_distance_down_from_root(root.right, k-left_recur-2)
			return 1 + left_recur
		#mirror of line 25 to line 35 above
		right_recur = self.k_distance_from_given_node(root.right, k, given_node)
		if right_recur != -1:
			if right_recur+1 == k:
				print root.val,
			else:
				self.k_distance_down_from_root(root.left, k-right_recur-2)
			return 1 + right_recur

#Time Complexity:O(n)	
# tree_obj = Tree()
# tree_obj.root = Node(1)
# tree_obj.root.left = Node(2)
# tree_obj.root.right = Node(3)
# tree_obj.root.left.left = Node(7)
# tree_obj.root.left.right = Node(6)
# tree_obj.root.right.left = Node(5)
# tree_obj.root.right.right = Node(4)
# tree_obj.k_distance_from_given_node(tree_obj.root, 2, tree_obj.root.left.left)
