"""
    A simple algorithm can be used:
    1. Sort the intervals based on increasing order of 
    starting time.
2. Push the first interval on to a stack.
3. For each interval do the following
   a. If the current interval does not overlap with the stack 
       top, push it.
   b. If the current interval overlaps with stack top and ending
       time of current interval is more than that of stack top, 
       update stack top with the ending  time of current interval.
4. At the end stack contains the merged intervals.
    """

def merged_interval(intervals):
	sorted_by_lower_bound = sorted(intervals, key = lambda tup:tup[0])
	merged =[]
	for higher in sorted_by_lower_bound:
		if not merged:
			merged.append(higher)
		else:
			lower = merged[-1]
			if higher[0] <= lower[1]:
				upper_bound = max (lower[1], higher[1])
				merged[-1] = (lower[0], upper_bound)
			else:
				merged.append(higher)
	return merged

l = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]
print("Original list of ranges: {}".format(l))
merged_list = merged_interval(l)
print("List of ranges after merge_ranges: {}".format(merged_list))