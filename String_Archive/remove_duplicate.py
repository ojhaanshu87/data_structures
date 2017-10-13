class Solution(object):
	def __init__(self, string):
		self.string = string

	def remove_dups(self):
		dict = {}
		non_repeat = ""
		for char in self.string:
			if char not in dict:
				non_repeat += char
				if ord(char.lower()) >= ord('a') and ord(char.lower()) <= ord('z'):
					dict[char] = 1

		return non_repeat
 