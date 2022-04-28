# 快慢指针方法
# 快指针： 每次两个节点
# 慢指针： 每次一个节点


# 通过这个例子， 学会了快慢指针， 学会了try-catch
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 巧用 try catch
class Solution(object):
    def hasCycle(self, head):
        try:
            # 这里的 head一定需要是慢指针，而 fast 是快指针， 否则运行轨迹不是正常
            slow, fast = head, head.next
            while slow is not fast:
                slow, fast = slow.next, fast.next.next
            return True
        except:
            return False

# while 语句中如果没有fast.next的话就会出问题
class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

# 将访问到的值置为空
class Solution(object):
    def hasCycle(self, head):
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False