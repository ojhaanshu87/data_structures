class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree(object):
    def __init__(self):
        self.root = None
    
    def is_inorder(self, root):
        stack, inorder_ptr = [], -1
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.data <= inorder_ptr:
                return False
            inorder_ptr = root.data
            root = root.right
        return True
    
if __name__ == '__main__':
	tree_obj = Tree()
	tree_obj.root = Node(3)
	tree_obj.root.left = Node(2)
	tree_obj.root.right = Node(5)
	tree_obj.root.right.left = Node(1)
	tree_obj.root.right.right = Node(4)
	tree_obj.root.right.left.left = Node(40)
	if (tree_obj.is_inorder(tree_obj.root)):
	    print("yes")
	else:
	    print("no")
