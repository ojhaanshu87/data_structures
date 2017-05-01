class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #insert into list
    def push_elem(self, new_data):
        new_val = Node(new_data)
        new_val.next=self.head
        self.head = new_val

    #print element of link list
    def print_list(self):
        curr  = self.head
        while curr:
            print curr.val
            curr= curr.next
            
    #remove duplicates from unsorted list elemnt
    def remove_dups_unsorted(self):
        curr = second = self.head
        while curr is not None:
            while second.next is not None:
                if second.next.val == curr.val:
                    second.next = second.next.next
                else:
                    second = second.next
            curr = second = curr.next