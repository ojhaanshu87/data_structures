'''
Dynamic programming Approach:

if input[i] == input[j]:
	T[i][j] = T[i+1][j-1]+2
else:
	T[i][j] = max(T[i+1][j], T[i][j-1])
'''

class Solution(object):
	def __init__(self, string):
		self.string = string

	def get_lps(self):
		len_string = len(self.string)
		#create dynamic programming table
		dp_table = [[0 for x in range(len_string)] for x in range(len_string)]
		#string of length one is one
		for elem in range(len_string):
			dp_table[elem][elem]=1
		#fill dynamic programming matrix is like matrix chain multiplication
		for elem in range(2, len_string+1):
			for i in range (len_string-elem+1):
				j = i+elem-1
				if (self.string[i] == self.string[j] and elem ==2):
					dp_table[i][j] = 2
				elif self.string[i] == self.string[j]:
					dp_table[i][j] = dp_table[i+1][j-1]+2
				else:
					dp_table[i][j] = max (dp_table[i+1][j], dp_table[i][j-1])

		return dp_table[0][len_string-1]

if __name__ =='__main__':
	solution = Solution("somestring")
	print solution.get_lps()
#Time Complexity of the above implementation is O(n^2)