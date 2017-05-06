MAX_SIZE = 256
 
def are_anagram(string1, string2):

	#base case
    if len(string1) != len(string2):
        return 0
 
    #two count arrays and initialize all values as 0
    count1 = [0] * MAX_SIZE
    count2 = [0] * MAX_SIZE
 
    # For each character in input strings, increment count
    # in the corresponding count array
    for i in string1:
        count1[ord(i)]+=1
 
    for i in string2:
        count2[ord(i)]+=1
 
    # Compare count arrays
    for i in xrange(MAX_SIZE):
        if count1[i] != count2[i]:
            return 0
 
    return 1