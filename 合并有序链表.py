# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        front = ListNode()
        cur = front
        while l1 or l2:
            # print(l1.val, l2.val)
            if  l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next
            elif (l1 == None):
                cur.next = l2
                cur = l2
                l2 = l2.next
            else:
                cur.next = l1
                cur = l1
                l1 = l1.next
        return front.next
