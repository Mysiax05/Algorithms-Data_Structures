# Time complexity: O(n^2)
# Space complexity: O(1)
# n - number of elements in the input array

def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        current = A[i]
        j = i
        while j > 0 and A[j-1] > current:
            A[j] = A[j-1]
            j -= 1
        A[j] = current
#end def
