"""
Given a string s, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.
"""

# abcabcbb => 3 subs

from collections import deque
import heapq
from typing import Any


def length_of_longest_substring(s: str) -> int:
    max_length = 0
    window = deque()
    seen = set()

    for c in s:
        while c in seen:
            removed = window.popleft()
            seen.remove(removed)

        window.append(c)
        seen.add(c)

        max_length = max(max_length, len(window))

    return max_length

# def length_of_longest_substring(s: str) -> list:
#     ret = []
#     window = deque()
#     tmp = {}

#     for c in s:
#         if c not in tmp:
#             tmp[c] = False
#             window.append(c)
#         else:
#             while c in tmp:
#                 removed = window.popleft()
#                 tmp.pop(removed, None)

#             window.append(c)
#             tmp[c] = False
#         ret.append("".join(window))

#     return ret

# s = "abcabcbb"
# result = length_of_longest_substring(s)
# print(result)
