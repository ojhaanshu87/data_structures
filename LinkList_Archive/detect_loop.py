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

	def detect_loop (self):
		slow_ptr =self.head
		fast_ptr = self.head
		while (fast_ptr and slow_ptr and fast_ptr.next):
			slow_ptr = slow_ptr.next
			fast_ptr = fast_ptr.next.next
			if fast_ptr == slow_ptr:
				print "loop found"
				return
 