class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        first = head
        if head == None:
            return head
        elif head.next == None:
            return head
        second = head.next
        pre = head
        while second and second.next:
            tmp = second.next.next
            second.next.next = first.next
            first.next = second.next
            second.next = tmp
            first = first.next
            second = second.next
        return pre