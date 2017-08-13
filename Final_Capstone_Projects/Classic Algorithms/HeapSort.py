# ----------------------------------
#   Ethan Shapiro
#   Heap Sort
#   Date Created 7/15/2017
#   Date Last Edited
# ----------------------------------


def heapify(arr, n, i):
    # set largest as parent
    largest = i

    # set left and right child indices
    l = i*2 + 1
    r = i*2 + 2

    # Check if left child is largest
    # and exists
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child is largest
    # and exists
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If child is larger than root, swap root and heapify root
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify root
        heapify(arr, n, largest)


l = [1, 23, 5, 61, 50, 70, 2, 4]
def heap_sort(arr):
    loop_len = int((len(arr)-1)/2)
    n = len(arr)

    # max heap array
    for i in range(loop_len, -1, -1):
        heapify(arr, n, i)
    print(arr)
    # Sort
    for i in range(0, n):
        heapify(arr, n-i, 0)
        arr[0], arr[(n-1)-i] = arr[(n-1)-i], arr[0]

heap_sort(l)


