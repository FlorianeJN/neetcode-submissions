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

        The lowest common ancestor is a node such that p and q are descendants
                      5
                    /   \
                   3     8
                  / \   / \             p = 3
                 1   4 7   9            q = 8
                  \
                   2

        Approach:
        - Go through the tree
        - if value is split between p and q (we have to go left AND right) -> value is lca
        - if value is p or q -> value is lca
        """
        node = root
        while node:
            if p.val < node.val < q.val or q.val < node.val < p.val:
                return node
            if p.val == node.val or q.val == node.val:
                return node
            
            if q.val > node.val:
                node = node.right
            if q.val < node.val:
                node = node.left
        
        return None

            

        