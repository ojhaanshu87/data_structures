class Solution(object):
	def __init__(self, string):
		self.string = string

	def remove_dups(self):
		max_count = 0
		#includes the charcters in dict which have count 1 only
		single_chars =[]
		# since we need to remove multiple entry and store as single char
		#e.g. aaaaa should be append as 'a'
		multiple_chars = []
		for char in set(list(self.string)):
			count = list(self.string).count
			if count == 1:
				max_count = count
				multiple_chars.append(char)

			else:
				single_chars.append(char)

		return single_chars + multiple_chars
 
