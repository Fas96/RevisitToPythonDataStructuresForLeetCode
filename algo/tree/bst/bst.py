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


if __name__ == '__main__':
    cusBST = CusBST()
    cusBST.insertNode(3)
    cusBST.insertNode(1)
    cusBST.insertNode(-1)
    cusBST.insertNode(4)
    cusBST.insertNode(0)
    print(cusBST.minimumValueBST(cusBST.root).value)
