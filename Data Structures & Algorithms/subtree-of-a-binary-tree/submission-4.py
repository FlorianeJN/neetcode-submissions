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
        Time Complexity: O(n^m)

        another approach: serialize trees. check if subroot_string is within root_string
        Time Complexity: O(n+m)
        Space Complexity: O(n+m)
        """
        root_str = self.serialize(root)
        subroot_str = self.serialize(subRoot)

        return subroot_str in root_str

    def serialize(self,root) -> str:
        output = ""

        def dfs(node):
            nonlocal output
            if not node:
                output += "null"
                return
            output += "#" + str(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output
            
