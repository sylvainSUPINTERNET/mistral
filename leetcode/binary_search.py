"""
Exercise — Binary Search
Interviewer:

Given a sorted array of distinct integers nums and an integer target, return the index of target.

If the target doesn't exist, return -1.

Your solution must run in O(log n) time.

"""

nums = [-1, 0, 3, 5, 9, 12]
target = 9

# Considering the nums entry is sorted ASC
def binary_search(nums, target):
    idx_left = 0
    idx_right = len(nums) - 1

    while idx_left <= idx_right:
        mid = (idx_left+idx_right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            idx_right = mid - 1

        if nums[mid] < target:
            idx_left = mid + 1
    
    return -1


i = binary_search(nums, target)
print(i)

# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# x = binary_search(nums, target)
# if x != -1:
#     print(f"{nums[x]}")