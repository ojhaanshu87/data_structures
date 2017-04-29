#max path sum
#k distance from leaf
#inorder without recursion and stack
#build tree using inorder and (pre or post) order
#binaryTree to DLL

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key




# # Driver code
# root = root(10)
# root.left      = root(8)
# root.right     = root(2)
# root.left.left  = root(4)
# root.left.right  = root(5)
#
# print "Preorder traversal of binary tree is"
# preorder(root)
#
# print "\nSize of the tree is %d" %(size_tree(root))
#
# print "\ndepth of the tree is %d" %(max_depth(root))
#
# print "\nroot to leaf in single line"
# print leaf_to_path(root)
#
# print "\nLevel Order Traversal of binary tree is -"
# level_order(root)
#
# if children_sum(root):
#     print "\nnot satisfy childeren sum"
# else:
#     print "\nsatisfy children sum"
#
# mirror_tree(root)
# print "\nPreorder traversal of binary tree after mirror is"
# preorder(root)
#
# convert_to_sum_tree(root)
# print "\nPreorder traversal after sum property is"
# preorder(root)
#





# # Driver program to test above function
# root = root(20)
# root.left = root(8)
# root.right = root(22)
# root.left.left = root(4)
# root.left.right = root(12)
# root.left.right.left = root(10)
# root.left.right.right = root(14)
# target = root.left
# k_distnace_from_given_root(root, 2, target)


# Driver program to test above function
# root = root(20)
# root.left = root(8)
# root.right = root(22)
# root.left.left = root(4)
# root.left.right = root(12)
# root.left.right.left = root(10)
# root.left.right.right = root(14)
# target = root.right
# #k_distnace_from_given_root(root, 4, target)
# #dist_from_root(root, 12, 0)
# print dist_bw_two_keys(root, 20, 22)
# #print distance


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
