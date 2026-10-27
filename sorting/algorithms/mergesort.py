# Time complexity: O(nlogn)
# Space complexity: O(n)
# n - number of elements in the input array

def merge(A, p, q, r):
    T = A[p:r+1]
    n1 = q - p + 1
    n2 = r - q
    i, j, k = 0, n1, p
    while i < n1 and j < n1 + n2:
        if T[i] <= T[j]:
            A[k] = T[i]
            i += 1
        else:
            A[k] = T[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = T[i]
        i += 1
        k += 1
    while j < n1 + n2:
        A[k] = T[j]
        j += 1
        k += 1
#end def

def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
#end def
