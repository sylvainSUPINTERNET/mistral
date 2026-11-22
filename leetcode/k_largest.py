"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in sorted order, not the kth distinct element.

"""

nums = [3, 2, 1, 5, 6, 4]
k = 2

# Expected: 5


import heapq

ret = []
heapq.heapify(ret)

for n in nums:
    if len(ret) < k:
        heapq.heappush(ret, n)
    else:
        if ret[0] < n:
            heapq.heapreplace(ret, n)

print(ret)