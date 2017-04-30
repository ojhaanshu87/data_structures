def longest_common_substr(str1,str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    store_table = [[0]*(len_str2+1) for x in range(len_str1+1)]
    longest = 0
    lcs_set = set()
    for elem in range(len_str1):
        for elem1 in range(len_str2):
            if str1[elem] == str2[elem1]:
                c = store_table[elem][elem1] + 1
                store_table[elem+1][elem1+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(str1[elem-c+1:elem+1])
                elif c == longest:
                    lcs_set.add(str1[elem-c+1:elem+1])

    return lcs_set