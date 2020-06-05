"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        ans = []
        while queue:
            l = []
            for _ in range(len(queue)):# 其实我想请您解释一下这个loop
                node = queue.popleft()
                l.append(node.val)
                queue.extend(node.children)
            ans.append(l)
        return ans
# 方法二 BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        def bfs(root):
            queue = [root]
            while queue:
                l = []
                n = []
                for node in queue:
                    l.append(node.val)
                    for ch in node.children:
                        n.append(ch)
                ans.append(l)
                queue = n
        
        ans = []
        bfs(root)
        return ans