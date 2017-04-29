def longest_palindrome(string_elem):
    max_len = 1
 
    start = 0
    length = len(string_elem)
 
    low = 0
    high = 0
 
    # One by one consider every character as center point of 
    # even and length palindromes
    for elem in xrange(1, length):
    # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = elem - 1
        high = elem
        while low >= 0 and high < length and string_elem[low] == string_elem[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
 
        # Find the longest odd length palindrome with center 
        # point as elem
        low = elem - 1
        high = elem + 1
        while low >= 0 and high < length and string_elem[low] == string_elem[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
 
    print "Longest palindrome substring is:",
    print string_elem[start:start + max_len]
 
    return max_len