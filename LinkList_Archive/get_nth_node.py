class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push_elem(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def get_nth_node(self, nth_index):
        curr = self.head
        count =0
        while (curr):
            if (count==nth_index):
                return curr.val
            count +=1
            curr = curr.next
        assert(False)
        return 0