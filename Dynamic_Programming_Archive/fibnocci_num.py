fib_arr =[0,1]

def febno(num):
	if num < 0:
		return -1
	elif num <= len(fib_arr):
		return fib_arr[num-1]
	else:
		temp_vble = febno(num-1)+febno(num-2)
		fib_arr.append(temp_vble)
		return temp_vble