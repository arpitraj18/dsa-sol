# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inord=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inord.append(node.val)
            inorder(node.right)
        inorder(root)
        left=0
        right=len(inord)-1
        while left<right:
            current_sum=inord[left]+inord[right]
            if current_sum==k:
                return True
            elif current_sum<k:
                left+=1
            else:
                right-=1
        return False