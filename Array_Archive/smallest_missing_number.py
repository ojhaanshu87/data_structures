# Examples
# Input: {0, 1, 2, 6, 9}, n = 5, m = 10
# Output: 3

# Input: {4, 5, 10, 11}, n = 4, m = 12
# Output: 0

# Input: {0, 1, 2, 3}, n = 4, m = 5
# Output: 4

# Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
# Output: 8

#modified B-Search method. This method doesn’t work if there are duplicate elements in the array.

def missing_number(arr, start, end):
	start = 0
	end = len(arr)-1
	mid = (start + end) / 2

	if (start > end):
		return end+1

	if (start != arr[start]):
		return start

	if (arr[mid]==mid):
        return missing_number(arr, mid+1, end)

    return missing_number(arr, start, mid)