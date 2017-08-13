# nl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nl[::][0])
#
# for i in range(len(nl)-1, 0-1, -1):
#     nl[::][i]
#
# print(nl[0][2])
# print(nl[::])
# print([sublist[i] for sublist in nl for i in range(len(nl)-1, 0-1, -1)])
#
# n = [['x', 'x'], ['x', 'x']]
#
# if n[::].count(' ') > 0:
#     print("found space")
#
# x = 0
# y = 4
# if x or y < 0 or x or y > 3:
#     print('x or y is less than 0')
#
#
#
# cards = dict.fromkeys(map(str, range(1,14+1)), 0)
#
# print(sorted(['A', '1', '2', 'J']))

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low  --> Starting index,
# # high  --> Ending index
#
# # Function to do Quick sort
# def quickSort(arr, low, high):
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#
# # Python program for implementation of Quicksort Sort
#
# # This function takes last element as pivot, places
# # the pivot element at its correct position in sorted
# # array, and places all smaller (smaller than pivot)
# # to left of pivot and all greater elements to right
# # of pivot
# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low  --> Starting index,
# # high  --> Ending index
#
# # Function to do Quick sort
# def quickSort(arr, low, high):
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#
# # Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i]),
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

arr = [1, 23, 5, 61, 50, 70, 2, 4]
n = len(arr)

# Build a maxheap.
for i in range(n, -1, -1):
    heapify(arr, n, i)
print(arr)