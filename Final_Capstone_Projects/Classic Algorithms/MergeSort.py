#################################
#   Ethan Shapiro               #
#   Merge Sort                  #
#   Date Created 7/15/2017      #
#   Date Last Edited            #
#################################


class MergeSort(object):
    """A class that merge sorts a list of integers or strings"""

    def merge(self, lst, l, m, r):
        # Length of both sides
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = lst[l + i]

        for j in range(0, n2):
            R[j] = lst[m + 1 + j]

        # Sort arrays
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

            # Copy the remaining elements of L[], if there
            # are any
        while i < n1:
            lst[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            lst[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, lst, l, r):
        """Sort a list of integers"""
        if l < r:
            # Get the middle of list
            m = int((l+(r-1))/2)

            # Call itself until everything is lowest unit
            self.sort_ints(lst, l, m)
            self.sort_ints(lst, m+1, r)
            self.merge(lst, l, m, r)
