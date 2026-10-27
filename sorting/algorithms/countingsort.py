# Time complexity: O(n + k)
# Space complexity: O(n + k)
# n - number of elements in the input array
# k - largest number in the input array

def countingsort(A):
    n = len(A)
    k = max(A)
    count_array = [0 for _ in range(k+1)]
    result_array = [0 for _ in range(n)]
    for i in range(n):
        count_array[A[i]] += 1
    for i in range(1, k+1):
        count_array[i] += count_array[i-1]
    for i in range(n-1, -1, -1):
        result_array[count_array[A[i]] - 1] = A[i]
        count_array[A[i]] -= 1
    return result_array
#end def
