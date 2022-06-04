class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def popNode(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def append(self, val):
        new_node = Node(val)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def printDbLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='  ')
            temp = temp.next


if __name__ == '__main__':
    dbLinkedListUsers = DLinkedList(2)
    dbLinkedListUsers.append(3)
    dbLinkedListUsers.append(4)
    dbLinkedListUsers.append(5)
    dbLinkedListUsers.printDbLinkedList()
