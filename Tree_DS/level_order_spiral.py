class Node:
	def __init__ (self, key):
		self. left = None
		self.right = None
		self.val = key

def height_tree(root):
	if root is None:
		return 0
	if root is not None and root.left is None and root.right is None:
		return 1
	else:
		return 1 + max(height_tree(root.left), height_tree(root.right))

def spiral_form_util (root, level, set_value):
	if root is None:
		return
	if level==1:
		print root.val
	elif level > 1:
		if (set_value):
			spiral_form_util(root.left, level-1, set_value)
			spiral_form_util(root.right, level-1, set_value)
		else:
			spiral_form_util(root.right, level-1, set_value)
			spiral_form_util(root.left, level-1, set_value)

def spiral_form_traversal(root):
	set_value = False
	h = height_tree(root)
	for i in range(1, h+1):
		spiral_form_util(root, i, set_value)
		set_value = not set_value