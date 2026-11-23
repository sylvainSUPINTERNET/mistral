"""
Interviewer — Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements.

You may return the answer in any order.

"""

import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2

# Expected output: [1, 2]

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    m = {}

    # Step 1 : Count frequencies — O(n)
    for n in nums:
        if n not in m:
            m[n] = 1
        else:
            m[n] += 1

    # Step 2 : Maintain a min-heap of size K
    heap = []

    for value, freq in m.items():

        if len(heap) < k:
            heapq.heappush(heap, (freq, value))

        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, value))

    # Step 3 : Extract the K most frequent elements
    return [value for freq, value in heap]


result = top_k_frequent(nums, k)
print(result)  # [2, 1]