# Average time complexity: O(n + k)
# Worst case time complexity: O(n^2) (when all elements land in one bucket)
# Space complexity: O(n + k)
# n - number of elements in the input array
# k - quantity of buckets used during sorting

from insertionsort import insertionsort

def bucketsort(A, quantity):
    n = len(A)
    max_val = max(A)
    min_val = min(A)
    result = []
    if max_val == min_val:
        return A[0:n]
    buckets = [[] for _ in range(quantity)]
    for num in A:
        idx = int((num - min_val) / (max_val - min_val) * (quantity-1))
        idx = max(0, min(quantity-1, idx))
        buckets[idx].append(num)
    for bucket in buckets:
        insertionsort(bucket)
        for num in bucket:
            result.append(num)
    return result
#end def
