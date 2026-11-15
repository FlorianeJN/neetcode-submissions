# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """                
        Need to use BFS to change subtrees per level
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()
                curr.left , curr.right = curr.right, curr.left

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root
   