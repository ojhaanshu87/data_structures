class Solution(object):
	def __init__(self, string):
		self.string = string

	def max_repeat_char(self):
		#define empty dictionary
		dict = {}
		#traverse String
		for char in self.string:
			if char in dict:
				dict[char] +=1
			else:
				dict[char] = 1

		return max(zip(dict.keys(), dict.values()), key=lambda k : k[1])[0]
