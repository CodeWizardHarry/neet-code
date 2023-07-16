# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.

        steps:
        1. create dummy node, left and right pointers
        2. find the nth node from the end of the list
        3. remove it

        """
        #step1    
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        #step2

        while n > 0:
            n-=1
            right = right.next

        while right:
            left = left.next
            right = right.next

        #step3
        left.next = left.next.next
        
        return dummy.next

        
