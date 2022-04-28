import queue
class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        s = queue.Queue()
        s.put(root)
        res = []
        q = queue.Queue()
        while not s.empty() or not q.empty():
            tmp = []
            while not s.empty():                
                r = s.get()
                tmp.append(r.val)
                if r.right:
                    q.put(r.right)
                if r.left:
                    q.put(r.left)
                
            if len(tmp)!=0:
                tmp.reverse()
                res.append(tmp)
            tmp = []
            while not q.empty():                            
                r = q.get()
                tmp.append(r.val)
                if r.right:
                    s.put(r.right)
                if r.left:
                    s.put(r.left)

            if len(tmp)!=0:
                # tmp.reverse()
                res.append(tmp)
        return res