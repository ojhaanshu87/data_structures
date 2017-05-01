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

	def reverse_alternate_k_size(self,head, k):
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

        #Now head points to the kth node.  So change next of head to (k+1)th node
		if head is not None:
			head.next = curr
        # do not want to reverse next k nodes. So move the current pointer to skip next k nodes 
		count = 0
		while (count < k-1 and curr is not None):
			curr = curr.next
			count +=1
        #Recursively call for the list starting from current->next. And make rest of the list as next of first node 
		if curr is not None:
			curr.next = self.reverse_alternate_k_size(curr.next, k)

        #prev is new head of the input list
		return prev


