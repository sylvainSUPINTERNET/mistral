"""
Exercise — Sort an Array
Interviewer:

Given an array of integers, implement Merge Sort without using sorted() or .sort().

Your algorithm must achieve O(n log n) worst-case time complexity.

nums = [8, 3, 5, 1, 9, 2, 7]

# Expected
# [1, 2, 3, 5, 7, 8, 9]

"""

nums = [8, 3, 5, 1]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    print(f"l : {left}");
    right = merge_sort(nums[mid:])
    print(f"r : {right}")

    # return merge(left, right)

merge_sort(nums)