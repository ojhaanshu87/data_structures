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

	def print_elem (self):
		temp = self.head
		while (temp):
			print temp.val
			temp = temp.next

	def reverse_list (self):
		prev = None
		curr = self.head
		while (curr is not None):
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev
