# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Node is good if the path from the root to x contains
        no node with a value greater than node
        
        approach: pass down max value seen to far.
        node is good if node.val >= max_value_seen so far
        top down DFS
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        count = 0

        def dfs(node,max_so_far):
            nonlocal count
            if not node:
                return
            
            if node.val >= max_so_far:
                count += 1
            
            new_max = max(max_so_far,node.val)
            dfs(node.left,new_max)
            dfs(node.right,new_max)
  
        dfs(root,root.val)
        return count
