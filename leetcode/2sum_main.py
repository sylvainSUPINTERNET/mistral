# save in map each num with indice 
# check if the target - current num = something in the map

nums = [2, 7, 11, 15]
target = 9

s = {}

for i, num in enumerate(nums):
    if target - num in s:
        print(num)
        break
    s[num] = i
