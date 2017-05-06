#Utility function for reverse_each_words all the characters between a start and end index
def reverse_each_word(arr,start,end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

def reverse_each_word_sentance(arr):
	#step 1: reverse_each_word the entire string
	reverse_each_word(arr,0,len(arr)-1)

	#step 2: reverse_each_word
	start_index = 0
	end_index = 0

	for i in range(0,len(arr)):
		if arr[i] == " ":  #end of word!
			end_index = i-1 #leave the space
			reverse_each_word(arr,start_index,end_index)
			start_index = i+1 #next character!
	#IMPORTANT: Handle last word!
	reverse_each_word(arr,start_index,len(a)-1)