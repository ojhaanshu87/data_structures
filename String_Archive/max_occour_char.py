MAX_SIZE = 256
def max_occour_char(string):
	#initialise count to zero
	count = [0]*MAX_SIZE
	#define initially max as -1
	max_count = -1
	char = ''
	for elem in string:
		count[ord(elem)] +=1
	for elem in string:
		if max_count < count[ord(elem)]:
			max_count = ord(elem)
			char = elem
	return char