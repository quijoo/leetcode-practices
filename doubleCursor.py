# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#  python 指针问题， 如果对对象直接赋值会出现覆盖的情况
#  这里只对对象的 next 属性进行赋值
# 这个题： 对于对象的赋值并不能改变原对象， 但是对象的属性是引用的（不要直接对对象赋值）
class Solution(object):
    def removeNthFromEnd(self, head, n):
        k = 0
        Node = ListNode(None)
        Node.next = head
        first = second = Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return Node.next
