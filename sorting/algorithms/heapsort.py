# Time complexity: O(nlogn)
# Space complexity: O(1)
# n - number of elements in the input array

def parent(i):
    return (i-1)//2
#end def

def left(i):
    return 2*i + 1
#end def

def right(i):
    return 2*i + 2
#end def

def heapify(A, n, i):
    while True:
        l, r, max_idx = left(i), right(i), i
        if l < n and A[l] > A[max_idx]:
            max_idx = l
        if r < n and A[r] > A[max_idx]:
            max_idx = r
        if max_idx != i:
            A[i], A[max_idx] = A[max_idx], A[i]
            i = max_idx
        else:
            break
#end def

def build_max_heap(A, n):
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)
#end def

def heapsort(A):
    n = len(A)
    build_max_heap(A, n)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
#end def
