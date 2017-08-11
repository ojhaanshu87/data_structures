class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def preorder_itr(self, root):
		if root is None:
			return
		stack = []
		stack.append(root)
		while (len(stack) > 0):
			node = stack.pop()
			print node.val,
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

	def inorder_itr(self, root):
		if root is None:
			return
		stack = []
		curr = root
		flag = 0
		while (not flag):
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				if (len(stack) > 0):
					curr = stack.pop()
					print curr.val,
					curr = curr.right
				else:
					flag = 1

tree_obj = Tree()
tree_obj.root = Node(10)
tree_obj.root.left = Node(8)
tree_obj.root.right = Node(2)
tree_obj.root.left.left = Node(3)
tree_obj.root.left.right = Node(5)
tree_obj.root.right.left = Node(2)
tree_obj.inorder_itr(tree_obj.root)