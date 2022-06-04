# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def LocateNode(head, n):
        # Take a slow and fast node
        slow = fast = head

        # find the nth node from the end:
        for i in range(n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow

    someNode = ListNode(-1)
    someNode.next = head

    # find the node in front of the nth node
    x = LocateNode(someNode, n + 1)
    x.next = x.next.next

    return someNode.next


if __name__ == '__main__':
    
    removeNthFromEnd([1, 2, 3, 4, 5], 2)
