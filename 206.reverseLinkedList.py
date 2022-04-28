# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        pre = None
        while head != None:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre