class Solution(object):
	def __init__(self, string):
		self.string = string

	def first_non_repeat(self):
		#define empty dictionary
		dict = {}
		#define empty array
		non_repeat_char = []
		#traverse String
		for char in self.string:
			#check each char present
			if char in dict:
				dict[char] +=1
			else:
				dict[char] = 1
				#if previously no present then append in empty array
				non_repeat_char.append(char)
		#traverse array
		for elem in non_repeat_char:
			if dict[elem] == 1:
				return elem
		return None