# Create dp table of (totalEggs + 1) X (totalFloors + 1)
# Base Case: When egg is zero or one then, set for floor i, table[0][i] = 0; and table[1][i] = i
# Base Case: Floor is zero or one then, set for egg j, table[j][0] = 0 and table[j][1] = 1
# Iterate egg i from 2 to total_eggs
#     Iterate floor j from 2 to total_floors
#         Set table[i][j] = INFINITY
#         Iterate floor k from 1 to j
#             Set maxDrop = 1 + max(table[i-1][k-1], table[i][j-k])
#             If table[i][j] > maxDrop then
#                 Set table[i][j] = maxDrop

INT_MAX = 9999999

def max_floor(eggs, floors):
    #create dp table
    store_table =[[0 for x in range (floors+1)] for x in range (eggs+1)]
    #base case 1
    for egg in range(1, eggs+1):
        store_table[egg][1]=1
        store_table[egg][0]=0
    #base case 2
    for floor in range (1, floors+1):
        store_table[1][floor]=floor
    #iterate over eggs
    for egg in range (2, eggs+1):
        #iterate over floors
        for floor in range (2, floors+1):
            #set table to max value
            store_table[egg][floor]=INT_MAX
            #iterate floor
            for elem in range (1, floor+1):
                max_drop = 1 +max(store_table[egg-1][elem-1], store_table[egg][floor-elem])
                if max_drop < store_table[egg][floor]:
                    store_table[egg][floor]=max_drop
    return store_table[eggs][floors]
