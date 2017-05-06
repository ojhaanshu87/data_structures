# Source http://www.geeksforgeeks.org/lexicographic-rank-of-a-string/

def factorial(num):
	if(num<=1): 
		return 1
	return (num*factorial(num-1))

def lexiographic_order(string):
	order=0
	to_list=list(string)
	to_list.sort()
	for i in range(0,len(string)):
		for j in range(0,len(to_list)):
			if string[i]==to_list[j]:
				order+=j*factorial(len(to_list)-1)
				to_list.remove(to_list[j])
				break;
	order+=1
	return order
