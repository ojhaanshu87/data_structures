class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

#k distance from given node Utility Function
def k_dist_node_down(root, k):
    if root is None or k <0:
        return
    if k==0:
        print root.val
        return

    k_dist_node_down(root.left, k-1)
    k_dist_node_down(root.right, k-1)

def k_distnace_from_given_node(root, k, target):
    if root is None:
        return -1

    if root==target:
        k_dist_node_down(root, k)
        return 0

    left_recur = k_distnace_from_given_node(root.left, k, target)
    if left_recur != -1:
        if left_recur+1 == k:
            print root.val
        else:
            k_dist_node_down(root.right, k-left_recur-2)
        return 1+left_recur

    right_recur = k_distnace_from_given_node(root.right, k, target)
    if right_recur !=-1:
        if right_recur+1 ==k:
            print root.val
        else:
            k_dist_node_down(root.left, k-right_recur-2)
        return 1+right_recur
    return -1