"""
Interviewer — Problem Statement
Given an integer array nums and an integer k, return the k most frequent elements.

You may return the answer in any order.

"""

nums = [1, 1, 1, 2, 2, 3]
k = 2

# # Expected output: [1, 2]
  
  
import heapq

hp = []
heapq.heapify(hp)

m = {}
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    for n in nums:
        if n not in m:
            m[n] = 1
        else:
            m[n] += 1


top_k_frequent(nums, k)
print(m)
