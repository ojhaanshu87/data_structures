class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_k_distance_from_root(root, k):
    if root is None:
        return 0
    if k==0:
        print root.val
    else:
        print_k_distance_from_root(root.left, k-1)
        print_k_distance_from_root(root.right, k-1)

