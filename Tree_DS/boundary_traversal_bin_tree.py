# Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.


# We break the problem in 3 parts:
# 1. Print the left boundary in top-down manner.
# 2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts
#   21 Print all leaf nodes of left subtree from left to right
#   22 Print all leaf nodes of right subtree from left to right.
# 3 Print the right boundary in bottom-up manner.

# We need to take care of one thing that nodes are not printed again. e.g. The left most node is also the leaf node of the tree.

class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def print_leaves(self, root):
		#RESULT 4 8 6 7
		if (root):
			self.print_leaves(root.left)
			#print if it is a leaf node
			if root.left is None and root.right is None:
				print root.val,
			self.print_leaves(root.right)

	# A function to print all right boundary nodes, except a leaf node. Print the nodes in BOTTOM UP manner
	def right_boundary(self, root):
		#RESULT 3 1
		if(root):
			if (root.right):
				#for BOTTOM UP fashion first print right node 
				self.right_boundary(root.right)
				print root.val,
			elif (root.left):
				self.right_boundary(root.left)
				print root.val

	# A function to print all left boundary nodes, except a leaf node. Print the nodes in TOP DOWN manner
	def left_boundary(self, root):
		#RESULT 1 2
		if(root):
			if (root.left):
				# to ensure top down order, print the node before calling itself for left subtree
				print root.val,
				self.left_boundary(root.left)
			elif (root.right):
				print root.val,
				self.right_boundary(root.right)

	def boundary_traversal(self, root):
		if(root):
			print root.val,
			self.left_boundary(root.left)
			self.print_leaves(root.left)
			self.print_leaves(root.right)
			self.right_boundary(root.right)
				




if __name__ == '__main__':
	tree_obj = Tree()
	tree_obj.root = Node(1)
	tree_obj.root.left = Node(2)
	tree_obj.root.right = Node(3)
	tree_obj.root.left.left = Node(4)
	tree_obj.root.left.right = Node(5)
	tree_obj.root.right.left = Node(6)
	tree_obj.root.right.right = Node(7)
	tree_obj.root.left.right.right = Node(8)
	tree_obj.boundary_traversal(tree_obj.root)
