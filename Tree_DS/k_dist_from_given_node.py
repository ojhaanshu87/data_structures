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
    #Base Case 1
    if root is None:
        return -1
    #Base Case 2 
    # If target is root then print all downward nodes
    if root==target:
        k_dist_node_down(root, k)
        return 0
    # Recur for left subtree
    left_recur = k_distnace_from_given_node(root.left, k, target)
    # Check if target node was found in left subtree
    if left_recur != -1:
        # If root is at distance k from target, print root
        # Note: left_recur is distance of root's left child from target
        if left_recur+1 == k:
            print root.val
        # Else go to right subtreee and print all k-left_recur-2 distant nodes
        # Note: that the right child is 2 edges away from left chlid
        else:
            k_dist_node_down(root.right, k-left_recur-2)
        # Add 1 to the distance and return value for for parent calls
        return 1+left_recur
    
    # Similar Recur for right subtree (as last 26-39 line number for left subtree)
    right_recur = k_distnace_from_given_node(root.right, k, target)
    if right_recur !=-1:

        if right_recur+1 ==k:

            print root.val

        else:
            k_dist_node_down(root.left, k-right_recur-2)

        return 1+right_recur
    # If target was neither present in left nor in right subtree    
    return -1