class Solution(object):
	def __init__(self, sentence):
		self.sentence = sentence

	def reverse(self):
	    #Tokenise each word
		token = self.sentence.split(' ')
		#calculate length of word
		length = len(token)
		#iterate through the length
		for elem in range(length/2):
			#make temproray veriable to store each word and reverse till loop complete
			temp = token[elem]
			token[elem] = token[length-elem-1]
			token[length-elem-1] = temp

		return ' '.join([x for x in token])

if __name__=='__main__':
    solution = Solution("how are you")
    print solution.reverse()
