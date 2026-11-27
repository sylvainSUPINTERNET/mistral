"""
Exercice — Number of Islands (LeetCode 200, Medium)
Énoncé :

On te donne une grille 2D contenant uniquement des "1" et des "0".
- "1" représente de la terre.
- "0" représente de l'eau.
- Une île est un ensemble de cellules terrestres connectées horizontalement ou verticalement.
- Les diagonales ne comptent pas.
"""

grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"]
]

from collections import deque

q = deque({(0,0)})
visited = set({(0,0)})

while q:
    x, y = q.popleft()

