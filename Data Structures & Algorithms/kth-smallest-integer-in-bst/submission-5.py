# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        We could go through the BST using inorder traversal 
        (inorder gives sorted order) and fill an array. Then return
        arr[k-1]
        Time complexity: O(n)
        Space complexity: O(n)

        another approach:
        Go through BST using inorder traversal but keep track of count of 
        nodes traversed. return kth node's value
        Time complexity: O(n)
        Space complexity: O(h)
        """

        # Recursive DFS version
        count = 0
        kth_smallest = None

        def dfs(node):
            nonlocal kth_smallest
            nonlocal count
            if not node:
                return
            
            # early return
            if kth_smallest is not None:
                return
            
            dfs(node.left)
            if count == k - 1:
                kth_smallest = node.val
            
            count += 1
            dfs(node.right)
            
        dfs(root)
        return kth_smallest
        