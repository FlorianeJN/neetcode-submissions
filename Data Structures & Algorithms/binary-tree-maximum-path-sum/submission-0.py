# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        We are given the root of a non-empty binary tree.
        We want the maximum path sum of any non-empty path

        Brute force approach -> Compute every path and keep track of max
        Time complexity: O(n^2)
        Space complexity: O(h)

        another approach -> use bottom up approach: as we go up take
        the max value?
        """

        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum
            if not node:
                return 0

            # First we do the recursive calls (bottom up)
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            max_path_sum = max(left + right + node.val, max_path_sum)
            return node.val + max(left,right)
        dfs(root)
        return max_path_sum
  