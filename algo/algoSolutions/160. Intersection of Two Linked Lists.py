class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# difficulty  of different lengths
# lets loop all from nodes from   start
# combine the nodes and check for case where is no intersection
# list A + list B has the same length as list B + list A.
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ptr1, ptr2 = headA, headB

        while ptr1 != ptr2:
            if ptr1 is None:
                ptr1 = headB
            else:
                ptr1 = ptr1.next
            if ptr2 is None:
                ptr2 = headA
            else:
                ptr2 = ptr2.next
        return ptr1


if __name__ == '__main__':
    sln = Solution()
    sln.getIntersectionNode()
