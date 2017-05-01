##########################################################
#reverse first half
#compare with secod half
#if both same return True else return False
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

    def is_palindrome(self):
        rev, fast_ptr = None, self.head
        #reverse first half of list
        while (fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            self.head.next, rev, self.head = rev, self.head, self.head.next
        #if link list length is odd, set the head as next to median node
        tail = self.head if fast_ptr else self.head
        #compare reverse first half with second half and restore the reverse first half
        is_pal = True
        while rev:
            is_pal = is_pal and rev.val = tail.val
            rev.next, self.head, rev = self.head, rev, rev.next
        return is_pal