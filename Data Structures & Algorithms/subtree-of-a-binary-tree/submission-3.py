# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Brute force approach: go through tree and check if same tree
        every time we find a node thats the same as subroot
        Time Complexity: O(n^2) if n is the length of the first tree
        """

        if not root and not subRoot:
            return True

        # First DFS until we find first matching node
        stack = [root]
        subroot_found = False

        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if self.isSameTree(cur,subRoot):
                    return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False

    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
