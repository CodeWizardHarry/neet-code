# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.

        steps:
        1. create a dummy node, left and right pointers
        2. find the nth node from the end of the list
        3. remove it

        """
        # step1
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        # step2
        while n > 0:
            n -= 1
            right = right.next



        while right:
            left = left.next
            right = right.next

        # left.next = right    mistake1  this removes all the nodes between slow and fast rather than the nth node from the end
        left.next = left.next.next

        return dummy.next


d   1   2   3   4   5
l                   r
        r