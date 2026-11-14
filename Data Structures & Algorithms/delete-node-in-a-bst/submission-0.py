# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        First find the node
        For deletion we have two options:
            - The node to be deleted has 0 or 1 child
            - The node to be deleted has 2 children

        If the node has 0 or 1 child, we can remove the node and append the root to the node's present child

        If the node has 2 children, we need to overwrite the root with the minimum node's value
        (from the right subtree) and remove that minimum node from the tree.
        """

        if not root:
            return None

        # the node that needs to be deleted is in the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        # the node that needs to be deleted is in the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        # the node that needs to be deleted is the current one (root)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # we have both children
            min_node = self.find_min_node(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right,min_node.val)
        
        return root

    def find_min_node(self,root):
        while root and root.left:
            root = root.left
        return root

        
        