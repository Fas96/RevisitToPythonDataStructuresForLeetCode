class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class MainStack:
    def __init__(self, val):
        new_node = Node(val)
        self.top = new_node
        self.height = 1

    def pushNode(self, val):
        new_node = Node(val)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def popNode(self):
        if self.height == 0:
            return None
        temp = self.top

        self.top = self.top.next
        temp.next = None

        self.height -= 1
        return temp

    def printStack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end='  ')
            temp = temp.next


if __name__ == '__main__':
    cusStack = MainStack(23)
    cusStack.pushNode(234)
    cusStack.pushNode(3)
    cusStack.pushNode(4)
    cusStack.pushNode(5)
    cusStack.pushNode(6)
    cusStack.pushNode(7)
    cusStack.pushNode(4)
    cusStack.pushNode(3)
    cusStack.pushNode(4)
    cusStack.pushNode(45)
    cusStack.printStack()
    print("\n")
    cusStack.popNode()
    cusStack.popNode()
    cusStack.popNode()
    cusStack.popNode()
    cusStack.popNode()
    cusStack.printStack()
