# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root.val==p.val or root.val==q.val:
            return root
        leftlca=self.lowestCommonAncestor(root.left,p,q)
        rightlca=self.lowestCommonAncestor(root.right,p,q)

        if leftlca is not None and rightlca is not None :
            return root
        elif leftlca is not None :
            return leftlca
        else:
            return rightlca