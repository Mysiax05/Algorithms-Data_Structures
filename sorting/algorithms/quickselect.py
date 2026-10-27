# Average time complexity: O(n)
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
    A[r], A[i] = A[i], A[r]
    return i
#end def

def quickselect(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    left_size = q - p + 1
    if k == left_size:
        return A[q]
    if k < left_size:
        return quickselect(A, p, q-1, k)
    else:
        return quickselect(A, q+1, r, k - left_size)
#end def
