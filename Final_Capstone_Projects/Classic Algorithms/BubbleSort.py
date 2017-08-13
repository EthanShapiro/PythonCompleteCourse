#################################
#   Ethan Shapiro               #
#   Merge Sort                  #
#   Date Created 7/15/2017      #
#   Date Last Edited            #
#################################


class BubbleSort(object):

    def bubble_sort(self, lst):
        swapped = False
        max_len = len(lst)-1
        for i, k in enumerate(lst):
            if i >= max_len:
                break
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if swapped:
            self.bubble_sort(lst)


b = BubbleSort()
l = [10, 1, 15, 20, 2, 4]
b.bubble_sort(l)
print(l)
