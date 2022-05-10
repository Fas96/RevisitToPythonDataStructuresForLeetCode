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
            """while temp is not None:
                temp = temp.next
            temp = new_node"""
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':
    userDataList = LinkedList(3)
    print(userDataList.head.value)
    print(userDataList.head.next)
    print(userDataList.tail.value)
