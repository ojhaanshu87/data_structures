class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def height_tree(root):
	if root is None:
		return 0
	if root is not None and root.left is None and root.right is None:
		return 1
	else:
		lheight = height_tree(root.left)
		rheight = height_tree(root.right)
		if (lheight > rheight):
			return lheight+1
		else:
			return rheight+1

def reverse_level_util(root, level):
 
    if root is None:
        return
    if level ==1 :
        print root.val,
 
    elif level>1:
        reverse_level_util(root.left, level-1)
        reverse_level_util(root.right, level-1)
 
def reverse_level_order(root):
    h = height_tree(root)
    for i in reversed(range(1, h+1)):
        reverse_level_util(root,i)
