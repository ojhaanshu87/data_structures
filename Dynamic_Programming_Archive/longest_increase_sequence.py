def longest_increase_seq (arr):
	len_arr = len(arr)
	lis = [1]*len_arr
	for elem in range (1, len_arr):
		for elem1 in range (0, elem):
			if (arr[elem] > arr[elem1] and lis[elem] < lis[elem1]+1):
				lis[elem] = lis[elem1]+1
	max_elem =0
	for elem in range (0, len_arr):
		max_elem = max(max_elem, lis[elem])
	return max_elem