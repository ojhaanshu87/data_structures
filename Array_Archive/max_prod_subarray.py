class Solution(object):
	def __init__(self, arr):
		self.arr = arr

	def max_prod_subarray(self):
		max_so_far = 1
		max_end_here = 1
		min_end_here = 1
		for elem in range(0, len(self.arr)):
			# if list elem > 0
			if self.arr[elem] > 0:
				max_end_here = max_end_here *self.arr[elem]
				min_end_here = min(min_end_here * self.arr[elem], 1)
			#if list elem equals 0
			if self.arr[elem] == 0:
				max_end_here =1
				min_end_here =1
			#if elem less than 0
			else:
				tmp = max_end_here
				max_end_here = max(min_end_here * self.arr[elem], 1)
				min_end_here = tmp * self.arr[elem]
				if max_so_far < max_end_here:
					max_so_far = max_end_here
		return max_so_far

#if __name__ == '__main__':
#	solution = Solution([1, -2, -3, 0, 7, -8, -2])
#	print solution.max_prod_subarray()
