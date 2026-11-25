"""
Exercice — LRU Cache (Medium)
HashMap
Cache
O(1)

Énoncé
Tu dois implémenter un cache avec une capacité maximale de capacity éléments.

Deux méthodes :
- get(key) : retourne la valeur associée à la clé, ou -1 si elle n'existe pas.
- put(key, value) : ajoute ou met à jour une entrée.
Règle importante : lorsque le cache est plein, tu dois supprimer l'élément le moins récemment utilisé (Least Recently Used).

Un get réussi et un put sur une clé existante rendent cette entrée récemment utilisée.
"""


# use doubly linked list for least recently used logic
# with python => OrderedDict ( equivalent of LinkedHashMap in java )
# HashMap + doubly linked list
# get => update head ( most recent )
# put => add then check capacity and remove the last node in the linked list (prev from the tail)

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        self.cache[key] = value
        self.cache.move_to_end(key, last=False)

        if len(self.cache) > self.capacity:
            removed = self.cache.popitem()
            print(f"LRU removed: {removed}")


lru_cache = LRUCache(capacity=2)

lru_cache.put("key", 1)
lru_cache.put("keyx", 1)
lru_cache.put("keyb", 1)

print(lru_cache.cache)

# cache = OrderedDict()
# cache["A"] = 1
# cache["B"] = 2
# cache["C"] = 3
# cache.move_to_end("A", last=True)
# print(cache)

# class LRUCache:

#     def __init__(self, capacity: int):
#         pass

#     def get(self, key: int) -> int:
#         pass

#     def put(self, key: int, value: int) -> None:
#         pass




# lru_cache = LRUCache(capacity=5)


