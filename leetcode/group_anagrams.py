"""
Interviewer:

Given an array of strings strs, group the anagrams together.

Anagrams are words containing exactly the same characters with the same frequencies, regardless of their order.

"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Expected output (any group order):
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]


# Le but est de trier la clé dans un ordre pour qu'on retrouve en O(1) dans la map si la clé anagram existe ou pas

def group_anagrams(strs: list[str]) -> list[list[str]]:
    m = {}
    ret = []

    for st in strs:
        if not m:
            tmp = list(st)
            tmp.sort()
            m["".join(tmp)] = []
        else:
            tmp = list(st)
            tmp.sort()
            k = "".join(tmp)
            if k in m:
                m[k].append(st)
            else:
                m[k] = []

    for k in m:
        l = [k]
        l.extend(m[k])
        ret.append(l)
    return ret


if __name__ == "__main__":
    print(group_anagrams(strs))