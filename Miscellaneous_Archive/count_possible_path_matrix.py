'''
The problem is to count all the possible paths from top left to bottom right 
of a mXn matrix with the constraints that from each cell you can either move only to right or down

Approach:

Returns count of possible paths to reach cell at row number m and column
number n from the topmost leftmost cell (cell at 1, 1)

fact ((m-1 + n-1))/ fact((m-1))* fact((n-1)) 
'''

def factorial(num):
	if num ==0 or num == 1:
		return 1
	if num <0:
		print "negative number not allowed"
	else:
		return num * factorial(num-1)

def possible_path (row_matrix, column_matix):
	return factorial(row_matrix-1 +column_matix-1) / (factorial(row_matrix-1) * 
		factorial(column_matix-1)) 


