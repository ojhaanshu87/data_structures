MAX_ELEM = 1000

def pair_sum(arr, target):
	bin_hash = [0]*MAX_ELEM
	for elem in range (0, len(arr)):
		temp = target-arr[elem]
		if (temp >=0 and bin_hash[temp]==1):
			print "Pair with the given sum is", arr[elem], "and", temp
		bin_hash[arr[elem]]=1
