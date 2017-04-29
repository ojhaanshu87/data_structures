class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to find min and max distances with
# respect to root
def find_min_max(root, minimum, maximum, hd):

    # Base Case
    if root is None:
        return

    # Update min and max
    if hd < minimum[0] :
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    # Recur for left and right subtrees
    find_min_max(root.left, minimum, maximum, hd-1)
    find_min_max(root.right, minimum, maximum, hd+1)

# A utility function to print all roots on a given line_no
# hd is horizontal distance of current root with respect to root
def print_vert_line(root, line_no, hd):

    # Base Case
    if root is None:
        return

    # If this root is on the given line number
    if hd == line_no:
        print root.val,

    # Recur for left and right subtrees
    print_vert_line(root.left, line_no, hd-1)
    print_vert_line(root.right, line_no, hd+1)

def vertical_order(root):

    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    find_min_max(root, minimum, maximum, 0)

    # Iterate through all possible lines starting
    # from the leftmost line and print roots line by line
    for line_no in range(minimum[0], maximum[0]+1):
        print_vert_line(root, line_no, 0)
        print

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)

vertical_order(root)