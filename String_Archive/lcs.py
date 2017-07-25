class Solution(object):
	def __init__(self, string1, string2):
		self.string1 =string1
		self.string2 = string2

	def get_lcs(self):
		#calculate length of LCS
		len_1 = len(self.string1)
		len_2 = len(self.string2)
		#create dynamic programming table to store the values
		dp_table = [[None]*(len_2+1) for elem in range(len_1+1)]
		for i in range(len_1+1):
			for j in range(len_2+1):
				if i==0 or j==0:
					dp_table[i][j]=0
				elif self.string1[i-1] == self.string2[j-1]:
					dp_table[i][j] = 1 + dp_table[i-1][j-1]
				else:
					#it gives total length of lcs
					dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

		#print LCS value
		index = dp_table[len_1][len_2]
		#define character array
		lcs_string = [""]*(index+1)
		lcs_idx = ["\0"]
		#start from bottom rightand store char in lcs_string
		i =len_1
		j = len_2
		while i>0 and j>0:
			#if current char in str_1[] and str_2 are same then it is part of lcs
			if self.string1[i-1] == self.string2[j-1]:
				lcs_string[index-1] = self.string1[i-1]
				i -=1
				j -=1
				index -=1
			#if not same then find larger of two and go to direction of larger value
			elif (dp_table[i-1][j] > dp_table[i][j-1]): 
				i -=1
			else:
				j -=1
		return ''.join(lcs_string) 


# if __name__ =='__main__':
# 	solution = Solution("str1", "str2")
# 	print solution.get_lcs()
 # Time Complexity : O(len(str1) * len(str2))