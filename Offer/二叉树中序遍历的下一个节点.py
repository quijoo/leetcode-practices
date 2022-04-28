# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            # 返回右子树的最左子节点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
                
        else:
            p = pNode
            while True:
                # 有父节点 并且 p 是左节点
                # 1. 如果 p 是在任意 中间节点的左子树 则会最终递归到最近未访问根节点
                # 2. 如果 p 不是所有节点左子树上的点 那么返回 NULL
                if p.next and p.next.left == p:
                    return p.next
                if not p.next:
                    return None
                p = p.next