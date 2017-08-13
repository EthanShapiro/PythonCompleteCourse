#################################
#   Ethan Shapiro               #
#   Quick Sort                  #
#   Date Created 7/15/2017      #
#   Date Last Edited            #
#################################

class QuickSort(object):

    def quick_sort(self, lst, low, high):
        """Takes a list and sorts it"""
        if low < high:

            # Get pivot point
            pi = self.partition(lst, low, high)

            self.quick_sort(lst, low, pi-1)
            self.quick_sort(lst, pi+1, high)

    def partition(self, lst, low, high):
        """
        Splits the list by a pivot point
        Swaps high number from right with low number from left
        and returns the pivot point
        """
        # Set pivot index point as median
        pivot = int((low + high) / 2)

        # Swap pivot point with the highest index item
        lst[pivot], lst[high] = lst[high], lst[pivot]

        # Set pivot index to highest
        pivot = high

        # lowest index
        i = low-1

        # Loop through list get left and right highest
        for j in range(low, high):
            if lst[j] <= lst[pivot]:
                # increment lowest index
                i += 1
                # swap current index with higher index
                lst[j], lst[i] = lst[i], lst[j]

        lst[i+1], lst[pivot] = lst[pivot], lst[i+1]

        return i + 1

q = QuickSort()
l = [2, 1, 5, 20, 6, 19]
q.quick_sort(l, 0, len(l)-1)
print(l)