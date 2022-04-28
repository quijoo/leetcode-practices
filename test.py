# class Node:
#     # insert 和 remove 都是构造形的， 所以是构造 root 的 left ， right 然后 return root
#     def __str__(self):
#         return str(self.val)
#     def __init__(self, val = None, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def insert(self, root, val):
#         if root == None:
#             root = Node(val = val)
#         elif root.val < val:
#             root.right = self.insert(root.right, val)
#         elif root.val > val:
#             root.left = self.insert(root.left, val) 
#         return root
#     def query(self, root, val):
#         if root == None:
#             return False
#         elif root.val < val:
#             return query(root.right, val)
#         elif root.val > val:
#             return query(root.left, val)
#         else:
#             return True
#     def min(self, root):
#         if root.left == None:
#             return root
#         return self.min(root.left)

#     def max(self, root):
#         if root.right == None:
#             return root
#         return self.max(root.right)

#     def remove(self, root, val):
#         if root == None:
#             return
#         elif root.val < val:
#             root.right = remove(root.right, val)
#         elif root.val > val:
#             root.right = remove(root.left, val)
#         else:
#             if root.left == None and root.right == None:
#                 root = None
#             elif root.left != None and root.right != None:
#                 tmp = self.min(root.right)
#                 root.val = tmp.val
#                 root.right = self.remove(root.right, tmp.val)
                
#             elif root.right != None:
#                 root = root.right
#             else:
#                 root = root.left
#         return root
                
# if __name__ == "__main__":
#     pass


    def remove(self, root, val):
        if root == None:
            return
        elif root.val < val:
            root.right = self.remove(root.right, val)
        elif root.val > val:
            root.left = self.remove(root.left, val)
        else:
            if root.left and root.right:
                tmp = self.min(root.right)
                root.val = tmp.val
                root.right = self.remove(root.right, tmp.val)
            elif root.left == None and root.right == None:
                root = None
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
        return root