from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        mergeLinkedListNode = ListNode(-1)
        temporal = mergeLinkedListNode
        result = []

        for ll in lists:
            while ll:
                result.append(ll.val)
                ll = ll.next

        resultSorted = sorted(result)

        for val in resultSorted:
            temporal.next = ListNode(val)
            temporal = temporal.next
        return mergeLinkedListNode.next()


if __name__ == '__main__':
    soln = Solution()
    soln.mergeKLists([[]])
