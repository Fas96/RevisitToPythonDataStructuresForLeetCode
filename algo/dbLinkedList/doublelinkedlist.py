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

    def prependNode(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

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

    def popFirstNode(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def removeNodeAtPosition(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirstNode()
        if index == self.length - 1:
            return self.popNode()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def insertNodeAtPosition(self, index, value):
        if index == 0:
            self.prependNode(value)
        if index == self.length:
            self.append(value)
        tempBeforePosition = self.get(index - 1)
        tempAfterPosition = tempBeforePosition.next
        new_node = Node(value)

        new_node.next = tempAfterPosition
        new_node.prev = tempBeforePosition

        tempBeforePosition.next = new_node
        tempAfterPosition.prev = new_node

        self.length += 1
        return True

    def set_node_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < (self.length / 2):
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def printDbLinkedList(self):
        if self.length == 0:
            print("List is Empty")
            return "EMPTY LIST"
        temp = self.head

        while temp is not None:
            print(temp.value, end='  ')
            temp = temp.next


if __name__ == '__main__':
    dbLinkedListUsers = DLinkedList(2)
    dbLinkedListUsers.append(10)
    dbLinkedListUsers.append(12)
    dbLinkedListUsers.append(15)
    dbLinkedListUsers.prependNode(100)
    dbLinkedListUsers.prependNode(200)
    dbLinkedListUsers.printDbLinkedList()
    print("\n----------------")
    dbLinkedListUsers.popFirstNode()
    dbLinkedListUsers.printDbLinkedList()
    print("----get index---", dbLinkedListUsers.length)
    print(dbLinkedListUsers.get(4).value)

    dbLinkedListUsers.set_node_value(0, 000)
    dbLinkedListUsers.set_node_value(1, 1000)
    dbLinkedListUsers.set_node_value(2, 2000)
    dbLinkedListUsers.set_node_value(3, 3000)
    print("\n--")
    dbLinkedListUsers.printDbLinkedList()
    dbLinkedListUsers.insertNodeAtPosition(2, 900)
    dbLinkedListUsers.insertNodeAtPosition(3, 900)
    dbLinkedListUsers.insertNodeAtPosition(4, 900)
    print("\n--")
    dbLinkedListUsers.printDbLinkedList()
    dbLinkedListUsers.removeNodeAtPosition(0)
    dbLinkedListUsers.removeNodeAtPosition(1)
    dbLinkedListUsers.removeNodeAtPosition(4)
    dbLinkedListUsers.removeNodeAtPosition(dbLinkedListUsers.length-1)
    print("\nRemoved")
    dbLinkedListUsers.printDbLinkedList()
