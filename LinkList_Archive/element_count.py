class Node:
	def __init__ (self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__ (self):
		self.head = None

	def push_elem (self, new_data):
		new_val = Node(new_data)
		new_val.next = self.head
		self.head = new_val

	def count_elem(self):
		count =0
		while (self.head):
			self.head = self.head.next
			count +=1
		return count