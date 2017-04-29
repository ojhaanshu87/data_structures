def largest_possible_num(arr):

	for i in range(len(arr)-1):
	    for j in range(i+1, len(arr)):
	        if arr[i]+arr[j] < arr[j]+arr[i]:
	            arr[i], arr[j] = arr[j], arr[i]  #Swaping elements
	return ''.join(arr)

a = ["61","59", "62"]
print largest_possible_num(a)
#One Line Solution
# def arrange(arr):
# 	return ''.join(sorted(arr, cmp=lambda x, y: cmp(y + x, x + y)))
