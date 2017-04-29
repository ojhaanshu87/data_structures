def sort_list_by_fre(arr):
	sort_arr = sorted(arr, key = arr.count, reverse = True)
	return sort_arr