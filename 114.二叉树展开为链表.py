class Solution:
    def __init__(self):
        self.pre = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.pre
        root.left = None
        pre = root