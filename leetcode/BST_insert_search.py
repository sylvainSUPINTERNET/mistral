from collections import deque


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BST:
    def __init__(self, nums):
        self.nums = nums
        self.root = None

        for value in nums:
            self.build_insert(value)

    # From empty tree
    def build_insert(self, value) -> Node:
        if self.root is None:
            self.root = Node(value)
            return self.root

        current_node = self.root

        while True:
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value, parent=current_node)
                    return self.root

            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value, parent=current_node)
                    return self.root

            else:
                return self.root
    # BFS
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

    # Using BST properties
    def search_optim(self, value) -> bool:
        node = self.root

        while node is not None:
            if node.value == value:
                return True

            if value > node.value:
                node = node.right
            else:
                node = node.left

        return False

    # rule : left -> node -> right
    # en gros on va tout à gauche tant qu'on peut, max arrivé => on garde la value et on pop la stack ( avoir le parent du dernier explorer ) 
    # puis on explore celui à droite et on répète cette logique
    def inorder(self) -> list[int]:
        result = []
        stack = [self.root] if self.root is not None else []
        current = self.root

        while stack:
            if current is not None and current.left is not None:
                stack.append(current.left)
                current = current.left
            else:
                s = stack.pop()
                result.append(s.value)

                # Changement de direction
                current = s.right

                if current is not None:
                    stack.append(current)

        return result



        # if self.root.left != None:
        #     stack.append(self.root.left)

        # current_node = self.root
        
        # while current_node.left is not None:
        #     current_node = current_node.left
        #     print(current_node.value)
        #     stack.append(current_node)

        # if current_node.left is None:
        #     print(current_node.value)
        #     stack.append(current_node)

        # print("JE")
        # while stack:
        #     p = stack.pop()
        #     print(p.value)


        # while stack:
        #     current_node = stack.pop()
        #     yield current_node.value

        return []

if __name__ == "__main__":
    nums = [50, 20, 70, 10, 30, 60, 80]
    bst = BST(nums)

    print(bst.inorder())

    # print(bst.search(20))
    # print(bst.search(100))
    # bst.insert(25)
    # print(bst.inorder())