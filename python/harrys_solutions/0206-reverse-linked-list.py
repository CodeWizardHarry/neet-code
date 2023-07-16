# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

    def to_linked_list(self, lst: list):
        if not lst:
            return None

        head = ListNode()
        cur = head

        for v in lst:
            cur.next = ListNode(v)
            cur = cur.next

        return head.next

    def print_list(self, list: ListNode):
        while list is not None:
            print(list.val, end=" → ")
            list = list.next

        print("END")


s = Solution()
list1 = s.to_linked_list([1, 2, 3, 4, 5])
s.print_list(list1)
