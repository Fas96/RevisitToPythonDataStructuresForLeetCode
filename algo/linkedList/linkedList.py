"""

{
"value":45
"next":None
}

"""

head = {
    "value": 10,
    "next": {
        "value": 20,
        "next": {
            "value": 30,
            "next": {
                "value": 40,
                "next": {
                    "value": 50,
                    "next": {
                        "value": 60,
                        "next": None
                    }
                }
            }
        }
    }
}


def traverse():
    while head['next'] is not None:
        print(head['next']['value'])
        head['next'] = head['next']['next']


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def popItem(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        """When more than one item exist in the linkedList"""
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        """If only one item exist"""
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prependItem(self, value):
        new_node = Node(value)

        '''If Linked list is already empty'''
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            '''if linked list has items'''
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        """move head to next and set previous head.next(temp) to None"""
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        """set tail to None when all the list is empty"""
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length < index:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_Value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_Node(self, index, value):
        if index == 0:
            return self.prependItem(value)
        if index == self.length:
            return self.append(value)
        '''The index before the index we want to insert'''
        temp = self.get(index - 1)
        '''new node'''
        new_node = Node(value)
        '''our new node points to the node after temp'''
        new_node.next = temp.next;
        '''our temp at index-1 now points to the new node'''
        temp.next = new_node
        self.length += 1
        return True

    def reverseLinkedList(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before

            before = temp
            temp = after

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            return None
        # temp=self.get(index-1)
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.popItem()

        prev = self.get(index - 1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # def reverse(self):
    #     temp = self.head
    #     self.head = self.tail
    #     self.tail = temp
    #     '''before temp after'''
    #     before = None
    #     after = temp.next
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #
    #         before = temp
    #         temp = after

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='  ')
            temp = temp.next


if __name__ == '__main__':
    userDataList = LinkedList(1)
    userDataList.append(2)
    userDataList.append(3)
    userDataList.append(4)
    userDataList.append(5)
    userDataList.append(6)
    userDataList.append(7)
    userDataList.append(8)
    userDataList.append(9)
    userDataList.append(10)
    userDataList.append(11)
    userDataList.append(12)
    userDataList.append(13)
    userDataList.append(14)
    userDataList.append(15)
    # userDataList.popItem()
    userDataList.printList()
    # userDataList.popItem()
    # userDataList.printList()
    # print(userDataList.popItem())
    # userDataList.printList()

    print("\n==========")
    # print(userDataList.popItem())
    userDataList.reverseLinkedList()
    userDataList.printList()
