class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def level_order(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print queue[0].val,
        node = queue.pop(0)
       #Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)