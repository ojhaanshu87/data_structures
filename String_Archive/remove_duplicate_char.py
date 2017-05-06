MAX_SIZE = 256

#convert to array to become mutable, since string is immutable
def to_list(string):
	arr = []
	for elem in string:
		arr.append(elem)
	return arr

#array to string conversion
def to_str(arr):
	return ''.join(arr)


def remove_duplicates(string):
	#define empty hash
	bin_hash =[0]*MAX_SIZE
	#input index set to 0
	input_index = 0
	#result index final set to 0
	result_index = 0

	temp =''

	str_to_list = to_list(string)

	while input_index != len(str_to_list):
		temp = str_to_list[input_index]
		if bin_hash[ord(temp)]==0:
			bin_hash[ord(temp)]=1
			str_to_list[result_index]=str_to_list[input_index]
			result_index +=1
		input_index +=1
	return to_str(str_to_list[0:result_index])
 
