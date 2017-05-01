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

	def remove_loop_util(self, loop_node):
		ptr1 = self.head
		while(1):
			ptr2 = loop_node
			while (ptr2.next != loop_node and ptr2.next != ptr1):
				ptr2 = ptr2.next
			#if ptr2 reaches ptr1 then loop there and break
			if ptr2.next ==ptr1:
				break
			ptr1 = ptr1.next
		ptr2.next = None

	def detect_and_remove_loop(self):
		slow_ptr = self.head
		fast_ptr = self.head
		while (slow_ptr and fast_ptr and fast_ptr.next):
			slow_ptr = slow_ptr.next
			fast_ptr = fast_ptr.next.next
			if (slow_ptr == fast_ptr):
				self.remove_loop_util(slow_ptr)
				#return 1 show that loop found
				return 1
		#return 0 indicates loop not found
		return 0
