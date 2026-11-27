"""
Exercice — Koko Eating Bananas (LeetCode 875, Medium)
Koko possède n tas de bananes. Chaque tas contient un certain nombre de bananes.

Elle dispose de h heures maximum pour manger toutes les bananes.

Elle doit choisir une vitesse de consommation k bananes par heure.
Règles
1. Chaque heure, Koko choisit un seul tas.
2. Elle mange jusqu'à k bananes dans ce tas.
3. Si le tas contient moins de k bananes, elle le termine, mais ne peut pas commencer un autre tas pendant cette heure.
4. Elle veut manger le plus lentement possible, tout en respectant les h heures.
Objectif
Trouver la plus petite valeur entière k permettant de terminer tous les tas en h heures maximum.

"""

piles = [3, 6, 7, 11]
hours_max = 8

# Résultat attendu : 4, ça veut dire au minimum mangé 4 bananes par heure pour finir tous les tas dans les 8 heures.

from math import ceil

def minEatingSpeed(piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total_h = 0
            for p in piles:
                total_h += ceil(p / mid)

            if total_h > h:
                left = mid + 1
            else:
                right = mid

        return left


f = minEatingSpeed(piles, hours_max)
print(f)