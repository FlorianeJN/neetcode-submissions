# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        left tree must have nodes less than node
        right tree must have nodes greater than node
        both left and right subtrees are also binary search trees

        if i do top down, propagate valid range for node's value
        if we go right update lower_bound
        if we go left update upper_bound
        """

        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True
            if not lower_bound < node.val < upper_bound:
                return False

            return dfs(node.right, node.val, upper_bound) and dfs(
                node.left, lower_bound, node.val
            )

        return dfs(root, float("-inf"), float("inf"))
