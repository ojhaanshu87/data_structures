def swap(arr,elem1,elem2):
    arr[elem1],arr[elem2] = arr[elem2],arr[elem1]

def zig_zag(arr):
    for elem in range(len(arr)-1):
        if not elem&1:
            if arr[elem] > arr[elem+1]:
                swap(arr,elem,elem+1)
        elif arr[elem] < arr[elem+1]:
            swap(arr,elem,elem+1)
    return arr