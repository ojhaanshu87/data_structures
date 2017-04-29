def seg_0_1(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        while (arr[left]==0 and left < right):
            left +=1
        while (arr[right]==1 and left < right):
            right -=1
        if (left < right):
            arr[left]=0
            arr[right]= 1
            left +=1
            right -=1

def print_arr(arr):
    for elem in range (0, len(arr)):
        print arr[elem]