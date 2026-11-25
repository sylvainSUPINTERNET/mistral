from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, nums):
        self.nums = nums
        self.root = None

        for value in nums:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    return
            
            if current_node.value < value:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    return


    # BFS ( largeur ) - pas d'exploit du BST impl "simple"
    def search(self, value) -> bool:
        if self.root.value == value:
            return True
        
        q = deque()
        q.appendleft(self.root)

        while len(q) != 0:
            node = q.pop()
            if node.value == value:
                return True
            if node.right is not None:
                q.appendleft(node.right)
            if node.left is not None:
                q.appendleft(node.left)
        return False

    # using BST properties ( BST à gauche tjr le chemin vers le plus petit, à droite tjr le chemin vers le plus grand)
    def search_optim(self, value) -> bool:
        if self.root.value == value:
            return True
        
        q = deque()
        q.appendleft(self.root)

        while len(q) != 0:
            node = q.pop()
            if node.value == value:
                return True

            if value > node.value:
                q.appendleft(node.right)

            if value < node.value:
                q.appendleft(node.left)
            
            # if node.right is not None:
            #     q.appendleft(node.right)
            # if node.left is not None:
            #     q.appendleft(node.left)
        return False


if __name__ == "__main__":
    nums = [50, 20, 70, 10, 30, 60, 80]

    bst = BST(nums)
    print(bst.search(20))
    print(bst.search(100))



