class Node(object):
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	def reverse_level_order (self, root):
		if root is None:
			return
		stack = []
		queue = []
		queue.append(root)
		while (len(queue) > 0):
			pop_elem = queue.pop(0)
			stack.append(pop_elem)
			#every time to maintain the sequence insert right child first then left child
			if pop_elem.right:
				queue.append(pop_elem.right)
			if pop_elem.left:
				queue.append(pop_elem.left)
		#pop all item from stack and print
		while (len(stack) > 0):
			pop_elem = stack.pop()
			print pop_elem.val,

"""
RECURSIVE APPROACH
INPUT
    3
   / \
  9  20
    /  \
   15   7
OUTPUT
[
  [15,7],
  [9,20],
  [3]
]

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        sol = {}
        def traversal(node, depth=0):
            if not node:
                return
            traversal(node.left, depth+1)
            if depth in sol:
                sol[depth].append(node.val)
            else:
                sol[depth] = [node.val]
            traversal(node.right, depth+1)
        traversal(root)
        return [arr for key,arr in sorted(sol.items(), key=lambda x: x[0], reverse=True)]
"""
#Time Complexity: O(n) where n is number of nodes in the binary tree.	
# tree_obj = Tree()
# tree_obj.root = Node(1)
# tree_obj.root.left = Node(2)
# tree_obj.root.right = Node(3)
# tree_obj.root.left.left = Node(7)
# tree_obj.root.left.right = Node(6)
# tree_obj.root.right.left = Node(5)
# tree_obj.root.right.right = Node(4)
# tree_obj.reverse_level_order(tree_obj.root)
