''' 
O(n) time and O(n) extra space
We can use one stack for printing from left to right and other stack for printing from right to left. 
In every iteration, we have nodes of one level in one of the stacks.
We print the nodes, and push nodes of next level in other stack.
'''

class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def level_order_spiral(self, root):
		if root is None:
			return
		stack1 = []
		stack2 = []
		stack1.append(root)
		while (stack1 or stack2):
			while (len(stack1)> 0):
				pop_elem = stack1.pop(0)
				print pop_elem.val,
				if pop_elem.right:
					stack1.append(pop_elem.right)
				if pop_elem.left:
					stack1.append(pop_elem.left)
			while (len(stack2)> 0):
				pop_elem = stack2.pop(0)
				print pop_elem.val,
				if pop_elem.left:
					stack2.append(pop_elem.left)
				if pop_elem.right:
					stack2.append(pop_elem.right)
	
tree_obj = Tree()
tree_obj.root = Node(1)
tree_obj.root.left = Node(2)
tree_obj.root.right = Node(3)
tree_obj.root.left.left = Node(7)
tree_obj.root.left.right = Node(6)
tree_obj.root.right.left = Node(5)
tree_obj.root.right.right = Node(4)
tree_obj.level_order_spiral(tree_obj.root)