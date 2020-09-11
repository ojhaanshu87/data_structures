""""
Distance for follwoing program is calucalted only if both the input nodes are at same level with incomplete node info as LIST of Nodes 
For Sample Input 7 and 1
The Output as 
				The distance between node 7 and 1 which are at same level is 2
				('Incomplete nodes not having left or right child are ', [2, 7, 3])
For Sample Input 7 and 3
The Output as 
				node 7, and node 3 are not in same level
				('Incomplete nodes not having left or right child are ', [2, 7, 3])
				
***********************************************************************************************************************
Extension of the code if both node are not at same level and if distance needed then Uncomment line number 88 to 90 after comment 92 to 95
 
 """ 



DISTANCE = 0
INCOMPLETE_NODE = []

class Node(object):
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	#distance between two keys util function
	def dist_from_root(self, root, elem, k):
		# import pdb;
		# pdb.set_trace()
		global DISTANCE
		if root is None:
			return 0
		if root.val == elem:
			DISTANCE = k
		else:
			self.dist_from_root(root.left, elem, k+1)
			self.dist_from_root(root.right,elem,  k+1)
		return DISTANCE

	def lca_binary_tree(self, root, elem1, elem2):
		if root is None:
			return 0
		if root.val == elem1 or root.val == elem2:
			return root.val
		left_lca = self.lca_binary_tree(root.left, elem1, elem2)
		right_lca = self.lca_binary_tree(root.right, elem1, elem2)
		if left_lca and right_lca:
			return root.val
		else:
			return left_lca if left_lca else right_lca

	def is_child_node_present(self, root):
		global INCOMPLETE_NODE
		if root == None:
			return 0
		else:
			if root:
				# incomplete_node = []
				if root.left != None and root.right != None: 
					self.is_child_node_present(root.left)
					self.is_child_node_present(root.right)
				elif root.left != None and root.right == None: 
					INCOMPLETE_NODE.append(root.val)
					self.is_child_node_present(root.left)

				elif root.left == None and root.right != None: 
					INCOMPLETE_NODE.append(root.val)
					self.is_child_node_present(root.right)

				else:
					pass
		return "Incomplete nodes not having left or right child are ", INCOMPLETE_NODE


	def dist_bw_two_keys(self, root, elem1, elem2):
		global DISTANCE
		lca_elem = self.lca_binary_tree(root, elem1, elem2)
		self.dist_from_root(root, elem1,0)
		dist_elem1 = DISTANCE
		self.dist_from_root(root, elem2, 0)
		dist_elem2 = DISTANCE
		# self.dist_from_root(root, lca_elem, 0)
		# lca_elem_dist = DISTANCE
		# return "The total node distance between node {0} and {1} are {2}".format(str(elem1), str(elem2), str(dist_elem1 + dist_elem2 - 2*lca_elem_dist))

		if dist_elem1 == dist_elem2:
			return "The distance between node {0} and {1} which are at same level is {2}".format(str(elem1), str(elem2), str(dist_elem1))
		else:
			return "node {0}, and node {1} are not in same level".format(str(elem1), str(elem2))	

if __name__ == '__main__':
	tree_obj = Tree()
	tree_obj.root = Node(5)
	tree_obj.root.left = Node(2)
	tree_obj.root.right = Node(3)
	tree_obj.root.left.left = Node(7)
	tree_obj.root.left.left.left = Node(9)
	tree_obj.root.right.right = Node(1)
	tree_obj.root.right.right.left = Node(4)
	tree_obj.root.right.right.right = Node(6)
	print tree_obj.dist_bw_two_keys(tree_obj.root, 7, 3)
	print tree_obj.is_child_node_present(tree_obj.root)
