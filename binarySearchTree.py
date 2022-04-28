# 二叉搜索树不用处理重复数据， 因为搜索本来就要去重
class Node:
    def __str__(self):
        return str(self.val)
    def __init__(self, val = None, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
    def insert(self, root, val):
        # 实现方法 1, 将处理空节点处理好了
        # 问题： 根节点值的必须定义好
        if root == None:
            root = Node(val = val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        if root == None:
            return False
        elif root.val == val:
            return True
        elif root.val > val:
            return self.query(root.left, val)
        else:
            return self.query(root.right, val)

            
    def max(self, root):
        if root.right:
            return self.max(root.right)
        else:
            return root


    def min(self, root):
        if root.left:
            return self.min(root.left)
        else:
            return root

    def remove(self, root, val):
        # 删除节点的三种情况
        # 1. 待删除节点 无左右节点，            直接删除
        # 2. 待删除节点 只有左、右子树           用该节点的子树代替父节点的子树
        # 3. 待删除结点既有左节点又有右节点       找到该节点的右子树最小值来替代该节点， 然后在右子树删除最小值
        if root == None:
            return
        elif val < root.val:
            root.left = self.remove(root.left, val)
        elif val > root.val:
            root.right = self.remove(root.right, val)
        else:
            # 相等， 即找到了
            if root.left and root.right:
                # 最复杂的情况
                temp = self.min_1(root.right)
                root.val = temp.val
                root.right = self.remove(root.right, temp.val)
            elif root.left == None and root.right == None:
                root == None
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
        return root




if __name__ == "__main__":
    pass
