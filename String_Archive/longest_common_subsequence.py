class LongestCommonSequence(object):
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2

	def get_len_lcs(self):  
	    len_str1, len_str2 = len(self.str1), len(self.str2)  
	    dp_table = [[0]*(len_str2+1) for i in xrange(len_str1+1)]
	    for i in range(len_str1+1): 
	        for j in range(len_str2+1): 
	            if i == 0 or j == 0 : 
	                dp_table[i][j] = 0
	            elif str1[i-1] == str2[j-1]: 
	                dp_table[i][j] = dp_table[i-1][j-1]+1
	            else: 
	                dp_table[i][j] = max(dp_table[i-1][j] , dp_table[i][j-1]) 
	    return dp_table[len_str1][len_str2]

str1 = "abcdaf"
str2 = "acbcf"
print LongestCommonSequence(str1, str2).get_len_lcs()
