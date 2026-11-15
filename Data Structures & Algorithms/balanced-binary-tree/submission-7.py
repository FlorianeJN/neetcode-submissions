# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Use bottom up approach
        For each node evaluate max depth left and right subtree
        """
        
        def dfs(node):
            if not node:
                return (True,0)

            # recursive calls for bottom up
            left_ok, left_h = dfs(node.left)
            right_ok, right_h = dfs(node.right)
            
            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
            return (balanced,1 + max(left_h,right_h))

        res,_ = dfs(root)
        return res



            
            
        