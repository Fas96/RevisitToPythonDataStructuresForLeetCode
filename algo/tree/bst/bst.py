COUNT = [10]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class CusBST:
    def __init__(self):
        self.root = None

    def minimumValueBST(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def printBST(self, node):
        node = self.root
        temp = node
        if temp:
            print(temp.value)
            self.printBST(temp.left)
            self.printBST(temp.right)

    def containsValue(self, target):
        temp = self.root
        while temp is not None:
            if target == temp.value:
                return True
            if target < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def insertNode(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = Node(value)
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)

        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def bfs(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results


if __name__ == '__main__':
    cusBST = CusBST()
    cusBST.insertNode(47)
    cusBST.insertNode(21)
    cusBST.insertNode(76)
    cusBST.insertNode(18)
    cusBST.insertNode(27)
    cusBST.insertNode(52)
    cusBST.insertNode(82)
    print(cusBST.minimumValueBST(cusBST.root).value)
    print("=====")
    print(cusBST.bfs())
    print("DFS dfs_pre_order")
    print(cusBST.dfs_pre_order())
    print("dfs_post_order")
    print(cusBST.dfs_post_order())
    print("in order traversal")
    print(cusBST.dfs_in_order())
