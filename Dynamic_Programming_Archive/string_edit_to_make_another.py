def edit_str(str1, str2, len_str1, len_str2):
    # aux table to store result
    store_table = [[0 for x in range(len_str2+1)] for x in range(len_str1+1)]
 
    # fill table in bottom up manner
    for elem in range(len_str1+1):
        for elem1 in range(len_str2+1):
 
            # If first string is empty, remove all from second string
            if elem == 0:
                store_table[elem][elem1] = elem1
 
            # If second string is empty, remove all from first string
            elif elem1 == 0:
                store_table[elem][elem1] = elem
 
            # If last characters are same, then ignore the last and process for same
            elif str1[elem-1] == str2[elem1-1]:
                store_table[elem][elem1] = store_table[elem-1][elem1-1]
 
            # If last character are different, consider all possibility
            else:
                store_table[elem][elem1] = 1 + min(store_table[elem][elem1-1],        # Insert
                                   store_table[elem-1][elem1],        # Remove
                                   store_table[elem-1][elem1-1])    # Replace
 
    return store_table[len_str1][len_str2]