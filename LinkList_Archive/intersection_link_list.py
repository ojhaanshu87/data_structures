class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push_elem (self, new_data):
        new_val = Node(new_data)
        new_val.next = self.head
        self.head = new_val

    def print_list(self):
        temp = self.head
        while temp:
            print temp.val
            temp = temp.next

    def get_intersection (self, head1, head2):
        curr1, curr2 = head1, head2
        len1, len2 = 0, 0
        while curr1 is not None:
            len1 +=1
            curr1 = curr1.next
        while curr2 is not None:
            len2 +=1
            curr2 = curr2.next
        curr1, curr2 = head1, head2
        if len1 > len2:
            for elem in range (len1-len2):
                curr1 = curr1.next
        elif len2 > len1:
            for elem in range (len2-len1):
                curr2 = curr2.next
        while curr2 <> curr1:
            curr2 = curr2.next
            curr1 = curr1.next
        return curr1

