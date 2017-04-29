class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#distance between two keys util function
def dist_from_root(root, elem, k):
    global distance
    if root is None:
        return 0
    if root.val == elem:
        distance = k
    else:
        dist_from_root(root.left, elem, k+1)
        dist_from_root(root.right,elem,  k+1)

def lca_binary_tree(root, elem1, elem2):
    if root is None:
        return 0
    if root.val==elem1 or root.val==elem2:
        return root.val
    left_lca = lca_binary_tree(root.left, elem1, elem2)
    right_lca = lca_binary_tree(root.right, elem1, elem2)
    if left_lca and right_lca:
        return root.val
    else:
        return left_lca if left_lca else right_lca

distance = 0
def dist_bw_two_keys(root, elem1, elem2):
    global distance
    lca_elem = lca_binary_tree(root, elem1, elem2)
    dist_from_root(root, elem1,0)
    dist_elem1 = distance
    dist_from_root(root, elem2, 0)
    dist_elem2 = distance
    dist_from_root(root, lca_elem, 0)
    lca_elem_dist = distance
    return dist_elem1 + dist_elem2 - 2*lca_elem_dist
