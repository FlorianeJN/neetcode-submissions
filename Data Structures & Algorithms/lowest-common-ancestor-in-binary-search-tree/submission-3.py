# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Input: binary search tree (BST), two nodes p and q
        Output: lowest common ancestor

        Approach:
        - Go through the tree
        - if value is split between p and q (we have to go left AND right) -> value is lca
        - if value is p or q -> value is lca
        """
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        # if the value is p or q, the node is the lca
        if p.val == root.val or q.val == root.val:
            return root

        # Go left and right
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
