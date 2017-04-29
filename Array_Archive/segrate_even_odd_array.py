def seg_even_odd_array(arr):
	left, right = 0, len(arr)-1
	while (left < right):
		while (arr[left]%2==0 and left <right):
			left +=1
		while (arr[right]%2==1 and left <right):
			right -=1
		while (left < right):
			arr[left], arr[right] = arr[right], arr[left]
			left +=1
			right -=1


def print_arr(arr):
    for elem in range (0, len(arr)):
        print arr[elem]
