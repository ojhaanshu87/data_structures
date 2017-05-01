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

	def reverse_k_size(self,head, k):
		prev = None
		curr = head
		next = None
		count = 0
		while (curr is not None and count < k):
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
			count +=1
		if next is not None:
			head.next = self.reverse_k_size(next, k)
		return prev