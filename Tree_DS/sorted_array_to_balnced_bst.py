# Time:  O(n)
# Space: O(logn)
#
# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.


#ALGORITHM

# 1) Get the Middle of the array and make it root.
# 2) Recursively do same for left half and right half.
#       a) Get the middle of left half and make it left child of the root
#           created in step 1.
#       b) Get the middle of right half and make it right child of the
#           root created in step 1.




# Definition for a  binary tree node
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Tree:

    @staticmethod
    def perfect_tree_pivot(n):
        """
        Find the point to partition n keys for a perfect binary search tree
        """
        x = 1
        # find a power of 2 <= n//2
        # while x <= n//2:  # this loop could probably be written more elegantly :)
        #     x *= 2
        x = 1 << (n.bit_length() - 1)  # use the left bit shift, same as multiplying x by 2**n-1

        if x // 2 - 1 <= (n - x):
            return x - 1  # case 1: the left subtree of the root is perfect and the right subtree has less nodes
        else:
            return n - x // 2  # case 2 == n - (x//2 - 1) - 1 : the left subtree of the root
                               # has more nodes and the right subtree is perfect.
    

    def sorted_array_to_bst_recu(self, num, start, end):
        if start == end:
            return None
        mid = start + self.perfect_tree_pivot(end - start)
        node = TreeNode(num[mid])
        node.left = self.sorted_array_to_bst_recu(num, start, mid)
        node.right = self.sorted_array_to_bst_recu(num, mid + 1, end)
        return node


    # @param num, a list of integers
    # @return a tree node
    def sorted_array_to_bst(self, num):
        return self.sorted_array_to_bst_recu(num, 0, len(num))

if __name__ == "__main__":
    num = [1, 2, 3]
    result = Tree().sorted_array_to_bst(num)
    print result.val
    print result.left.val
print result.right.val