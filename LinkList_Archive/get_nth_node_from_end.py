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
   
	def nth_elem_from_end (self, target):
		main_ptr = self.head
		ref_ptr = self.head
		count = 0
		if (self.head is not None):
			while (count < target):
				if (ref_ptr is None):
					print ("%d is greater than list count" %(target))
					return
				ref_ptr = ref_ptr.next
				count +=1

		while (ref_ptr is not None):
			main_ptr = main_ptr.next
			ref_ptr = ref_ptr.next

		print ("Node %d from last is %d" %(target, main_ptr.val))

#alternative method is to count the elemnt in LinkedList and then apply (len-target-1)