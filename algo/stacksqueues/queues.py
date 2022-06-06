class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class MainQueue:
    def __init__(self, val):
        new_node = Node(val)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.height -= 1
        return temp

    def printQueue(self):
        temp = self.first

        while temp is not None:
            print(temp.value,end='     ')
            temp = temp.next


if __name__ == '__main__':
    cusQueue = MainQueue(1)
    cusQueue.enqueue(23)
    cusQueue.printQueue()
    cusQueue.enqueue(34)

    cusQueue.dequeue()
    cusQueue.dequeue()
    print("\n")
    cusQueue.printQueue()
