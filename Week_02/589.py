#前序遍历: 根左右
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        tree = [root.val]
        if root.children:
            for child in root.children:
                tree += self.preorder(child)
        return tree


"""
# Definition for a Node.
class Node:
"""
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        def tranverse_path(root1):
            if not root:
                return []
            ans.append(root1.val)
            for i in root1.children:
                tranverse_path(i)
        tranverse_path(root)
        return ans