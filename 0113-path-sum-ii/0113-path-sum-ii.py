# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result=[]
        def dfs(node,target,current_path):
            if not node:
                return
            current_path.append(node.val)
            if not node.left and not node.right and node.val==target:
                result.append(list(current_path))
            else:
                remaining=target-node.val
                dfs(node.left,remaining,current_path)
                dfs(node.right,remaining,current_path)
            current_path.pop()

        dfs(root,targetSum,[])
        return result


        