''' 
A) Conver number to Binary
B) Count 1's in Binary conversion
C) If Single 1 found in count return True else return False 

Alternatively :

if bin(num and (num-1) == 0) return TRUE else return FALSE
'''

#Number to Binary ITERATIVE Approach
def decimal_to_binary(num):
	quot = int(num)
	base = 0
	counter = 0
	binary=[]
	while (quot > 0):
		rem = quot%2
		binary.append(str(rem))
		quot = quot//2
		counter +=1

	binary.reverse()
	return(int(''.join(binary)))

#Number to Binary RECURSIVE Approach
# def decimal_to_binary_rec (num):
# 	if num > 1:
# 		decimal_to_binary_rec(num/2)
# 	print (num%2),

#count 1's in binary number
def counts_ones_in_binary_conversion(num):
	binary_num_input =decimal_to_binary(num)
	count_one =0
	for elem in str(binary_num_input):
		if elem == '1':
			to_int = int(elem)
			count_one += 1
	return count_one 

def is_power_of_two(num):
	ones_count = counts_ones_in_binary_conversion(num)
	if num > 0 and ones_count == 1:
		return True
	else:
		return False


