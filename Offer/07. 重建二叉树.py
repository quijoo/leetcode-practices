# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        val = preorder[0]
        index = inorder.index(val)
        root = TreeNode(val)

        root.left = self.buildTree(preorder[1:index+1], inorder[:index]) if index != 0 else None
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:]) if index != len(preorder)-1 else None

        return root