#根据以上定义，若 rootroot 是 p, qp,q 的 最近公共祖先 ，则只可能为以下情况之一：p 和 q 在 rootroot 的子树中，且分列 root的 异侧（即分别在左、右子树中）； p = root ，且 q 在root 的左或右子树中；q = root ，且 p 在root 的左或右子树中；
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q: return root
        left = self.lowestCommonAncestor( root.left,p,q)
        right= self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root

