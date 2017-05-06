def to_str(arr):
	return ''.join(arr)

def permute_all(arr, start_ind, end_ind):
	if (start_ind==end_ind):
		print to_str(arr)
	else:
		for elem in range (start_ind, end_ind+1):
			arr[end_ind], arr[start_ind] = arr[start_ind], arr[end_ind]
			permute_all(arr, end_ind+1, start_ind)
			#backtracking
			arr[end_ind], arr[start_ind] = arr[start_ind], arr[end_ind]

