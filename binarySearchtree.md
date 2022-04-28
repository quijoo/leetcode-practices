## 二叉树

***两种方法之间， 唯一的区别就是， 左、右子树为空的情况如何处理， 方法二可以有效地减小递归调用的层数***

1. 在当前函数处理子树为空的情况下， 可以有效地减小递归调用的层数
2. 

#### 1. 节点定义

```python
# 需要定义序列化函数方便打印
class Node:
    def __str__(self):
        return str(self.val)
    def __init__(self, val = None, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
```

#### 2. 插入函数实现

* 方法一

  **推荐** 这种方法需要传入root， 实现简单， 结构清晰， 函数开始处理空的子树， 而递归前不需要处理空子树

  ```python
      def insert_1(self, root, val):
          # 实现方法 1, 将处理空节点处理好了
          # 问题： 根节点值的必须定义好
          if root == None:
              root = Node(val = val)
          elif val < root.val:
              root.left = self.insert_1(root.left, val)
          elif val > root.val:
              root.right = self.insert_1(root.right, val)
          return root
  ```

  

* 方法二

  该方法不需要传入root， 但是实现不简洁， 需要在递归前判断子树是否为空

  ```python
  def insert_2(self, val):
      # 插入方法 2
      if self.val == None:
          self.val = val
      if val < self.val:
          if self.left == None:
              self.left = Node()
          self.left.insert_2(val)
      elif val > self.val:
          if self.right == None:
              self.right = Node()
          self.right.insert_2(val)
  ```

  

#### 3. 查询函数的实现也有两种

```python
# 这里仅仅展示最优雅的实现方法
def query(self, root, val):
    if root == None:
        return False
    if root.val == val:
        return True
    elif root.val < val:
        return self.query(root.right, val)
    else:
        return self.query(root.left, val)
```



#### 4. 最大/最小函数

**实现原理： 一直便利左子树。 或者右子树。**

这种情况下， 使用方法一更优。 他的 `api` 更加便利

```python
def max_1(self):
    if self.right:
        return self.right.max_1()
    else:
        return self

def max_2(self, root):
    if root.right:
        return self.max_2(root.right)
    else:
        return root

def min_1(self):
    if self.left:
        return self.left.min_1()
    else:
        return self

def min_2(self, root):
    if root.left:
        return self.min_2(root.left)
    else:
        return root
```



#### 5. remove 函数

删除节点的三种情况

1. 待删除节点 无左右节点**(None, None)**

   **直接删除**

2. 待删除节点 只有左、右子树**(None, Value)**

   **用该节点的子树代替父节点的子树**

3. 待删除结点既有左节点又有右节点**(Value, Value)**

   **找到该节点的右子树最小值来替代该节点， 然后在右子树删除最小值**

```python
def remove(self, root, val):
	# 根节点 == None 的情况    
    if root == None:
        return
    # 正常的便利
    elif val < root.val:
        root.left = self.remove(root.left, val)
    elif val > root.val:
        root.right = self.remove(root.right, val)
    # val == root.val 当找到一个值的方法
    else:
        # 左右全部不为空
        if root.left and root.right:
            temp = self.min_1(root.right)
            root.val = temp.val
            root.right = self.remove(root.right, temp.val)
        # 左右有一个为空
        elif root.left == None and root.right == None:
            root == None
        # 左右都为空
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
    return root
```

