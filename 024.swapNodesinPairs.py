class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        s, pre = ListNode(None), ListNode(None)
        if head == None or head.next == None:
            return head
        s.next = head.next
        pre.next = head
        while head and head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            pre.next = tmp
            pre = head
            head = head.next
        return s.next