class Node :
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push_elem(self, new_data):
		new_val = Node(new_data)
		new_val.next = self.head
		self.head = new_val

	def print_list(self):
		temp = self.head
		while temp:
			print temp.val
			temp = temp.next

	def pair_swap(self):
		temp = self.head
		if temp is None:
			return 0
		while (temp is not None and temp.next is not None):
			temp.val, temp.next.val = temp.next.val, temp.val
			temp = temp.next.next