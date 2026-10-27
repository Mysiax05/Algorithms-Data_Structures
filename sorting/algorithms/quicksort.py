# Average time complexity: O(nlogn)
# Worst case time complexity: O(n^2)
# Space complexity: O(logn)
# n - number of elements in the input array

from random import randint

def partition(A, p, r):
    pivot_idx = randint(p, r)
    pivot = A[pivot_idx]
    A[r], A[pivot_idx] = A[pivot_idx], A[r]
    i = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i
#end def

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
#end def
