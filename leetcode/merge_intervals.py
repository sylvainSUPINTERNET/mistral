"""
Énoncé : on te donne une liste d'intervalles [start, end]. Tu dois fusionner tous ceux qui se chevauchent.
"""

intervals = [
    [1, 3],
    [2, 6],
    [5, 9],
    [15, 18]
]


# Considering intervals is sorted by start time
# parcours O(n log n) si on doit trier les intervalles avant, sinon O(n) si déjà trié
def merge_intervals(intervals) -> list[list[int]]:

    result = []

    for i in range(len(intervals)):
        x = intervals[i][len(intervals[i])-1]

        if i+1 < len(intervals) and x >= intervals[i+1][0]:
            intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0])
            intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result
        

result = merge_intervals(intervals)
print(result)


intervals = [[1, 10], [2, 6]]
result_2 = merge_intervals(intervals)
print(result_2)