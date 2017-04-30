class Node:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push_elem (self, new_data):
		new_val = Node(new_data)
		new_val.next = self.head
		self.head = new_val
    
	def get_mid_elem(self):
		slow_ptr = self.head
		fast_ptr = self.head
		if (self.head is not None):
			while (slow_ptr and fast_ptr and fast_ptr.next):
				slow_ptr = slow_ptr.next
				fast_ptr = fast_ptr.next.next
			return slow_ptr.val
