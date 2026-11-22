"""
You are given an array of k sorted linked lists, each sorted in ascending order.

Merge all the linked lists into one sorted linked list and return its head.
"""

import heapq

lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

# Expected: [1, 1, 2, 3, 4, 4, 5, 6]

ret = []
heapq.heapify(ret)

def merge_k_lists(lists: list[list[int]]) -> list[int]:
    for l in lists:
        heapq.heappush(ret, l[0])
                
merge_k_lists(lists)

print(ret)
